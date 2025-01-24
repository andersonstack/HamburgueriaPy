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
        "cardápio",
        "relatórios",
        "vendas",
        "informações",
        "sair")
    print(">> Escolha uma opção\n")


def screen_infor() -> None:
    header("informações")
    print("""
    Equipe:
        Anderson G.Pereira Cruz
        github: andersoncruz-13
    """)
    input(">> Enter para continuar\n")
