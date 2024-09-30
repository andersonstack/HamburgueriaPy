from os import system, name


def clear() -> None:
    if name == 'nt':
        system("cls")
    else:
        system("clear")


def cabecalho(title: str) -> None:
    line = "=" * 29
    print(f"=|{line}|=")
    print(f" | {title.title():^28}|")
    print(f"=|{line}|=")


def opcoes(*args) -> None:
    for index, option in enumerate(args, start=1):
        if option == "sair" or option == "menu principal":
            print(f"=| 0. {option.title():<24} |=")
        else:
            print(f"=| {index}. {option.title():<24} |=")
    print(f"{'=' * 33}")


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


def tela_almoxarifado() -> None:
    cabecalho("almoxarifado")
    opcoes(
        "adicionar compra",
        "visualizar almoxarifado",
        "buscar item",
        "excluir item",
        "editar item",
        "menu principal")
    print(">> Escolha uma opção\n")


def tela_funcionarios() -> None:
    cabecalho("funcionários")
    opcoes(
        "contratar funcionário",
        "visualizar funcionário",
        "buscar funcionário",
        "demitir funcionário",
        "editar funcionário",
        "menu principal")
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


if __name__ == "__main__":
    tela_principal()
    tela_almoxarifado()
    tela_funcionarios()
    tela_clientes()
    tela_relatorios()
    tela_informacoes()
