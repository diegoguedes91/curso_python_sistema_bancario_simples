# Curso de Python 3 do Básico ao Avançado 
#### Desafio: Sistema Bancario simples 

Exercício com Abstração, Herança, Encapsulamento e Polimorfismo. 

Criar um sistema bancáro (extremamente simples) que tem clientes, contas e um banco. </br>A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas. 

### Dicas: 
1. Criar classe Cliente que herda da classe pessoa (Herança)
    * Pessoa tem nome e idade (com getters)
    * Cliente tem conta (Agregação da classe ContaCorrente ou ContaPoupança)

### Algoritmo:  
```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserirconta(self, conta):
        self.conta = conta
```

2. Criar classes Conta Poupança e ContaCorrente que herdam de Conta
    * ContaCorrente deve  ter um limite extra
    * Contas têm agência, número da conta e saldo 
    * Contas devem ter método para depósito 
    * Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo - as subclasses que implementam o método sacar) 

### Algoritmo:
```python 
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def detalhes(self):
        print(f'Agencia: {self.agencia} '
              f'Conta: {self.conta} '
              f'saldo: R$ {self.saldo:.2f}')

    def deposito(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente para sacar')
            return
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self,valor):
        if valor > (self.saldo + self.limite):
            print('Saldo insuficiente para sacar')
        else:
            self.saldo -= valor
            self.detalhes()
```

3. Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação) 
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    * Banco tem contas e clientes (Agregação)
	    * Checar se a agência é daquele banco 
	    * Checar se o cliente é daquele banco 
	    * Checar se a conta é daquele banco 
Só será possível sacar se passar na autenticação do banco (descrita acima) 

### Algoritmo:
```python
class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.contas = []
        self.clientes = []

    def inserirCLiente(self, cliente):
        self.clientes.append(cliente)

    def inserirConta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
```

## Testes: 

No teste abaixo, foi inserido 3 clientes e contas. O primeiro cliente tem conta corrente, o segundo conta poupança e o terceiro não deve passar na autenticação do banco, pois a agencia é inválida. 

```python
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
```

Conforme o algoritmo acima, se o cliente passar na autenticação do Banco podera realizar auterações no saldo da conta

### Cliente1:

Cliente1 passou na autencação, fez um saque de 10, deposito de 200 e outro saque de 380 ficando com um saldo negativo, pois como o cliente1 tem uma conta corrente, ele tem um limite de 100 alem do saldo.

![imagem do terminal cliente 1](https://github.com/diegoguedes91/curso_python_sistema_bancario_simples/blob/main/teste_cliente1)

### Cliente2:

Cliente2 passou na autenticação, fez um saque de 10 e tentou fazer um outro saque de 30, porém diferente do cliente1, o cliente2 possui uma conta poupança, não tendo limite além do saldo, gerando uma mensagem e não podendo sacar.  

![imagem do terminal cliente 2](https://github.com/diegoguedes91/curso_python_sistema_bancario_simples/blob/main/teste_cliente2)

### Cliente3: 

O cliente3 não passou na autenticação, pois conforme o algoritmo da classe Banco, as agencias registradas são 1111, 2222, 3333. O cliente3 registrou a agencia 1164 gerando erro de autenticação.

![imagem do terminal cliente 3](https://github.com/diegoguedes91/curso_python_sistema_bancario_simples/blob/main/teste_cliente3)


