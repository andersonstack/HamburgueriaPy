from view.screens import clear, _basic
from warehouse.model import Warehouse
from warehouse.view import screen_warehouse
from controller.inputs import inputStr, inputInt
from view.styles import printS, printW, printE


def add_buy() -> None:
    _basic("adicionar compra")
    name = inputStr("Item:\n")
    quantity = inputInt("Quantidade:\n")
    print("")
    buy = Warehouse()
    buy.insert_data(name=name, quantity=quantity)
    printS("Compra cadastrada com sucesso. <Enter>")
    buy.close_connection()
    input()


def delete_buy() -> None:
    _basic("deletar compra")
    cod = inputInt("Código:\n")
    buy = Warehouse()
    if buy.visualize_buy(cod):
        confirm = input(f"Deletar {cod}?\n").upper()
        if confirm.startswith('S'):
                buy.delete_buy(cod)
                printS("Compra deletada com sucesso. <Enter>")
        else
                printW("Ação cancelada. <Enter>")
    else:
        printE("Código não alcançado! <Enter>")

    input()


def visualise_buys() -> None:
    _basic("Compras em almoxarifado")
    buy = Warehouse()
    buy.visualize_buys()
    printW("> Enter para continuar")
    buy.close_connection()
    input()


def search_buy() -> None:
    _basic("Busca de item")
    buy = Warehouse()
    cod = inputInt("Digite o ID do produto:\n")
    if not buy.visualize_buy(cod):
        printE("Código não alcançado! <Enter>")
        buy.close_connection()
        input()
        return

    printW("> Enter para continuar")
    buy.close_connection()
    input()


def edit_buy() -> None:
    _basic("Edição de item")
    buy = Warehouse()
    cod = inputInt("Digite o ID do produto:\n")
    if not buy.visualize_buy(cod):
        printE("Código não alcançado! <Enter>")
        input()
        return

    # name = inputStr("Nome do novo produto:\n")
    # buy.edit_buy(str(cod), str(name))

    printS("Item editado com sucesso. <Enter>")
    input("")


def main_warehouse() -> None:
    while True:
        clear()
        screen_warehouse()
        option = input("")

        match option:
            case '1':
                add_buy()
            case '2':
                visualise_buys()
            case '3':
                search_buy()
            case '4':
                delete_buy()
            case '5':
                edit_buy()
            case '0':
                clear()
                return


if __name__ == "__main__":
    delete_buy()
