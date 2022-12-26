from banco import Banco
from time import sleep

class Menu:
    def __init__(self, titulo, opcoes):
        self.__titulo = titulo
        self.__opcoes = opcoes
        self.__resposta = None
    
    @property
    def opcoes(self):
        return self.__opcoes
    
    def imprimir_menu(self):
        sleep(1)
        print('-' * 30)
        print(f'{self.__titulo:^30} ')
        print('-' * 30)
        print('Escolha uma opção:')
        
        for posicao, opcao in enumerate(self.__opcoes):
            print(f'{posicao} - {opcao}')
    
    def solicitar_resposta(self):
        while True:
            try:
                opcao = int(input('Opção: '))
                print('-' * 30)
            except ValueError:
                print('Informe uma opção válida.')
                continue
            else:
                if opcao < 0 or opcao >= len(self.opcoes):
                    print('Informe uma opção válida.')
                else:
                    return opcao
    
    @staticmethod
    def is_inteiro(numero):
        if isinstance(numero, int):
            return True

        
    