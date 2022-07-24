class Escritor:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome.upper()

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca) -> None:
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('A caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('A maquina está escrevendo...')


if '__main__' == __name__:
    escritor = Escritor('Pereirinha')
    caneta = Caneta('Compactor')
    maquina = MaquinaDeEscrever()

    print(escritor.nome)
    caneta.escrever()
    maquina.escrever()
    escritor.ferramenta = caneta
    escritor.ferramenta.escrever()
    escritor.ferramenta = maquina
    escritor.ferramenta.escrever()
