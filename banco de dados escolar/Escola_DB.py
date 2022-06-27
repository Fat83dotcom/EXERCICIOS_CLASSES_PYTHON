import psycopg2
from confideltials import senha


class Escola:
    def __init__(self, host='', port='', dbname='', user='', password='') -> None:
        self.con = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        self.cursor = self.con.cursor()

    def cadastroAluno(self, cpf, nome_aluno, sobrenome_aluno, endereco):
        sql = f"insert into aluno values('{cpf}', '{nome_aluno}', '{sobrenome_aluno}', '{endereco}')"
        self.cursor.execute(sql)
        self.con.commit()

    def cadastroEndereco(self, rua, numero, bairro, complemento):
        sql = f"insert into endereco values (default, '{rua}', '{numero}', '{bairro}', '{complemento}')"
        self.cursor.execute(sql)
        sql = "select max(cod_end) from endereco"
        self.cursor.execute(sql)
        ident = self.cursor.fetchall()
        for ide in ident:
            self.con.commit()
            return ide[0]


if __name__ == '__main__':
    e = Escola('192.168.0.4', '5432', 'db_escola', 'fernando', senha)
    endereco = e.cadastroEndereco('Orozimbo correia kriton', '1126', 'nova aurora', '')
    e.cadastroAluno('04664745643', 'Zezinho', 'Boca de Lobo', endereco)
