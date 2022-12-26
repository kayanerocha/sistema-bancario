from pessoa import Pessoa
from conta_corrente import ContaCorrente

class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.__conta = None
    
    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta
    
    def mostrar_cliente(self):
        print('------- DADOS DO CLIENTE ------')
        super().mostrar_pessoa()
        print(f'Agência: {self.conta.agencia}\nNúmero Conta: {self.conta.numero_conta}\nSaldo: {self.conta.saldo}')
        if isinstance(self.conta, ContaCorrente):
            print(f'Limite: {self.conta.limite}')
        print('-' * 30)

