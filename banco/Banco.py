from datetime import datetime


class Cliente:
    def __init__(self) -> None:
        self.nome = None
        self.cpf = None
        self.endereco = Endereco()


class Endereco:
    def __init__(self) -> None:
        self.rua = None
        self.numero = None
        self.bairro = None
        self.cidade = None
        self.estado = None


class Conta:
    # definição da classe

    def __init__(self, numero, saldo, limite) -> None:
        self.titular = Cliente()
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.extrato = Extrato(self.numero)

    # metodos da classe
    def idCliente(self, nome, cpf):
        self.titular.nome = nome
        self.titular.cpf = cpf

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['DEPOSITO', valor, 'DATA', datetime.today(), 'SALDO', self.saldo])

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insificiente R${self.saldo}')
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor, 'DATA', datetime.today(), 'SALDO', self.saldo])

    def transferir(self, contadestino, valor):
        if self.saldo < valor:
            print(f'Saldo insificiente. R${self.saldo}')
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['TRANSFERENCIA', valor, 'DATA', datetime.today(), 'SALDO', self.saldo])
            print('Transferencia realizada com sucesso')

    def mostrarSaldo(self):
        print(f'O saldo do cliente {self.titular.nome} é {self.saldo} ')


class Extrato:
    def __init__(self, conta) -> None:
        self.transacoes = []
        self.nConta = conta

    def extrato(self):
        print(f'Extrato: {self.nConta}')

        for item in self.transacoes:
            print(f"{item[0]}: {item[1]}, {item[2]}: {item[3].strftime('%d/%b/%y')}, {item[4]}: {item[5]}")


if __name__ == '__main__':
    c1 = Conta(1, 0, 1000)
    c2 = Conta(2, 0, 2000)
    c1.idCliente('Fernando Mendes', '929292992')
    c2.idCliente('Maria', '93939393')
    c1.depositar(3000)
    c1.transferir(c2, 1000)
    c1.sacar(432)
    c1.mostrarSaldo()
    c1.extrato.extrato()
    c2.extrato.extrato()
