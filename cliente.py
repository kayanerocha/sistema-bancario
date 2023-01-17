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
    
    def cadastrar_cliente(self):
        try:
            self.nome = str(input('Nome do cliente: '))
        except ValueError:
            print('Informe um nome válido: ')
        else:
            print('Deu certo')
            self.cpf = str(input('Informe o CPF do cliente com apenas números: '))
    
    def mostrar_cliente(self):
        print('------- DADOS DO CLIENTE ------')
        super().mostrar_pessoa()
        print(f'Agência: {self.conta.agencia}\nNúmero Conta: {self.conta.numero_conta}\nSaldo: {self.conta.saldo}')
        if isinstance(self.conta, ContaCorrente):
            print(f'Limite: {self.conta.limite}')
        print('-' * 30)
    
    @staticmethod
    def valida_cpf(cpf):
        # Insere o CPF em uma lista
        lista_cpf = []
        for n in str(cpf):
            lista_cpf.append(n)
        if len(lista_cpf) < 11 or len(lista_cpf) > 11:
            print('CPF inválido.')
            return False
        
        # Primeira multiplicação com os primeiros 9 digitos
        multiplicacao = Cliente.multiplica_digitos(10, lista_cpf)

        # Validação do primeiro dígito depois do -
        primeiro_resto = (multiplicacao * 10) % 11
        primeiro_resto = 0 if primeiro_resto == 10 else primeiro_resto
        if primeiro_resto == int(lista_cpf[9]):            
            # Segunda multiplicação com os primeiros 10 digitos
            multiplicacao = Cliente.multiplica_digitos(11, lista_cpf)
            segundo_resto = (multiplicacao * 10) % 11
            if segundo_resto == int(lista_cpf[10]):                
                return True
            print('CPF inválido.')
            return False
        else:
            print('CPF inválido.')
            return False
        
        # for i in range(10, 1, -1):
        #     print(i)
    
    @staticmethod
    def multiplica_digitos(limite, cpf):
        i = limite
        j = 0
        multiplicacao = 0
        while i >= 2:
            n = int(cpf[j])
            multiplicacao += i * n
            i -= 1
            j += 1
        
        return multiplicacao

