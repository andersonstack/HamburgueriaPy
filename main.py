####################################
###         VERSÃO 15            ###
####################################


#   Importações de módulos do projeto
from almoxarifado import buscar_item, excluir_item
from clientes import cadastrar_cliente, quadro_clientes, editar_clientes, excluir_cliente
from compras import cadastrar_compras
from data import almoxarifado, funcionarios
from funcionarios import contratar, demitir, buscar, editar_funcionario
from menu import (
    exibir_cardapio, verificar_hamburguer_existente, 
    atualizar_hamburguer, criar_novo_hamburguer, excluir_hamburguer
)
from relatorios import processo_compras, processos_vendas, imprimir_ranking, exibir_percas
from tools import varredura, limpar_tela, input_tratado
from vendas import (
    listar_pedidos, criar_pedido, decrementar_ingredientes, 
    perca_de_ingredientes, editar_pedido, fechar_vendas,
    deletar_pedido
)
from views import (
    cabecalho, titulo, principal, linha, quadro_almoxarifado, 
    sucess_msg, error_msg, leia_int, operacoes_clientes, 
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
                                    hamburguer = verificar_hamburguer_existente()

                                    if hamburguer:
                                        atualizar_hamburguer(hamburguer)
                                    else:
                                        confirmar = input_tratado("Deseja cria-lo?[S/N]: ")

                                        if confirmar[0] in 'S':
                                            criar_novo_hamburguer()
                                        else:
                                            break

                                case "E" | "2":
                                    excluir_hamburguer()

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
                                    criar_pedido()

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

                                                if finalizar_pedido == '0':
                                                    break

                                                decrementar_ingredientes(finalizar_pedido)
                                                sucess_msg("Pedido realizado com sucesso!")
                                                input(">> Enter")

                                            case "2" | "R":
                                                limpar_tela()
                                                titulo("Remoção de pedidos")
                                                excluir_pedido = int(input_tratado("N° do Pedido: "))

                                                if excluir_pedido == '0':
                                                    break

                                                subtitulo("ATENÇÃO")
                                                deletar_pedido = input_tratado("Pedido já foi confirmado (S/N): ")
                                                linha()

                                                match deletar_pedido:
                                                    case 'S':
                                                        perca_de_ingredientes(excluir_pedido)
                                                    case 'N':
                                                        deletar_pedido(excluir_pedido)

                                            case "3" | "E":
                                                titulo("Edição de pedidos")
                                                pedido_cliente = int(input_tratado("N° do Pedido: "))

                                                if pedido_cliente == '0':
                                                    break

                                                editar_pedido(pedido_cliente)

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
                    
                    case "4":
                        exibir_percas()

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