class Conta:
    # definição da classe

    def __init__(self, titular, numero, saldo, limite) -> None:
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    # metodos da classe

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insificiente R${self.saldo}')
        else:
            self.saldo -= valor

    def extrato(self):
        print(f'A conta {self.numero}, do titular {self.titular.nome}, possui um saldo de R${self.saldo}.')

    def transferir(self, contadestino, valor):
        if self.saldo < valor:
            print(f'Saldo insificiente. R${self.saldo}')
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            print('Transferencia realizada com sucesso')


if __name__ == '__main__':
    pass
