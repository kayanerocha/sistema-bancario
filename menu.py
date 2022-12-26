class Menu:
    def __init__(self, titulo, opcoes):
        self.__titulo = titulo
        self.__opcoes = opcoes
        self.__resposta = None
    
    @property
    def opcoes(self):
        return self.__opcoes
    
    def imprimir_menu(self):
        print(f'{self.__titulo:^30} ')
        print('-' * 30)
        print('Escolha uma opção:')
        
        for posicao, opcao in enumerate(self.__opcoes):
            print(f'{posicao} - {opcao}')
    
    def solicitar_resposta(self):
        while True:
            opcao = int(input('Opção: '))
            if Menu.is_inteiro(opcao) and opcao >= 0 and opcao < len(self.opcoes):
                self.__resposta = opcao
                break
        return self.__resposta
    
    @staticmethod
    def is_inteiro(numero):
        if isinstance(numero, int):
            return True

        
    