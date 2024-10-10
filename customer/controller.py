from view.screens import clear
from customer.view import screen_client
from customer.model import Customer
from controller.inputs import inputStr


def add_client() -> None:
    exists = inputStr("Cliente já teve cadastro?").upper()

    if exists.startswith('S'):
        ...
    elif exists.startswith('N'):
        cliente = Customer()
        name = inputStr("Nome:\n")
        address = input("Endereço:\n")
        cliente.add_customer(name=name, adress=address)
    else:
        print("Entrada inválida. Por favor, responda com 'Sim' ou 'Não'.")


def main_customer() -> None:
    while True:
        clear()
        screen_client()
        option = input("")

        match option:
            case '1':
                add_client()
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


if __name__ == '__main__':
    main_customer()
