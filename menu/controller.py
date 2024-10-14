from menu.view import screen_menu
from menu.model import Menu
from view.screens import clear, _basic
from view.styles import printW
from controller.inputs import inputStr, inputFloat


def add_hamburguer():
    _basic("Adicionar Hambúrguer")
    name = inputStr("Hambúrguer: ")
    price = inputFloat("Preço: ")

    ingredients = []
    numbers = 1
    printW("Ingredientes")
    while True:
        ingredient = inputStr(f"Ingrediente {numbers}: ")
        ingredients.append(ingredient)

        if len(ingredient) >= 1:
            printW("Deseja sair? ")
            op = input().upper()

            if op.startswith("S"):
                break

        numbers += 1

    hamburguer = Menu()
    hamburguer.insert_data(name=name, ingredients=ingredients, price=price)
    hamburguer.close_connection()


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
    add_hamburguer()
