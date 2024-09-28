from almoxarifado.controller import Almoxarifado
from view.telas import tela_almoxarifado, clear


def add_buy():
    clear()
    name = input("Item:\n")
    quantity = input("Quantidade:\n")
    buy = Almoxarifado()
    buy.add_buy(name=name, quantity=quantity)


def main_almoxarifado():
    while True:
        clear()
        tela_almoxarifado()
        option = input("")

        match option:
            case '1':
                add_buy()
            case '2':
                # visualizar almoxarifado
                ...
            case '3':
                # buscar item
                ...
            case '4':
                # excluir item
                ...
            case '5':
                # editar item
                ...
            case '0':
                return
