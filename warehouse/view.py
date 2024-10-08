from view.screens import header, options
from typing import Dict


def screen_warehouse() -> None:
    header("almoxarifado")
    options(
        "adicionar compra",
        "visualizar almoxarifado",
        "buscar item",
        "excluir item",
        "editar item",
        "menu principal")
    print(">> Escolha uma opção\n")


def bar_warehouse(
        label: str | None = "",
        dict_file: dict | None = None,
        ids: int | None = None) -> None:

    if not label:
        return

    row = 110
    text = label.upper()
    if not dict_file:
        items = ids
    else:
        items = len(dict_file)
    text_width = len(text)
    space = row - text_width - 2
    print(f"\033[1m {'.' * row} ")
    print(f"  {text} {items:<{space}} ")
    print(f" {'.' * row}\033[m")


def infor_warehouse(infor: Dict, text: str | None = "") -> None:
    if text:
        bar_warehouse(text, infor)

    ids = 5
    name = 90
    quantity = 10
    print(f"\033[1;31m-|-----|{"-" * name}|-------------|-")
    print(f" |{'ID':^{ids}}|{'NOME':^{name}}| {'QUANTIDADE':^{quantity}}  |")
    print(f"-|-----|{"-" * 90}|-------------|-\033[m")

    for key, value in infor.items():
        print(f" |{key:^{ids}}|{value[0].title():^{name}}| \
{value[1]:^{quantity}}  |")
        print(f"-|-----|{"-" * 90}|-------------|-")
