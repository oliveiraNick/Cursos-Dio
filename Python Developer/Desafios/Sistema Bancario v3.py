from abc import *


class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

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

