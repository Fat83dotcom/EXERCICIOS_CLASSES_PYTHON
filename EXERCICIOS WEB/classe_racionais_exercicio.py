'''
Um racional e qualquer numero da forma p/q, sendo p inteiro e q inteiro nao nulo. Crie
uma classe para representar um racional e os seguinte metodos:
1
(a) inverter sinal;
(b) somar dois racionais;
(c) subtrair dois racionais;
(d) produto de dois racionais;
(e) quociente de dois racionais;
'''


class Racional:
    def __init__(self) -> None:
        self.__numerador = None
        self.__denominador = None

    def entrarNumeros(self, numerador, denominador):
        self.denominador = denominador
        self.__numerador = numerador

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, valor):
        if valor == 0:
            self.__denominador = None
        else:
            self.__denominador = valor

    @property
    def numerador(self):
        return self.__numerador

    def inverterSinal(self):
        self.__numerador = -self.__numerador

    def somaRacional(self, num, den):
        self.entrarNumeros(num, den)
        try:
            denominador_mmc = self.__denominador * self.__denominador
            numerador_soma = (self.__denominador * self.__numerador) + (self.__denominador * self.__numerador)
            print(f'A soma entre {self.__numerador}/{self.__denominador} e'
                  f' {self.__numerador}/{self.__denominador} é {numerador_soma}/{denominador_mmc}')
        except TypeError as erro:
            print(f'Não há divisão por zero ou letras, erro levantado: {erro} ')

    def subtracaoRacional(self, num, den):
        self.entrarNumeros(num, den)
        try:
            denominador_mmc = self.__denominador * self.__denominador
            numerador_sub = (self.__denominador * self.__numerador) - (self.__denominador * self.__numerador)
            print(f'A subtração entre {self.__numerador}/{self.__denominador} e'
                  f' {self.__numerador}/{self.__denominador} é {numerador_sub}/{denominador_mmc}')
        except TypeError as erro:
            print(f'Não há divisão por zero ou letras, erro levantado: {erro} ')

    def produtoRacional(self, num, den):
        self.entrarNumeros(num, den)
        try:
            numerador = self.__numerador * self.__numerador
            denominador = self.__denominador * self.__denominador
            print(f'O produto entre {self.__numerador}/{self.__denominador} e'
                  f' {self.__numerador}/{self.__denominador} é {numerador}/{denominador}')
        except TypeError as erro:
            print(f'Não há divisão por zero ou letras, erro levantado: {erro} ')

    def quocienteRacional(self, num, den):
        self.entrarNumeros(num, den)
        try:
            numerador = self.__numerador * self.__denominador
            denominador = self.__denominador * self.__numerador
            print(f'O quociente entre {self.__numerador}/{self.__denominador} e'
                  f' {self.__numerador}/{self.__denominador} é {numerador}/{denominador}')
        except TypeError as erro:
            print(f'Não há divisão por zero ou letras, erro levantado: {erro} ')


if __name__ == '__main__':
    r = Racional()
    p = Racional()
    r.entrarNumeros(3, 4)
    print(r.denominador)
    # print(r.inverterSinal())
    print(r.numerador)
    p.somaRacional(3, 4)
    p.subtracaoRacional(9, 5)
    p.produtoRacional(3, 9)
    p.quocienteRacional(5, 8)
