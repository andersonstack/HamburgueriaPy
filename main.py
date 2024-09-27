from view import telas

get_out = False

while not get_out:
    telas.tela_principal()
    option = input("")

    match option:
        case '1':
            telas.tela_almoxarifado()
        case '2':
            telas.tela_funcionarios()
        case '3':
            telas.tela_clientes()
        case '4':
            telas.tela_relatorios()
        case '5':
            telas.tela_vendas()
        case '6':
            telas.tela_informacoes()
        case '0':
            print("Obrigado por usar o programa! :)\n")
            get_out = True
            break
        case _:
            print("Opção inválida...\n")

    option = input("Escolha outra opção ou '0' para voltar: \n")
