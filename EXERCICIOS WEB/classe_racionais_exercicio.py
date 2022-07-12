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
    def __init__(self, numerador, denominador) -> None:
        self.numerador = numerador
        self.denominador = denominador

    @property
    def denominador(self):
        return self._denominador

    @denominador.setter
    def denominador(self, valor):
        if valor == 0:
            self._denominador = 'Denominador Não pode ser zero.'
        else:
            self._denominador = valor

    def inverterSinal(self):
        self.numerador = -self.numerador

    def somaRacional(self, num, den):
        r = Racional(num, den)
        denominador_mmc = self.denominador * r.denominador
        numerador_soma = (r.denominador * self.numerador) + (self.denominador * r.numerador)
        print(f'A soma entre {self.numerador}/{self.denominador} e {r.numerador}/{r.denominador} é {numerador_soma}/{denominador_mmc}')

    def subtracaoRacional(self, num, den):
        r = Racional(num, den)
        denominador_mmc = self.denominador * r.denominador
        numerador_sub = (r.denominador * self.numerador) - (self.denominador * r.numerador)
        print(f'A subtração entre {self.numerador}/{self.denominador} e {r.numerador}/{r.denominador} é {numerador_sub}/{denominador_mmc}')

    def produtoRacional(self, num, den):
        r = Racional(num, den)
        numerador = self.numerador * r.numerador
        denominador = self.denominador * r.denominador
        print(f'O produto entre {self.numerador}/{self.denominador} e {r.numerador}/{r.denominador} é {numerador}/{denominador}')

    def quocienteRacional(self, num, den):
        r = Racional(num, den)
        numerador = self.numerador * r.denominador
        denominador = self.denominador * r.numerador
        print(f'O quociente entre {self.numerador}/{self.denominador} e {r.numerador}/{r.denominador} é {numerador}/{denominador}')


if __name__ == '__main__':
    r = Racional(4, 2)
    print(r.denominador)
    # print(r.inverterSinal())
    print(r.numerador)
    r.somaRacional(6, -3)
    r.subtracaoRacional(9, -5)
    r.produtoRacional(3, 9)
    r.quocienteRacional(5, 8)
