class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []  # type: ignore

    def inserirProdutos(self, produto):
        self.produtos.append(produto)

    def listaProdutos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somaTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = valor


if '__main__' == __name__:
    pass
