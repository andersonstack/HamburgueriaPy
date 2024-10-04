from view.screens import clear
from employee.view import screen_employee


def main_employee() -> None:
    while True:
        clear()
        screen_employee()
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
