class Aluno:
    def __init__(self, nome) -> None:
        self.__nome = nome

    def mostraNome(self):
        print(self.__nome)


aluno = Aluno('Fernando')

aluno.mostraNome()

# print(aluno.__nome)
