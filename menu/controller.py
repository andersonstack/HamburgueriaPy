from menu.view import screen_menu
from view.screens import clear


def main_menu() -> None:
    while True:
        clear()
        screen_menu()
        option = input("")

        while True:
            match option:
                case '1':
                    # add
                    ...
                case '2':
                    # view
                    ...
                case '3':
                    # search
                    ...
                case '4':
                    # delete
                    ...
                case '5':
                    # edit
                    ...
                case '0':
                    clear()
                    return


if __name__ == "__main__":
    ...