from sales.view import screen_sales
from controller.inputs import inputt
from view.screens import clear


def main_sales():
    while True:
        clear()
        screen_sales()
        option = inputt("")

        match option:
            case '1':
                # add
                ...
            case '2':
                # visualize
                ...
            case '3':
                # search
                ...
            case '4':
                # close sales
                ...
            case '0':
                clear()
                return
