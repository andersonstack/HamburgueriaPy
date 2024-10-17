from report.view import screen_report
from view.screens import clear
from view.styles import printW
from controller.inputs import inputt, inputDate
from report.model import Reports


def view_shopping_report() -> None:
    data = inputDate("Data:")
    clear()
    report = Reports("warehouse", data if data else "")
    report.show_reports()
    printW("> Enter para continuar")
    inputt("")


def view_sales_report() -> None:
    data = inputDate("Data: ")
    clear()
    report = Reports("sales", data if data else "")
    report.show_reports()
    printW("> Enter para continuar")
    inputt("")


def main_report() -> None:
    while True:
        clear()
        screen_report()
        option = inputt("")

        match option:
            case "1":
                view_shopping_report()
                ...
            case "2":
                view_sales_report()
                ...
            case "0":
                clear()
                return


if __name__ == "__main__":
    view_shopping_report()
