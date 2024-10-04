from view.screens import clear, _basic
from warehouse.model import Warehouse
from warehouse.view import screen_warehouse
from controller.inputs import inputStr, inputInt
from view.styles import printS, printW, printE


def add_buy():
    _basic("adicionar compra")
    name = inputStr("Item:\n")
    quantity = inputInt("Quantidade:\n")
    print("")
    buy = Warehouse()
    buy.add_buy(name=name, quantity=quantity)
    printS("Compra cadastrada com sucesso. <Enter>")
    input()


def delete_buy():
    _basic("deletar compra")
    cod = inputInt("Código:\n")
    buy = Warehouse()
    if buy.view_buy(str(cod)):
        confirm = input(f"Deletar {cod}?\n").upper()
        match confirm:
            case 'S':
                buy.delete_buy(str(cod))
                printS("Compra deletada com sucesso. <Enter>")
            case _:
                printW("Ação cancelada. <Enter>")
    else:
        printE("Código não alcançado! <Enter>")

    input()


def visualise_buys():
    _basic("Compras em almoxarifado")
    buy = Warehouse()
    buy.view_warehouse()
    printW("> Enter para continuar")
    input()


def search_buy():
    _basic("Busca de item")
    buy = Warehouse()
    cod = inputInt("Digite o ID do produto:\n")
    if not buy.view_buy(str(cod)):
        printE("Código não alcançado! <Enter>")

    printW("> Enter para continuar")
    input()


def edit_buy():
    _basic("Edição de item")
    buy = Warehouse()
    cod = inputInt("Digite o ID do produto:\n")
    if not buy.view_buy(str(cod)):
        printE("Código não alcançado! <Enter>")
        input()
        return

    name = inputStr("Nome do novo produto:\n")
    buy.edit_buy(str(cod), str(name))

    printS("Item editado com sucesso. <Enter>")
    input("")


def main_warehouse():
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
                return
