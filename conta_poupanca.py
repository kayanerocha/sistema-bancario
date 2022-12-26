from conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficente para saque.')
            return
        self.saldo -= valor
        print(f'Você sacou R$ {valor:.2f}. Seu saldo atual é R$ {self.saldo:.2f}')

