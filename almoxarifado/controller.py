from view.telas import clear, cabecalho
from almoxarifado.model import Almoxarifado
from almoxarifado.view import tela_almoxarifado
from controller.inputs import inputStr, inputInt


def _basic(text: str):
    clear()
    cabecalho(text)
    print("")


def add_buy():
    _basic("adicionar compra")
    name = inputStr("Item:\n")
    quantity = inputInt("Quantidade:\n")
    print("")
    buy = Almoxarifado()
    buy.add_buy(name=name, quantity=quantity)
    input("> Enter para continuar")


def delete_buy():
    _basic("deletar compra")
    cod = inputInt("Código:\n")
    buy = Almoxarifado()
    if buy.view_buy(str(cod)):
        confirm = input(f"Deletar {cod}?\n").upper()
        match confirm:
            case 'S':
                buy.delete_buy(cod)
                print("Compra deletada!\n")
            case _:
                print("Ação cancelada.\n")
    else:
        print("Código não alcançado!\n")

    input("> Enter para continuar")


def visualise_buys():
    _basic("Compras em almoxarifado")
    buy = Almoxarifado()
    buy.view_buys()
    input("> Enter para continuar")


def search_buy():
    _basic("Busca de item")
    buy = Almoxarifado()
    cod = inputInt("Digite o ID do produto:\n")
    if not buy.view_buy(str(cod)):
        print("Código não alcançado!\n")

    input("> Enter para continuar")


def edit_buy():
    _basic("Edição de item")
    buy = Almoxarifado()
    cod = inputInt("Digite o ID do produto:\n")
    if not buy.view_buy(str(cod)):
        print("Código não alcançado!\n")

    name = inputStr("Nome do novo produto:\n")
    buy.edit_buy(str(cod), str(name))

    input("> Item editado. Enter para continuar")


def main_almoxarifado():
    while True:
        clear()
        tela_almoxarifado()
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
