from controller.inputs import inputt, inputInt
from menu.model import Menu
from sales.model import Sales
from sales.view import screen_sales
from typing import Dict
from view.screens import clear
from view.styles import printW, printS
from warehouse.model import Warehouse


def extract_ingredients(pedido, quantity) -> Dict[str, int]:
    try:
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
    finally:
        menu.close_connection()


def verify_ingredients(ingredients: Dict[str, int]) -> bool:
    try:
        warehouse = Warehouse()
        items = warehouse.verify_ingredients(ingredients)
        if items:
            return True
        return False
    finally:
        warehouse.close_connection()


def get_price(cod: int) -> float:
    try:
        price = Menu()
        return price.fetch_price(cod)
    finally:
        price.close_connection()


def handle_sell(pedido: int, quantity: int) -> bool:
    ingredients_count = extract_ingredients(pedido, quantity)
    if len(ingredients_count) > 0:
        if verify_ingredients(ingredients_count):
            return True
    return False


def sell():
    pedido = inputInt("N° Pedido:\n")
    quantity = inputInt("Quantia:\n")

    if handle_sell(pedido, quantity):
        price = get_price(pedido)
        sales = Sales()
        sales.insert_data("Anderson", pedido, price)
        printS("Pedido realizado com sucesso. <Enter>")
        input()
        return

    printW("Erro ao fazer o pedido. <Enter>")
    input()
    return


def view_all_sales() -> None:
    sales = Sales()
    sales.fetch_all_sales()
    sales.close_connection()
    printW("> Enter para continuar")
    input
    return


def search_sales() -> None:
    cod = inputInt("N° do pedido: ")
    sales = Sales()
    sales.fetch_one_sales(cod)
    sales.close_connection()
    printW("> Enter para continuar")
    input
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
                view_all_sales()
                ...
            case '3':
                search_sales()
                ...
            case '4':
                # close sales
                ...
            case '0':
                clear()
                return


if __name__ == '__main__':
    sell()
