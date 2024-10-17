from view.screens import header, options
from typing import List, Dict


def view_reports(
        report: List[Dict[int, List]], data: str | None = None) -> None:
    total_lenght = 112

    for dics in report:
        header(data if data else "Todas")
        for keys, values in dics.items():
            row_cod = total_lenght - len(f" | Cód: {keys}")
            row_product = total_lenght - len(f" | Produto: {values[0]}")
            row_price = total_lenght - len(f" | Preço: {values[1]}")

            print(f" | Cód: {keys}{' ' * row_cod}|")
            print(f" | Produto: {values[0]}{' ' * row_product}|")
            print(f" | Preço: {values[1]}{' ' * row_price}|")
            print(f"-|{'-' * 110}|-")


def screen_report() -> None:
    header("relatórios")
    options(
        "relatório de compra",
        "relatorio de vendas",
    )
    print(">> Escolha uma opção\n")
