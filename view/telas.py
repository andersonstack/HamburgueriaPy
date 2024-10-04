from os import system, name


def clear() -> None:
    if name == 'nt':
        system("cls")
    else:
        system("clear")


def _basic(text: str):
    clear()
    cabecalho(text)
    print("")


def cabecalho(title: str) -> None:
    row = 110
    print(f"\033[1m |{'.' * row}|")
    print(f" |{title.title():^{row}}|")
    print(f" |{'.' * row}|\033[m")


def opcoes(*args) -> None:
    for index, option in enumerate(args, start=1):
        if option == "sair" or option == "menu principal":
            print(f"=| 0. {option.title():<105} |=")
        else:
            print(f"=| {index}. {option.title():<105} |=")
    print(f"{'=' * 114}")


def tela_principal() -> None:
    cabecalho("hamburgueria py")
    opcoes(
        "almoxarifado",
        "funcionarios",
        "clientes",
        "relatórios",
        "vendas",
        "informações",
        "sair")
    print(">> Escolha uma opção\n")


def tela_clientes() -> None:
    cabecalho("clientes")
    opcoes(
        "adicionar cliente",
        "visualizar cliente",
        "buscar cliente",
        "excluir cliente",
        "editar cliente",
        "menu principal")
    print(">> Escolha uma opção\n")


def tela_relatorios() -> None:
    cabecalho("relatórios")
    opcoes(
        "relatório de compra",
        "relatorio de vendas",
    )
    print(">> Escolha uma opção\n")


def tela_vendas() -> None:
    cabecalho("vendas")
    opcoes(
        "vender",
        "lista de vendas",
        "fechar vendas",
        "menu principal"
    )


def tela_informacoes() -> None:
    cabecalho("informações")
    print("""
    Equipe:
        Anderson G.Pereira Cruz
        github: andersoncruz-13
    """)
    print(">> Escolha uma opção\n")
