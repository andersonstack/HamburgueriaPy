from sales.view import screen_sales
from controller.inputs import inputt
from view.screens import clear
from menu.model import Menu
from typing import Dict


def extract_ingredients(pedido, quantity) -> Dict[str, int]:
    menu = Menu()
    ingredients = menu.handle_hamburguer(pedido)
    ingredients_count: Dict[str, int] = {}

    for i in ingredients:
        # Removendo as aspas se ainda existirem
        ingredient_clean = i.strip('\"')
        if ingredient_clean in ingredients_count:
            ingredients_count[ingredient_clean] += 1
        else:
            ingredients_count[ingredient_clean] = 1

    for i, j in ingredients_count.items():
        ingredients_count[i] = j * quantity
    return ingredients_count


def handle_sell():

    pedido = 3
    quantity = 5

    ingredients_count = extract_ingredients(pedido, quantity)
    print(ingredients_count)


def sell():
    ...


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
    handle_sell()
