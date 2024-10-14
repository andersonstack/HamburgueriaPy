from menu.view import screen_menu
from menu.model import Menu
from view.screens import clear, _basic
from view.styles import printW, printS
from controller.inputs import inputStr, inputFloat, inputInt


def add_burguer():
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


def view_menu() -> None:
    menu = Menu()
    menu.view_menu()
    menu.close_connection()
    printW("> Enter para continuar")
    input()


def search_burguer() -> None:
    cod = inputInt("Código: ")
    menu = Menu()
    menu.visualize_hamburguer(cod)
    menu.close_connection()
    printW("> Enter para continuar")
    input()


def delete_burguer() -> None:
    _basic("Deletar Hambúrguer")
    cod = inputInt("Código: ")
    menu = Menu()
    menu.visualize_hamburguer(1)
    printW("Deletar Hambúrguer? \n")
    confirm = input().upper()
    if confirm.startswith("S"):
        menu.delete_hamburguer(cod)
        menu.close_connection()
        printS("Hambúrguer deletado com sucesso. <Enter>")
        input()
        return
    else:
        printW("Ação cancelada. <Enter>")
        input()
        return


def edit_burguer():
    ...


def main_menu() -> None:
    while True:
        clear()
        screen_menu()
        option = input("")

        while True:
            match option:
                case '1':
                    add_burguer()
                    ...
                case '2':
                    view_menu()
                    ...
                case '3':
                    search_burguer()
                    ...
                case '4':
                    delete_burguer()
                    ...
                case '5':
                    edit_burguer()
                    ...
                case '0':
                    clear()
                    return


if __name__ == "__main__":
    add_burguer()
