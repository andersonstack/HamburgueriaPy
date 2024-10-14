from data.saveFiles import SaveData
from menu.view import visualize_menu
from typing import List
from json import dumps
import sqlite3


class Menu(SaveData):
    def __init__(self) -> None:
        super().__init__("./data/cardapio.db")
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    ingredients LIST,
                    price FLOATING
                )
                """
            )

    def insert_data(self, name: str, ingredients: List[str],
                    price: float) -> None:
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO data(name, ingredients, price)
                VALUES (?, ?, ?)
                """, (name, dumps(ingredients, ensure_ascii=False), price)
            )

    def view_menu(self) -> None:
        with self.conn:
            cursor = self.conn.execute(
                """
                SELECT * FROM data
                """
            )
            menu = cursor.fetchall()
            visualize_menu(menu)


if __name__ == "__main__":
    # name = "X-TUDO"
    # ingredients = ['Pão', 'Bacon', 'Bacon', 'Salsicha', 'Ovo']
    # price = 10.99
    x = Menu()
    # x.insert_data(name=name, ingredients=ingredients, price=price)
    x.view_menu()
