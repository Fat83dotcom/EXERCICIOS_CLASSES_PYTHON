from banco.cliente import Cliente
from banco.conta import Conta


cli1 = Cliente('Fernando Mendes', '1234567895', 'ruas das capivara 666')
cli2 = Cliente('Maria da rosa', '987548575', 'rua das aboboras amassadas 345')

c1 = Conta(cli1, '345f65', 0, 1000)
c2 = Conta(cli2, '212l394', 0, 9000)


c1.depositar(600)
c1.extrato()
c1.sacar(800)
c1.extrato()
c1.transferir(c2, 200)
c2.extrato()
c1.extrato()
