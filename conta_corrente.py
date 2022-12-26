from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, saldo, limite=1000):
        super().__init__(agencia, saldo)
        self.__limite = limite
    
    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if valor > self.saldo + self.__limite:
            print('Saldo insuficente para saque.')
            return
        self.saldo -= valor
        self.__limite -= abs(self.saldo)
        print(f'Você sacou R$ {valor:.2f}. Seu saldo atual é R$ {self.saldo:.2f} e o limite é de {self.__limite}')
    
    def mostrar_conta(self):
        super().mostrar_conta()
        print(f'Limite: R${self.__limite:.2f}')