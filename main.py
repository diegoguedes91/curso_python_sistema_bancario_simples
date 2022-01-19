from conta import ContaPoupanca, ContaCorrente
from cliente import Cliente
from banco import Banco

banco = Banco()


cliente1 = Cliente('Diego', 30)
cliente2 = Cliente('Alex', 40)
cliente3 = Cliente('Rose', 19)

conta1 = ContaCorrente(1111, 100, 120)
conta2 = ContaPoupanca(3333, 101, 35)
conta3 = ContaCorrente(1164, 120, 100)


cliente1.inserirconta(conta1)
cliente2.inserirconta(conta2)
cliente3.inserirconta(conta3)


banco.inserirCLiente(cliente1)
banco.inserirConta(conta1)

banco.inserirCLiente(cliente2)
banco.inserirConta(conta2)

banco.inserirCLiente(cliente3)
banco.inserirConta(conta3)

if banco.autenticar(cliente1):
    conta1.detalhes()
    conta1.sacar(10)
    conta1.deposito(200)
    conta1.sacar(380)
    print('#' * 80)
else:
    print('Cliente não autenticado')

if banco.autenticar(cliente2):
    conta2.detalhes()
    conta2.sacar(10)
    conta2.sacar(30)
    print('#'*80)
else:
    print('Cliente não autenticado')

if banco.autenticar(cliente3):
    conta3.detalhes()
    conta3.sacar(10)
    print('#' * 80)
else:
    print('Cliente não autenticado')