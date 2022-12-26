from abc import ABC, abstractmethod
from random import randint

class Conta(ABC):
    def __init__(self, agencia, saldo):
        self.__agencia = agencia
        self.__numero_conta = Conta.gerar_numero_conta()
        self.__saldo = saldo
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    
    def depositar(self, valor):
        if valor < 0:
            print('Valor inválido para depósito.')
            return
        self.__saldo += valor
        print(f'R$ {valor:.2f} depositado com sucesso.\nSaldo atual é de R$ {self.saldo:.2f}')
    
    @abstractmethod
    def sacar(self, valor): pass

    @staticmethod
    def gerar_numero_conta():
        i = 0
        numero = ''
        while i < 5:
            numero += str(randint(0, 9))
            i += 1
        return numero
    
    def mostrar_conta(self):
        print('------- DADOS DA CONTA -------')
        print(f'Agência: {self.__agencia}\nNúmero: {self.__numero_conta}\nSaldo: R${self.__saldo:.2f}')