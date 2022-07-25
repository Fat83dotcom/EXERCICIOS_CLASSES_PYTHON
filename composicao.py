class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = []  # type: ignore

    def insereEndereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def listaEndereco(self):
        for end in self.endereco:
            print(end.cidade, end.estado)


class Endereco:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado


if '__main__' == __name__:

    c1 = Cliente('Fernando', 39)
    c1.insereEndereco('caldas novas', 'GO')

    c1.listaEndereco()
