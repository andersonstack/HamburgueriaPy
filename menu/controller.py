from controller.inputs import inputStr, inputFloat, inputInt, inputt
from menu.model import Menu
from menu.view import screen_menu
from view.screens import clear, _basic
from view.styles import printW, printS, printE


def collect_burguer_data() -> tuple:
    """Coleta os dados do hambúrguer (nome, preço, ingredientes)"""
    name = inputStr("Nome do Hambúrguer: ")
    price = inputFloat("Preço: ")

    ingredients = []
    numbers = 1
    printW("Ingredientes")
    while True:
        ingredient = inputStr(f"Ingrediente {numbers}: ")
        ingredients.append(ingredient)

        if len(ingredient) >= 1:
            printW("Deseja parar de adicionar ingredientes? ")
            op = input().upper()

            if op.startswith("S"):
                break

        numbers += 1

    return name, ingredients, price


def handle_burguer(menu: Menu, cod: int | None = None) -> None:
    """
    Lida com a adição ou edição de um hambúrguer.
    Se `cod` for fornecido, edita; senão, adiciona um novo hambúrguer.
    """
    try:
        if cod:
            printW(f"Editando hambúrguer de código {cod}...")
            menu.visualize_hamburguer(cod)

        name, ingredients, price = collect_burguer_data()

        if cod:
            if menu.edit_hamburguer(cod, name, ingredients, price):
                printS("Hambúrguer editado com sucesso!")
            else:
                printE("Falha ao editar hambúrguer.")
        else:
            if menu.insert_data(
                    name=name, ingredients=ingredients, price=price):
                printS("Hambúrguer adicionado com sucesso!")
            else:
                printE("Falha ao adicionar hambúrguer.")
    except Exception as e:
        printE(f"Erro ao processar hambúrguer: {e}")
    finally:
        menu.close_connection()
    input()
    return


def add_burguer():
    _basic("Adicionar Hambúrguer")
    menu = Menu()
    handle_burguer(menu)


def edit_burguer():
    _basic("Editar Hambúrguer")
    cod = inputInt("Código: ")
    menu = Menu()
    handle_burguer(menu, cod)


def view_menu() -> None:
    menu = Menu()
    try:
        menu.view_menu()
    except Exception as e:
        printE(f"Erro ao visualizar o menu: {e}")
    finally:
        menu.close_connection()
    printW("> Enter para continuar")
    input()
    return


def search_burguer() -> None:
    cod = inputInt("Código: ")
    menu = Menu()
    try:
        menu.visualize_hamburguer(cod)
    except Exception as e:
        printE(f"Erro ao buscar hambúrguer: {e}")
    finally:
        menu.close_connection()
    printW("> Enter para continuar")
    input()
    return


def delete_burguer() -> None:
    _basic("Deletar Hambúrguer")
    cod = inputInt("Código: ")
    menu = Menu()
    try:
        menu.visualize_hamburguer(cod)
        printW("Deletar Hambúrguer? \n")
        confirm = input().upper()
        if confirm.startswith("S"):
            if menu.delete_hamburguer(cod):
                printS("Hambúrguer deletado com sucesso!")
            else:
                printE("Falha ao deletar hambúrguer.")
        else:
            printW("Ação cancelada.")
    except Exception as e:
        printE(f"Erro ao deletar hambúrguer: {e}")
    finally:
        menu.close_connection()
    input()
    return


def main_menu() -> None:
    while True:
        clear()
        screen_menu()
        option = inputt("")

        match option:
            case '1':
                add_burguer()
            case '2':
                view_menu()
            case '3':
                search_burguer()
            case '4':
                delete_burguer()
            case '5':
                edit_burguer()
            case '0':
                clear()
                return


if __name__ == "__main__":
    edit_burguer()
