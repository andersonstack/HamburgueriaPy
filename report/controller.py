from report.view import screen_report
from view.screens import clear
from controller.inputs import inputt


def main_report() -> None:
    while True:
        clear()
        screen_report()
        option = inputt("")

        match option:
            case "1":
                # ver relatório de compras
                ...
            case "2":
                # ver relatório de vendas
                ...
            case "0":
                clear()
                return
