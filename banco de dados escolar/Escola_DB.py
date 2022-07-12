import psycopg2
from confidentials import senha


class BancoDeDados:
    def __init__(self, host='', port='', dbname='', user='', password='') -> None:
        self.con = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        self.cursor = self.con.cursor()

    def geradorSQLInsert(self, *args, nome_tabela=''):
        dados = args
        dadosDesempacotados = []
        for valores in dados:
            dadosDesempacotados.append(f'{valores}')
        dadosDesempacotados = tuple(dadosDesempacotados)
        sql = f"INSERT INTO {nome_tabela} VALUES {dadosDesempacotados}"
        return sql

    def verificadorEnderecoExiste(self, logradouro, numero):
        sql = "SELECT logradouro, numero, cod_end  FROM endereco"
        self.cursor.execute(sql)
        self.con.commit()
        pesquisa = self.cursor.fetchall()
        for valores in pesquisa:
            if logradouro == valores[0] and numero == valores[1]:
                return valores[-1]
        return False


class Escola(BancoDeDados):
    def cadastroAluno(self, cpf, nome_aluno, sobrenome_aluno, endereco):
        sql = self.geradorSQLInsert(cpf, nome_aluno, sobrenome_aluno, endereco, nome_tabela='aluno')
        self.cursor.execute(sql)
        self.con.commit()

    def cadastroEndereco(self, logradouro, numero, bairro, complemento):
        verificaExistencia = self.verificadorEnderecoExiste(logradouro, numero)
        if verificaExistencia:
            return verificaExistencia
        else:
            sql = self.geradorSQLInsert(logradouro, numero, bairro, complemento, nome_tabela='endereco')
            self.cursor.execute(sql)
            self.con.commit()
            codigoExistente = self.verificadorEnderecoExiste(logradouro, numero)
            return codigoExistente


if __name__ == '__main__':
    e = Escola('192.168.0.4', '5432', 'db_escola', 'fernando', senha)
    endereco = e.cadastroEndereco('João Naves de Avila', '4512', 'João Padilha Almeida da Silva Saravá', '')
    e.cadastroAluno('98585732281', 'Fernando', 'Jovem', endereco)
    # a = e.geradorSQLInsert('okokos', 'dmkmkdmkfdkm', 'ososos', nome_tabela='aluno')
    # print(a)
