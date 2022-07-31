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

    def abortar(self):
        self.con.rollback()

    def buscarDados(self):
        return self.cursor.fetchall()

    def geradorSQLInsert(self, *args, nome_tabela=''):
        dados = args
        # operador = ''
        dadosDesempacotados = ''
        for n, valores in enumerate(dados):
            if valores == 'default':
                if n == 0:
                    # operador += '(%s, '
                    dadosDesempacotados += f'({valores}, '
                elif n == len(dados) - 1:
                    # operador += '%s)'
                    dadosDesempacotados += f'{valores})'
                else:
                    # operador += '%s, '
                    dadosDesempacotados += f'{valores}, '
            else:
                if n == 0:
                    # operador += '(%s, '
                    dadosDesempacotados += f"('{valores}', "
                elif n == len(dados) - 1:
                    # operador += '%s)'
                    dadosDesempacotados += f"'{valores}')"
                else:
                    # operador += '%s, '
                    dadosDesempacotados += f"'{valores}', "
        sql1 = f"INSERT INTO {nome_tabela} VALUES {dadosDesempacotados}"
        return sql1

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

    def cadastroTabelas(self, nome_tabela, **kwarg,):
        colunas = [v for k, v in kwarg.items()]
        sql = self.geradorSQLInsert(*colunas, nome_tabela=nome_tabela)
        try:
            self.executar(sql)
            self.enviar()
        except psycopg2.Error as erro:
            self.abortar()
            print(f'O registro {colunas}, não foi efetuado com sucesso!')
            print(erro)

    def cadastroEndereco(self, default, logradouro, numero, bairro, complemento) -> int:
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
    # e.cadastroTabelas('aluno', cpf='98516232281', nome_aluno='Marijuana', sobrenome_aluno="Darc", endereco=endereco)
    # e.cadastroTabelas('departamento', cod_dep='default', nome_dep='Química')
    # e.cadastroTabelas('departamento', cod_dep='default', nome_dep='Física')
    # e.cadastroTabelas('departamento', cod_dep='default', nome_dep='Computação')
    # e.cadastroTabelas('departamento', cod_dep='default', nome_dep='Engenharia')
    # e.cadastroTabelas('departamento', cod_dep='default', nome_dep='Matemática Avançada')
    # e.cadastroTabelas('departamento', cod_dep='default', nome_dep='Ciências Humanas')
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Licenciatura em Física', cod_dep=16)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Licenciatura em Matemática', cod_dep=19)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Licenciatura em Geografia', cod_dep=20)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Licenciatura em História', cod_dep=20)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Licenciatura em Educação Física', cod_dep=20)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Licenciatura em Português', cod_dep=20)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia Civil', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia Química', cod_dep=15)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia de Software', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia de Hardware', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia de Produção', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia de Alimentos', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia Aeronáutica', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia Espacial', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Engenharia de Foguetes', cod_dep=18)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Libras', cod_dep=20)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Manufaturas', cod_dep=19)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Manutenção de Computadores', cod_dep=17)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Limpeza de Gabinetes', cod_dep=17)
    # e.cadastroTabelas('curso', cod_c='default', nome_c='Arquitetura de Redes', cod_dep=17)
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Maria', sobrenome_prof='Bezarra')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Penisvaldo', sobrenome_prof='Bucetâneo')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Rondisley', sobrenome_prof='Proxeneta')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Betoneira', sobrenome_prof='Jualistina')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Robervaldo', sobrenome_prof='Juarez')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Francinildo', sobrenome_prof='Perclorético')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Rudisnilson', sobrenome_prof='Pretório')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Avacalhadislson', sobrenome_prof='Trincado')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Penisnildo', sobrenome_prof='Caralhudo')
    # e.cadastroTabelas('professor', matricula_prof='default', nome_prof='Frangostosky', sobrenome_prof='Peneirado')
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Análise Gramatical', matricula_prof=11)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Fundamentos de Linguagem C', matricula_prof=10)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Calculo I', matricula_prof=9)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Cosmologia', matricula_prof=8)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Anatomia Humana', matricula_prof=7)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Geologia', matricula_prof=6)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Química Analítica', matricula_prof=5)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Cinemática', matricula_prof=4)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='Banco de Dados', matricula_prof=3)
    # e.cadastroTabelas('disciplina', cod_d='default', nome_disciplina='História Geral', matricula_prof=2)
    # e.cadastroTabelas('prerequisito', cod_requisitante=2, cod_requisitado=10)
    e.cadastroTabelas('prerequisito', cod_requisitante=2, cod_requisitado=10)
    e.fecharConexao()
    # a = e.geradorSQLInsert('okokos', 'dmkmkdmkfdkm', 'ososos', nome_tabela='aluno')
    # print(a)
