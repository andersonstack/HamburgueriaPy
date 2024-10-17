from view.screens import header, options, _basic
from typing import Dict, List


def view_sales(sales: Dict[int, List[str]]) -> None:
    _basic("LISTA DE PEDIDOS")
    total_lenght = 114

    for key, values in sales.items():

        row_id = total_lenght - len(f" | N° Pedido: {key} |")
        row_client = total_lenght - len(f" | Cliente: {values[0]} |")
        row_food = total_lenght - len(f" | Pedido: {values[1]} |")
        row_price = total_lenght - len(f" | Preço: R$ {values[2]} |")

        print(f" | N° Pedido: {key}{' ' * row_id}|")
        print(f" | Cliente: {values[0]}{' ' * row_client}|")
        print(f" | Pedido: {values[1]}{' ' * row_food}|")
        print(f" | Preço: R$ {values[2]}{' ' * row_price}|")
        print(f"-|{'-' * 110}|-")


def screen_sales() -> None:
    header("vendas")
    options(
        "vender",
        "lista de vendas",
        "buscar venda",
        "fechar vendas",
        "menu principal"
    )
