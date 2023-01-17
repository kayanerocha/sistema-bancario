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
menu_inicial = Menu('SISTEMA BANCÁRIO', ['Sair', 'Cadastrar Banco', 'Listar Bancos'])
while True:
    menu_inicial.imprimir_menu()
    opcao = menu_inicial.solicitar_resposta()
    if opcao == 1:
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
    elif opcao == 2:
        lista_menu_bancos = []
        for banco in sistema_bancario.bancos:
            lista_menu_bancos.append(banco.nome)     
        lista_menu_bancos.append('Voltar')
        lista_menu_bancos.append('Sair')
        menu_bancos = Menu('LISTA DE BANCOS', lista_menu_bancos)

        while True:
            menu_bancos.imprimir_menu()
            opcao_banco = menu_bancos.solicitar_resposta()

            if opcao_banco >= len(lista_menu_bancos):
                print('Informe uma opção válida.')
            elif opcao_banco == len(lista_menu_bancos) - 2:
                break
            elif opcao_banco == len(lista_menu_bancos) - 1:
                exit()
            else:
                banco_escolhido = sistema_bancario.bancos[opcao_banco]
                opcoes_menu_banco = ['Cadastrar Cliente', 'Listar Clientes', 'Detalhes', 'Voltar', 'Sair']
                menu_banco = Menu(banco_escolhido.nome, opcoes_menu_banco)
                
                while True:
                    menu_banco.imprimir_menu()
                    opcao_interna = menu_banco.solicitar_resposta()
                    
                    if opcao_interna >= len(opcoes_menu_banco):
                        print('Informe uma opção válida.')
                    elif opcao_interna == len(opcoes_menu_banco) - 2:
                        break
                    elif opcao_interna == len(opcoes_menu_banco) - 1:
                        exit()
                    elif opcao_interna == 0:
                        nome_cliente = str(input('Nome do cliente: '))
                        while True:
                            try:
                                cpf = int(input('CPF do cliente: '))
                                if not Cliente.valida_cpf(cpf):
                                    continue
                            except ValueError:
                                print('Informe apenas números.')
                            else:
                                while True:
                                    tipo_conta = str(input('Tipo de conta [CP/CC]: '))
                                    if not banco_escolhido.inserir_cliente(nome_cliente, cpf, tipo_conta):                                       
                                        continue
                                    break
                                break
                    elif opcao_interna == 1:
                        banco_escolhido.listar_clientes()
                    else:
                        banco_escolhido.imprimir_detalhes()
            
    elif opcao == 0:
        break
