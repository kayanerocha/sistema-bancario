from cliente import Cliente
from conta import Conta
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from banco import Banco
from menu import Menu

bb = Banco('Banco do Brasil', '001')
# bb.inserir_cliente('Kayane', '20', 'cp', 0)

caixa = Banco('Caixa Econômica Federal', '104')
# caixa.inserir_cliente('Thayssa', '18', 'cc', 0)


# numero_conta = str(input('Número conta: '))
# bb.sacar('18', '104', numero_conta, 10)
# caixa.sacar('18', '104', numero_conta, 10)
# caixa.depositar('18', '104', numero_conta, 10)

# Criar menus
    # Cadastrar Banco
        # Pede as informações de banco
    # Listar Bancos
        # Ver informações de um banco
            # Cadastrar Cliente
                # Pede as informações de cliente
            # Listar Clientes
                # Ver informações de um cliente
                    # Depositar
                    # Sacar  

menu_inicial = Menu('SISTEMA BANCÁRIO', ['Cadastrar Banco', 'Listar Bancos', 'Sair'])
menu_inicial.imprimir_menu()
opcao = menu_inicial.solicitar_resposta()
