from view.telas import clear
from funcionarios.view import tela_funcionarios


def main_funcionarios() -> None:
    while True:
        clear()
        tela_funcionarios()
        option = input("")

        match option:
            case '1':
                ...
            case '2':
                ...
            case '3':
                ...
            case '4':
                ...
            case '5':
                ...
            case '0':
                return
