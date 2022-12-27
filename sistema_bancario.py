class SistemaBancario:
    def __init__(self) -> None:
        self.__bancos = []
    
    @property
    def bancos(self):
        # nomes = []
        # for banco in self.__bancos:
        #     nomes.append(banco.nome)
        # return nomes
        return self.__bancos
    
    def adiciona_banco(self, banco):
        self.__bancos.append(banco)