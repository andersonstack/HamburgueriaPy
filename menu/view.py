from typing import Any
from view.screens import _basic


def visualize_menu(menu: list[Any]) -> None:
    _basic("Menu de Lanches")
    total_length = 114  # Comprimento total da linha

    for item in menu:
        item_id = item[0]
        name = item[1]
        ingredients = eval(item[2])  # Converte a string de volta para lista
        price = item[3]

        # Calcular os espaços para alinhamento
        row_id = total_length - len(f" | CÓD: {item_id} |")
        row_name = total_length - len(f" | Nome: {name} |")
        row_ingredients = total_length - len(f" | Ingredientes: {', '.join(ingredients)} |")
        row_price = total_length - len(f" | Preço: R$ {price:.2f} |")

        # Exibir os dados formatados
        print(f" | CÓD: {item_id}{' ' * row_id}|")
        print(f" | Nome: {name}{' ' * row_name}|")
        print(f" | Ingredientes: {', '.join(ingredients)}{' ' * row_ingredients}|")
        print(f" | Preço: R$ {price:.2f}{' ' * row_price}|")
        print(f"-|{'-' * 110}|-")
