'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo,
 que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto
 que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''


class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def pontoMedioX(self):
        mX = self.x / 2
        return mX

    def pontoMedioY(self):
        mY = self.y / 2
        return mY


class Retangulo:
    def __init__(self, largura, altura) -> None:
        self.ponto = Ponto(largura, altura)
        self.largura = self.ponto.x
        self.altura = self.ponto.y

    def centroRetangulo(self):
        cR = (self.ponto.pontoMedioX(), self.ponto.pontoMedioY())
        return cR

    def imprimePontos(self):
        print(f'X = {self.largura}, Y = {self.altura}')


if __name__ == '__main__':
    r = Retangulo(255, 4)
    r.imprimePontos()
    print(r.centroRetangulo())
