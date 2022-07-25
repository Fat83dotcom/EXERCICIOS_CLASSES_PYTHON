class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} {self.nome} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} {self.nome} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} {self.nome} está estudando...')


if '__main__' == __name__:

    p1 = Pessoa('Juca', 44)
    c1 = Cliente('Zé', 99)
    c2 = Cliente('Maria', 88)
    a1 = Aluno('Jão', 34)
    a2 = Aluno('Gudulinho', 5)

    p1.falar()
    c1.falar()
    a1.falar()
    c2.comprar()
    a2.estudar()
