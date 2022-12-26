class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    def mostrar_pessoa(self):
        print(f'Nome: {self.__nome}\nCPF: {self.__cpf}')