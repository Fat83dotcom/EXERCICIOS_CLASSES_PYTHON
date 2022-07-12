class Aluno:
    def __init__(self, nome) -> None:
        self.__nome = nome


aluno = Aluno('Fernando')

print(aluno.__nome)
