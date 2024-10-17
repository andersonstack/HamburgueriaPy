from view.screens import header, options


def screen_report() -> None:
    header("relatórios")
    options(
        "relatório de compra",
        "relatorio de vendas",
    )
    print(">> Escolha uma opção\n")