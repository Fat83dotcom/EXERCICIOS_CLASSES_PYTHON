import psycopg2
from confidentials import senha
import abc


class BancoDeDados(abc.ABC):
    def __init__(self, host='', port='', dbname='', user='', password='') -> None:
        self.con = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        self.cursor = self.con.cursor()

    def fecharConexao(self):
        self.con.close()

    def executar(self, sql):
        self.cursor.execute(sql)

    def enviar(self):
        self.con.commit()

    def buscarDados(self):
        return self.cursor.fetchall()

    def geradorSQLInsert(self, *args, nome_tabela=''):
        dados = args
        dadosDesempacotados = ''
        for n, valores in enumerate(dados):
            if valores == 'default':
                if n == 0:
                    dadosDesempacotados += f'({valores}, '
                elif n == len(dados) - 1:
                    dadosDesempacotados += f'{valores})'
                else:
                    dadosDesempacotados += f'{valores}, '
            else:
                if n == 0:
                    dadosDesempacotados += f"('{valores}', "
                elif n == len(dados) - 1:
                    dadosDesempacotados += f"'{valores}')"
                else:
                    dadosDesempacotados += f"'{valores}', "
        sql = f"INSERT INTO {nome_tabela} VALUES {dadosDesempacotados}"
        return sql

    def verificadorEnderecoExiste(self, logradouro, numero):
        sql = "SELECT logradouro, numero, cod_end  FROM endereco"
        self.executar(sql)
        self.enviar()
        pesquisa = self.buscarDados()
        for valores in pesquisa:
            if logradouro == valores[0] and numero == valores[1]:
                return valores[-1]
        return False


class Escola(BancoDeDados):
    def __init__(self, host='', port='', dbname='', user='', password='') -> None:
        super().__init__(host, port, dbname, user, password)

    def cadastroAluno(self, cpf, nome_aluno, sobrenome_aluno, endereco):
        sql = self.geradorSQLInsert(cpf, nome_aluno, sobrenome_aluno, endereco, nome_tabela='aluno')
        self.executar(sql)
        self.enviar()

    def cadastroEndereco(self, default, logradouro, numero, bairro, complemento):
        verificaExistencia = self.verificadorEnderecoExiste(logradouro, numero)
        if verificaExistencia:
            return verificaExistencia
        else:
            sql = self.geradorSQLInsert(default, logradouro, numero, bairro, complemento, nome_tabela='endereco')
            self.executar(sql)
            self.enviar()
            codigoExistente = self.verificadorEnderecoExiste(logradouro, numero)
            return codigoExistente


if __name__ == '__main__':
    e = Escola('192.168.0.4', '5432', 'db_escola', 'fernando', senha)
    endereco = e.cadastroEndereco('default', 'Almondegas Podres de Melo', '12', 'João Padilha Saravá', '')
    e.cadastroAluno('98516232281', 'Marijuana', "Darc", endereco)
    e.fecharConexao()
    # a = e.geradorSQLInsert('okokos', 'dmkmkdmkfdkm', 'ososos', nome_tabela='aluno')
    # print(a)
