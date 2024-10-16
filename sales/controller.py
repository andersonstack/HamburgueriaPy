from sales.view import screen_sales
from controller.inputs import inputt, inputInt
from view.styles import printW, printS
from view.screens import clear
from menu.model import Menu
from warehouse.model import Warehouse
from typing import Dict


def extract_ingredients(pedido, quantity) -> Dict[str, int]:
    menu = Menu()
    ingredients = menu.handle_hamburguer(pedido)
    if not ingredients:
        return {}

    ingredients_count: Dict[str, int] = {}

    for i in ingredients:
        ingredient_clean = i.strip('\"')
        if ingredient_clean in ingredients_count:
            ingredients_count[ingredient_clean] += 1
        else:
            ingredients_count[ingredient_clean] = 1

    for i, j in ingredients_count.items():
        ingredients_count[i] = j * quantity
    return ingredients_count


def verify_ingredients(ingredients: Dict[str, int]) -> bool:
    warehouse = Warehouse()
    items = warehouse.verify_ingredients(ingredients)
    if items:
        return True
    return False


def handle_sell(pedido: int, quantity: int) -> bool:
    ingredients_count = extract_ingredients(pedido, quantity)
    if len(ingredients_count) > 0:
        if verify_ingredients(ingredients_count):
            printS("Pedido realizado com sucesso. <Enter>")
            input()
            return True
    return False


def sell():
    pedido = inputInt("N° Pedido:\n")
    quantity = inputInt("Quantia:\n")

    if handle_sell(pedido, quantity):
        print("ok")
        return

    printW("Erro ao fazer o pedido. <Enter>")
    input()
    return


def main_sales():
    while True:
        clear()
        screen_sales()
        option = inputt("")

        match option:
            case '1':
                sell()
            case '2':
                # visualize
                ...
            case '3':
                # search
                ...
            case '4':
                # close sales
                ...
            case '0':
                clear()
                return


if __name__ == '__main__':
    sell()
