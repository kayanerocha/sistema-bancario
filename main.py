from cliente import Cliente
from conta import Conta
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from banco import Banco
from menu import Menu
from sistema_bancario import SistemaBancario

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

sistema_bancario = SistemaBancario()
menu_inicial = Menu('SISTEMA BANCÁRIO', ['Cadastrar Banco', 'Listar Bancos', 'Sair'])
while True:
    menu_inicial.imprimir_menu()
    opcao = menu_inicial.solicitar_resposta()
    if opcao == 0:
        nome_banco = str(input('Nome do banco: '))
        while True:
            try:
                agencia = int(input('Agência do banco: '))
            except ValueError:
                print(f'Informe uma agência válida.')
            else:
                banco = Banco(nome_banco, agencia)
                sistema_bancario.adiciona_banco(banco)
                print('Banco criado com sucesso!')
                break
    elif opcao == 1:
        menu_bancos = Menu('LISTA DE BANCOS', sistema_bancario.bancos)
        menu_bancos.imprimir_menu()
    elif opcao == 2:
        break
