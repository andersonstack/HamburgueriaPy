from os import system, name


def clear() -> None:
    if name == 'nt':
        system("cls")
    else:
        system("clear")


def _basic(text: str):
    clear()
    header(text)
    print("")


def header(title: str) -> None:
    row = 110
    print(f"\033[1m |{'.' * row}|")
    print(f" |{title.title():^{row}}|")
    print(f" |{'.' * row}|\033[m")


def options(*args) -> None:
    for index, option in enumerate(args, start=1):
        if option == "sair" or option == "menu principal":
            print(f"=| 0. {option.title():<105} |=")
        else:
            print(f"=| {index}. {option.title():<105} |=")
    print(f"{'=' * 114}")


def screen_main() -> None:
    header("hamburgueria py")
    options(
        "almoxarifado",
        "funcionarios",
        "clientes",
        "relatórios",
        "vendas",
        "informações",
        "sair")
    print(">> Escolha uma opção\n")


def screen_client() -> None:
    header("clientes")
    options(
        "adicionar cliente",
        "visualizar cliente",
        "buscar cliente",
        "excluir cliente",
        "editar cliente",
        "menu principal")
    print(">> Escolha uma opção\n")


def screen_report() -> None:
    header("relatórios")
    options(
        "relatório de compra",
        "relatorio de vendas",
    )
    print(">> Escolha uma opção\n")


def screen_sales() -> None:
    header("vendas")
    options(
        "vender",
        "lista de vendas",
        "fechar vendas",
        "menu principal"
    )


def screen_infor() -> None:
    header("informações")
    print("""
    Equipe:
        Anderson G.Pereira Cruz
        github: andersoncruz-13
    """)
    print(">> Escolha uma opção\n")
