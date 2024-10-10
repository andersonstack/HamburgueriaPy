from view.screens import header, options


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
