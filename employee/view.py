from view.screens import header, options


def screen_employee() -> None:
    header("funcionários")
    options(
        "contratar funcionário",
        "visualizar funcionário",
        "buscar funcionário",
        "demitir funcionário",
        "editar funcionário",
        "menu principal")
    print(">> Escolha uma opção\n")
