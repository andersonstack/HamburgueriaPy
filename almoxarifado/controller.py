from view.telas import clear, cabecalho
from almoxarifado.model import Almoxarifado
from almoxarifado.view import tela_almoxarifado


def _basic(text: str):
    clear()
    cabecalho(text)
    print("")


def add_buy():
    _basic("adicionar compra")
    name = input("Item:\n")
    quantity = int(input("Quantidade:\n"))
    print("")
    buy = Almoxarifado()
    buy.add_buy(name=name, quantity=quantity)
    input("> Enter para continuar")


def delete_buy():
    _basic("deletar compra")
    cod = input("Código:\n")
    buy = Almoxarifado()
    if buy.view_buy(cod):
        confirm = input(f"Deletar {cod}?\n")
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
    cod = input("Digite o ID do produto:\n")
    if not buy.view_buy(str(cod)):
        print("Código não alcançado!\n")

    input("> Enter para continuar")


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
                ...
            case '3':
                search_buy()
                ...
            case '4':
                delete_buy()
                ...
            case '5':
                # editar item
                ...
            case '0':
                return
