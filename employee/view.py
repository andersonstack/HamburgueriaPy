from view.screens import header, options, _basic
from typing import Dict


def view_employee(infor: Dict[str, list]) -> None:
    _basic("Funcionário(s)")
    # Comprimento total da linha
    total_length = 114

    for keys in infor:
        row_cpf = total_length - len(f" | CPF: {keys} |")
        row_name = total_length - len(f" | Nome: {infor[keys][0]} |")
        row_address = total_length - len(f" | Endereço: {infor[keys][2]} |")
        row_age = total_length - len(f" | Idade: {infor[keys][1]} |")
        row_phone = total_length - len(f" | Telefone: {infor[keys][3]} |")

        print(f" | CPF: {keys}{' ' * row_cpf}|")
        print(f" | Nome: {infor[keys][0]}{' ' * row_name}|")
        print(f" | Idade: {infor[keys][1]}{' ' * row_age}|")
        print(f" | Endereço: {infor[keys][2]}{' ' * row_address}|")
        print(f" | Telefone: {infor[keys][3]}{' ' * row_phone}|")
        print(f"-|{"-" * 110}|-")


def screen_employee() -> None:
    header("funcionários")
    options(
        "contratar funcionário",
        "visualizar funcionários",
        "buscar funcionário",
        "demitir funcionário",
        "editar funcionário",
        "menu principal")
    print(">> Escolha uma opção\n")


if __name__ == '__main__':
    ...
