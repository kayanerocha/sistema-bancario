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
    
    def mostrar_cliente(self):
        print('------- DADOS DO CLIENTE ------')
        super().mostrar_pessoa()
        print(f'Agência: {self.conta.agencia}\nNúmero Conta: {self.conta.numero_conta}\nSaldo: {self.conta.saldo}')
        if isinstance(self.conta, ContaCorrente):
            print(f'Limite: {self.conta.limite}')
        print('-' * 30)
    
    def valida_cpf(self):
        # Insere o CPF em uma lista
        cpf = []
        for n in str(self.cpf):
            cpf.append(n)
        
        # Primeira multiplicação com os primeiros 9 digitos
        i = 10
        j = 0
        multiplicacao = 0
        while i >= 2:
            n = int(cpf[j])
            multiplicacao += i * n
            print(f'{i} * {n} = {i * n}')
            i -= 1
            j += 1
        print(f'Total: {multiplicacao}')

        # Validação do primeiro dígito depois do -
        primeiro_resto = (multiplicacao * 10) % 11
        primeiro_resto = 0 if primeiro_resto == 10 else primeiro_resto
        if primeiro_resto == int(cpf[9]):
            print('Passou na primeira validação.')

        else:
            print('Não passou na validação')
        
        # for i in range(10, 1, -1):
        #     print(i)
    
    

