from controller.inputs import inputt, inputInt
from employee.model import Employee
from menu.model import Menu
from sales.model import Sales
from sales.view import screen_sales
from typing import Dict
from view.screens import clear
from view.styles import printW, printS, printE
from warehouse.model import Warehouse


class MenuContext:
    def __init__(self):
        self.menu = Menu()

    def __enter__(self):
        return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.menu.close_connection()


class WarehouseContext:
    def __init__(self):
        self.warehouse = Warehouse()

    def __enter__(self):
        return self.warehouse

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.warehouse.close_connection()


def extract_ingredients(order: int, quantity: int) -> Dict[str, int]:
    with MenuContext() as menu:
        ingredients = menu.handle_hamburguer(order)
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
    with WarehouseContext() as warehouse:
        return warehouse.verify_ingredients(ingredients) is not None


def get_price(code: int) -> float:
    with MenuContext() as menu:
        return menu.fetch_price(code)


def handle_sell(pedido: int, quantity: int) -> bool:
    ingredients_count = extract_ingredients(pedido, quantity)
    if ingredients_count and verify_ingredients(ingredients_count):
        return True
    return False


def sell():
    order = inputInt("N° Pedido:\n")
    quantity = inputInt("Quantia:\n")

    if handle_sell(order, quantity):
        price = get_price(order)
        sales = Sales()
        sales.insert_data("Anderson", order, price)
        printS("Pedido realizado com sucesso. <Enter>")
    else:
        printW("Erro ao fazer o pedido. <Enter>")
    input()


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


def close_sales() -> None:
    cpf = inputInt("CPF: ")
    employee = Employee()
    if employee.visualize_employee(str(cpf)):
        close = Sales()
        if close.close_sales():
            printS("> Vendas fechadas com sucesso! <Enter>")
        else:
            printE("Erro ao fechar as vendas! <Enter>")
        close.close_connection()
    else:
        printE("Erro ao processar o cpf! <Enter>")
    input()


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
                close_sales()
                ...
            case '0':
                clear()
                return


if __name__ == '__main__':
    close_sales()
