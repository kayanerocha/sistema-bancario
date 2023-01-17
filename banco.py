from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

class Banco:
    def __init__(self, nome, agencia):
        self.__nome = nome
        self.__agencia = agencia
        self.__clientes = []
        self.__contas = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def contas(self):
        return self.__contas
    
    def inserir_cliente(self, nome, cpf, tipo_conta, saldo=0):
        if Banco.valida_conta(tipo_conta):
            cliente = Cliente(nome, cpf)
            cliente.conta = self.inserir_conta(tipo_conta, saldo)
            self.__clientes.append(cliente)
            print('Cliente cadastrado com sucesso!')
            cliente.mostrar_cliente()
            return True
        return False
    
    def listar_clientes(self):
        for cliente in self.__clientes:
            cliente.mostrar_cliente()
    
    def inserir_conta(self, tipo_conta, saldo):
        if tipo_conta.upper() in 'CP':
            conta = ContaPoupanca(self.agencia, saldo)
        elif tipo_conta.upper() in 'CC':
            conta = ContaCorrente(self.agencia, saldo)
        else:
            print('Tipo de conta inválida.')
            return

        self.__contas.append(conta)
        return conta
    
    def listar_contas(self):
        for cliente in self.__clientes:
            cliente.conta.mostrar_conta()
    
    def autenticar_cliente(self, cpf, agencia, numero_conta):
        for c in self.__clientes:
            if cpf.upper() == c.cpf.upper() and agencia == c.conta.agencia and numero_conta == c.conta.numero_conta:
                print('Cliente autenticado com sucesso.')
                return c
        print('Cliente não autenticado.')
        return False
    
    def sacar(self, cpf, agencia, numero_conta, valor):
        cliente = self.autenticar_cliente(cpf, agencia, numero_conta)
        if isinstance(cliente, Cliente):
            cliente.conta.sacar(valor)

    
    def depositar(self, cpf, agencia, numero_conta, valor):
        cliente = self.autenticar_cliente(cpf, agencia, numero_conta)
        if isinstance(cliente, Cliente):
            cliente.conta.depositar(valor)
    
    @staticmethod
    def valida_conta(tipo_conta):
        if tipo_conta.upper() not in ['CP', 'CC']:
            return False
        return True