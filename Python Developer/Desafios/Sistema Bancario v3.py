from abc import *


class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico


    #configurando o @classmethod e o acesso aos atributos privados da conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls (numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico


    #Configurando as funções de saque e depósito da conta
    def saque(self, valor:float):
        excedeu_saldo = valor > self.saldo

        if excedeu_saldo:
            print("\033[31mSaldo insuficiente! Tente outro valor ou adicione dinheiro a sua conta.\033[m")
        
        elif valor > 0:
            self._saldo -= valor
            print(f"\033[32mValor \033[4mR${valor:.2f}\033[m\033[32m retirado com sucesso!\033[m")

            return True

        else:
            print("\033[31mValor inválido, tente novamente!\033[m")
        
        return False

    def deposito(self, ):
        ...


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        Transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class ContaCorrente(Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente, historico, limite, limite_saque):
        super().__init__(saldo, numero, agencia, cliente, historico)

        self._limite: limite
        self._limite_saque: limite_saque
    

class Historico:
    ...


class Transacao(ABC):
    def registrar(self, conta):
        ...


class Saque(Transacao):
    ...


class Deposito(Transacao):
    ...


class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, cpf, data_nascimento):
        super().__init__(endereco)

        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

