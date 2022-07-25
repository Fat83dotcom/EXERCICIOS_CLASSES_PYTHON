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


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome) -> None:
        super().__init__(nome, idade)  # ou Cliente.__init__(self, nome, idade)
        self.sobrenome = sobrenome
