from view.screens import clear
from customer.view import screen_client


def main_customer() -> None:
    while True:
        clear()
        screen_client()
        option = input("")

        match option:
            case '1':
                ...  # Add
            case '2':
                ...  # Visualize
            case '3':
                ...  # Busque
            case '4':
                ...  # Remove
            case '5':
                ...  # Edita
            case '0':
                clear()
                return
