####################################
###         VERSÃO 16            ###
####################################


# Importações necessárias para main.
from almoxarifado_pct import buscar_item, excluir_item
from clientes_pct import cadastrar_cliente, quadro_clientes, editar_clientes, excluir_cliente
from compras_pct import cadastrar_compras
from dados_pct import almoxarifado, funcionarios
from funcionarios_pct import contratar, demitir, buscar, editar_funcionario
from cardapio_pct import (
    exibir_cardapio, verificar_hamburguer_existente, 
    atualizar_hamburguer, criar_hamburguer, excluir_hamburguer
)
from relatorios_pct import processo_compras, processos_vendas, imprimir_ranking
from ferramentas_pct import varredura, limpar_tela, input_tratado
from vendas_pct import *
from estilização_pct import (
    cabecalho, titulo, principal, linha, quadro_almoxarifado, 
    sucess_msg, error_msg, operacoes_clientes, 
    operacoes_funcionarios, quadro, subtitulo
)


#   Código principal
resp = ""
varredura()


while resp != "0":
    limpar_tela()
    cabecalho("Hamburgueria do Py")
    principal()

    resp = input_tratado("Operação: ")

    match resp:
        case "1" | "C":
            limpar_tela()
            op_compra = ""

            while op_compra != "0":
                limpar_tela()
                titulo("Compras")
                print("↪︎ 1.  Cadastrar Mercadorias")
                print("↪︎ 0.  Menu principal")
                linha()
                op_compra = input_tratado("Operação:    ")

                match op_compra:
                    case "1":
                        cadastrar_compras()
                    case "0":
                        break

        case "A" | "2":
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

                match op_almoxarifado:
                    case "B" | "1":
                        buscar_item()
                    case "E" | "2":
                        excluir_item()
                    case "M" | "0":
                        break

        case "V" | "3":
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

                match op_vender:
                    case "C" | "1":
                        exibir_cardapio()

                    case "A" | "2":
                        limpar_tela()
                        op_admi_cardapio = ""

                        while op_admi_cardapio != "0":
                            limpar_tela()
                            titulo("Administrar Cardápio")
                            print("↪︎ 1.  Atualizar Cardápio")
                            print("↪︎ 2.  Excluir Hambúrguer")
                            print("↪︎ 0.  Vendas")

                            op_admi_cardapio = input_tratado("Operação: ")

                            match op_admi_cardapio:
                                case "A" | "1":
                                    existencia, hamburguer = verificar_hamburguer_existente()

                                    if existencia:
                                        atualizar_hamburguer(hamburguer)
                                        input(">> Enter")
                                    else:
                                        error_msg(f"{hamburguer} não encontrado!")
                                        confirmar = input_tratado("Deseja cria-lo?[S/N]: ")

                                        if confirmar[0] in 'S':
                                            burguer = criar_hamburguer()
                                            if burguer:
                                                sucess_msg("Hambúrguer Criado com sucesso!")
                                            else:
                                                error_msg("Erro ao criar o hambúrguer, ingredientes em falta.")
                                            
                                            input(">> Enter")

                                        else:
                                            break

                                case "E" | "2":
                                    burguer_delete = excluir_hamburguer()
                                    if burguer_delete:
                                        sucess_msg("Hambúrguer excluido com sucesso!")
                                    else:
                                        error_msg("Hambúrguer não foi encontrado.")
                                    
                                    input(">> Enter")

                                case "0":
                                    break

                    case "V" | "3":
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

                            match op_fazer_venda:
                                case "V" | "1":
                                    if criar_pedido():
                                        sucess_msg("Pedido lançado no sistema!")
                                    else:
                                        error_msg("Error ao criar pedido.")
                                    input(">> Enter")

                                case "L" | "2":
                                    listar_pedidos()
                                    op_finalizar = ""

                                    while op_finalizar != "0":
                                        print("↪︎ 1.  Confirmar Pedido")
                                        print("↪︎ 2.  Remover Pedido")
                                        print("↪︎ 3.  Editar Pedido")
                                        print("↪︎ 0.  Retornar")
                                        op_finalizar = input_tratado("Operação: ")

                                        match op_finalizar:
                                            case "1" | "C":
                                                limpar_tela()
                                                titulo("Processamento de Pedidos")
                                                finalizar_pedido = int(input_tratado("N° do Pedido: "))
                                                if finalizar_pedido in pedidos:
                                                    pass
                                                else:
                                                    error_msg("Pedido não encotrado.")
                                                    input(">> Enter")
                                                    break

                                                if finalizar_pedido == '0':
                                                    break

                                                nome_hamburguer, quantia_hamburguer, adicional = extrair_informacoes(finalizar_pedido)
                                                atualizar_ingredientes((nome_hamburguer, quantia_hamburguer), "decrementar")
                                                atualizar_adicional(adicional, "decrementar")
                                                sucess_msg("Pedido realizado com sucesso!")
                                                input(">> Enter")

                                            case "2" | "R":
                                                limpar_tela()
                                                titulo("Remoção de pedidos")
                                                excluir_pedido = int(input_tratado("N° do Pedido: "))

                                                if excluir_pedido == '0':
                                                    break
                                                
                                                if deletar_pedido(excluir_pedido):
                                                    sucess_msg("Pedido excluido com sucesso!")
                                                else:
                                                    error_msg("Pedido não alcançado.")
                                                input(">> Enter")
                                                
                                            case "3" | "E":
                                                titulo("Edição de pedidos")
                                                pedido_cliente = int(input_tratado("N° do Pedido: "))

                                                if pedido_cliente == '0':
                                                    break

                                                if editar_pedido(pedido_cliente):
                                                    sucess_msg("Pedido editado!")
                                                else:
                                                    error_msg("Pedido não encontrado.")
                                                input(">> Enter")

                                case "F" | "3":
                                    fechar_vendas()

                                case "0":
                                    break

        case "F" | "4":
            op_funcionarios = ""

            while op_funcionarios != "0":
                operacoes_funcionarios()
                op_funcionarios = input_tratado("Operação:  ")

                match op_funcionarios:
                    case "1" | "Q":
                        limpar_tela()
                        titulo("Quadro de funcionários")

                        for cpf, dados in funcionarios.items():
                            nome = dados['Nome']
                            idade = dados['Idade']
                            quadro(cpf, nome, idade)

                        input(">> Enter")

                    case "2" | "G":
                        chave_acesso = True

                        if chave_acesso:
                            limpar_tela()

                            op_gerenciar = ""
                            while op_gerenciar != "0":
                                limpar_tela()
                                titulo("Administrativo")
                                print("↪︎ 1.  Contratar funcionários")
                                print("↪︎ 2.  Demitir funcionários")
                                print("↪︎ 3.  Buscar funcionário")
                                print("↪︎ 4.  Editar funcionário")
                                print("↪︎ 0. Menu Principal")
                                linha()
                                op_gerenciar = input_tratado("Operação: ")

                                match op_gerenciar:
                                    case "1":
                                        contratar()

                                    case "2":
                                        demitir()

                                    case "3":
                                        buscar()

                                    case "4":
                                        if editar_funcionario():
                                            sucess_msg("Funcionário foi editado com sucesso!")
                                            input(">> Enter")
                                        else:
                                            error_msg("Não cadastrado")
                                            input(">> Enter")

                                    case "0":
                                        break

                    case "0" | "S":
                        break

        case "CL" | "5":
            limpar_tela()
            op_cliente = ""

            while op_cliente != "0":
                operacoes_clientes()

                op_cliente = input_tratado("Operação:   ")

                match op_cliente:
                    case "1" | "C":
                        cadastrar_cliente()

                    case "2" | "L":
                        quadro_clientes()

                    case "3" | "E":
                        quadro_clientes()
                        editar_clientes()

                    case "4" | "D":
                        quadro_clientes()
                        excluir_cliente()

                    case "0" | "S":
                        break

        case "R" | "6":
            limpar_tela()
            op_relatorio = ""

            while op_relatorio != "0":
                limpar_tela()
                titulo("Relatórios")
                print("1 ↪︎ Relatório de Compras")
                print("2 ↪︎ Relatório de Vendas")
                print("3 ↪︎ Relatório de mais vendidos")
                print("4 ↪︎ Relatório de percas")
                print("0 ↪︎ Menu Principal")

                op_relatorio = input_tratado("Operação:   ")

                match op_relatorio:
                    case "1" | "C":
                        processo_compras()

                    case "2" | "V":
                        processos_vendas()

                    case "3":
                        imprimir_ranking()

                    case "0" | "S":
                        break

        case "INF" | "7":
            limpar_tela()
            titulo("Informações")
            subtitulo("Projeto de Gestão de uma Hamburgueria")
            print("-○  Equipe de desenvolvimento:")
            print("-○  Anderson G. Pereira Cruz")
            print("-○  Replit: @gabrielcruz133")
            print("-○  Instagram: biel.ands")
            print("-○  andersong.pereiracruz@gmail.com")
            print("-○  59-378/000 São José do Serído - RN")
            linha()
            input(">> Enter para continuar ")

        case "S" | "0":
            break

limpar_tela()
cabecalho("Hamburgueria do Py")
cabecalho("Até mais")
