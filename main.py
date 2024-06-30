# Importações importantes
from data import * # Dados do código
from views import * # Ferramentas de interface
from tools import * # Ferramentas para tratamento de entrada de dados
# Modularização de pastas 
from compras import * 
from almoxarifado import * 
from vendas import *
from clientes import *
from funcionarios import *
from relatorios import *
from menu import *

####################################
###         VERSÃO 14            ###
####################################

resp = ""

while resp != "0":
    limpar_tela()
    cabecalho("Hamburgueria do Py")
    principal()

    resp = input_tratado("Operação: ")

    if resp == "C" or resp == "1":
        limpar_tela()
        op_compra = ""

        while op_compra != "0":
            limpar_tela()
            titulo("Compras")
            print("↪︎ 1.  Cadastrar Mercadorias")
            print("↪︎ 0.  Menu principal")
            linha()
            op_compra = input_tratado("Operação:    ")

            if op_compra == "C" or op_compra == "1":
                cadastrar_compras()

            elif op_compra == "M" or op_compra == "0":
                break

    elif resp == "A" or resp == "2":
        limpar_tela()
        quadro_almoxarifado(almoxarifado)
        op_almoxarifado = ""

        while op_almoxarifado != "0":
            linha()
            print("↪︎ 1.  Buscar item")
            print("↪︎ 2.  Excluir item")
            print("↪︎ 0.  Menu principal")
            linha()
            op_almoxarifado = input_tratado("Operação:  ")

            if op_almoxarifado == "B" or op_almoxarifado == "1":
                buscar_item()
            
            elif op_almoxarifado == "E" or op_almoxarifado == "2":
                excluir_item()

            elif op_almoxarifado == "M" or op_almoxarifado == "0":
                break
 
    elif resp == "V" or resp == "3":
        limpar_tela()
        op_vender = ""

        while op_vender != "0":
            limpar_tela()
            titulo("Vendas")
            print("↪︎ 1.  Ver Cardápio")
            print("↪︎ 2.  Administrar Cardápio")
            print("↪︎ 3.  Vendas")
            print("↪︎ 0.  Menu Principal")
            linha()

            op_vender = input_tratado("Operação:    ")
            if op_vender == "C" or op_vender == "1":
                exibir_cardapio()

            elif op_vender == "A" or op_vender == "2":
                limpar_tela()
                op_admi_cardapio = ""

                while op_admi_cardapio != "0":
                    limpar_tela()
                    titulo("Administrar Cardápio")
                    print("↪︎ 1.  Atualizar Cardápio")
                    print("↪︎ 2.  Excluir Hambúrguer")
                    print("↪︎ 0.  Vendas")

                    op_admi_cardapio = input_tratado("Operação: ")

                    if op_admi_cardapio == "A" or op_admi_cardapio == "1":
                        hamburguer = verificar_hamburguer_existente()
                        
                        if hamburguer:
                            atualizar_hamburguer(hamburguer)

                        else:
                            confirmar = input_tratado("Deseja cria-lo?[S/N]: ")

                            if confirmar[0] in 'S':
                                criar_novo_hamburguer(hamburguer)
                            
                            else:
                                break

                    elif op_admi_cardapio == "E" or op_admi_cardapio == "2":
                        excluir_hamburguer()

                    elif op_admi_cardapio == "0":
                        break
            
            elif op_vender == "V" or op_vender == "3":
                    limpar_tela()
                    op_fazer_venda = ""

                    while op_fazer_venda != "0":
                        limpar_tela()
                        titulo("Vendas")
                        print("↪︎ 1.  Vender Hambúruguer")
                        print("↪︎ 2.  Lista de Pedidos")
                        print("↪︎ 3.  Fechar vendas")
                        print("↪︎ 0.  Vendas")

                        op_fazer_venda = input_tratado("Operação:   ")

                        if op_fazer_venda == "V" or op_fazer_venda == "1":
                            criar_pedido()

                        elif op_fazer_venda == "L" or op_fazer_venda == "2":
                            listar_pedidos()
                            op_finalizar = ''

                            while op_finalizar != "0":
                                print("↪︎ 1.  Confirmar Pedido")
                                print("↪︎ 2.  Remover Pedido")
                                print("↪︎ 3.  Editar Pedido")
                                print("↪︎ 0.  Retornar")
                                op_finalizar = input_tratado("Operação: ")
                                
                                if op_finalizar == '1' or op_finalizar[0] in 'C':
                                    limpar_tela()
                                    titulo("Processamento de Pedidos")
                                    finalizar_pedido = leia_int("N° do Pedido: ")
                                    
                                    if finalizar_pedido == '0':
                                        break

                                    decrementar_ingredientes(finalizar_pedido)
                                    sucess_msg("Pedido realizado com sucesso!")
                                    input(">> Enter")

                                elif op_finalizar == '2' or op_finalizar[0] in 'R':
                                    limpar_tela()
                                    titulo("Remoção de pedidos")
                                    excluir_pedido = leia_int("N° do Pedido: ")

                                    if excluir_item == '0':
                                        break

                                    delete = input_tratado("Pedido já foi confirmado (S/N): ")

                                    if delete[0] == 'S':
                                        if incrementar_ingredientes(excluir_pedido):
                                            sucess_msg("Pedido removido com sucesso!")
                                    else:
                                        if delete(excluir_pedido):
                                            sucess_msg("Pedido removido com sucesso!")
                                   
                                    input(">> Enter")

                                elif op_finalizar == '3' or op_finalizar[0] in 'E':
                                    titulo("Edição de pedidos")
                                    pedido_cliente = leia_int("N° do Pedido: ")

                                    if editar_pedido == '0':
                                        break

                                    editar_pedido(pedido_cliente)

                                    input(">> Enter")
                        
                        elif op_fazer_venda == "F" or op_fazer_venda == "3":
                            fechar_vendas()

                        elif op_vender == "0":
                                    break

    elif resp == 'F' or resp == '4':
        op_funcionarios = ''

        while op_funcionarios != '0':
            operacoes_funcionarios()
            op_funcionarios = input_tratado("Operação:  ")

            if op_funcionarios[0] in "1Q":
                limpar_tela()
                titulo("Quadro de funcionários")

                for cpf, dados in funcionarios.items():
                  nome = funcionarios[cpf]['Nome']
                  idade = funcionarios[cpf]['Idade']
                  quadro(cpf, nome, idade)        

                input(">> Enter")

            elif op_funcionarios[0] in "2G":
              chave_acesso = True

              if chave_acesso == True:
                limpar_tela()

                op_gerenciar = ''
                while op_gerenciar != '0':
                    limpar_tela()
                    titulo("Administrativo")
                    print("↪︎ 1.  Contratar funcionários      ")
                    print("↪︎ 2.  Demitir funcionários      ")
                    print("↪︎ 3.  Buscar funcionário     ")
                    print("↪︎ 4.  Editar funcionário     ")
                    print("↪︎ 0. Menu Principal") 
                    linha()
                    op_gerenciar = input_tratado("Operação: ")

                    if op_gerenciar == '1':
                        contratar()

                    elif op_gerenciar == '2':
                        demitir()

                    elif op_gerenciar == '3':
                        buscar()
                    
                    elif op_gerenciar == '4':

                        if editar_funcionario():
                            sucess_msg(f"{funcionarios[cpf]['Nome']} foi editado com sucesso!")
                            input(">> Enter")

                        else:
                            error_msg(f"Não cadastrado")
                            input(">> Enter")

                    elif op_gerenciar == '0':
                        break

            elif op_funcionarios[0] in '0S':
              break

    elif resp == "CL" or resp == "5":
        limpar_tela()
        op_cliente = ""

        while op_cliente != "0":
            operacoes_clientes()
            
            op_cliente = input_tratado("Operação:   ")

            if op_cliente[0] in "1C":
                cadastrar_cliente()

            elif op_cliente[0] in "2L":
                quadro_clientes()

            elif op_cliente[0] in "3E":
                quadro_clientes()
                editar_clientes()

            elif op_cliente[0] in "0S":
                break

    elif resp[0] in "R" or resp == '6':
        limpar_tela()
        op_relatorio = ""

        while op_relatorio != "0":
            limpar_tela()
            titulo("Relatórios")
            print("1 ↪︎ Relatório de Compras")  
            print("2 ↪︎ Relatório de Vendas")
            print("3 ↪︎ Relatório de mais vendidos")  
            print("0 ↪︎ Menu Principal") 

            op_relatorio = input_tratado("Operação:   ")

            if op_relatorio[0] in "1C":
                processo_compras()

            elif op_relatorio[0] in "2V":
                processos_vendas()
            
            elif op_relatorio == "3":
                imprimir_ranking()

            elif op_relatorio[0] in "0S":
              break
            
    elif resp == "INF" or resp == '7':
            limpar_tela()
            titulo("Informações")
            subtitulo("Projeto de Gestão de uma Hamburgueria")
            print("-○  Equipe de desenvolvimento:               ")
            print("-○  Anderson G. Pereira Cruz                 ")
            print("-○  Replit: @gabrielcruz133                  ")
            print("-○  Instagram: biel.ands                     ")
            print("-○  andersong.pereiracruz@gmail.com          ")
            print("-○  59-378/000 São José do Serído - RN       ")
            linha()
            input("<<ENTER>> para continuar")

    elif resp[0] in "S" or resp == '0':
        break

limpar_tela()
cabecalho("Hamburgueria do Py")
cabecalho("Até mais")