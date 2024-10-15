from view.screens import header, options


def screen_sales() -> None:
    header("vendas")
    options(
        "vender",
        "lista de vendas",
        "buscar venda",
        "fechar vendas",
        "menu principal"
    )
