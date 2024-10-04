from view.telas import cabecalho, opcoes


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