from data.saveFiles import SaveData
from menu.view import visualize_menu
from typing import List
from json import dumps, loads
import sqlite3


class Menu(SaveData):
    def __init__(self) -> None:
        super().__init__("./data/cardapio.db")
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _execute_query(self, query: str, params: tuple = ()) -> bool:
        try:
            with self.conn:
                self.conn.execute(query, params)
                return True
        except sqlite3.OperationalError:
            return False

    def _create_table(self) -> None:
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    ingredients LIST,
                    price FLOATING
                )
                """
            )

    def insert_data(self, name: str, ingredients: List[str],
                    price: float) -> bool:
        query = """
        INSERTO INTO data(name, ingredients, price)
        VALUES (?, ?, ?)
        """
        params = (name, dumps(ingredients, ensure_ascii=False), price)
        return self._execute_query(query, params)

    def view_menu(self) -> None:
        query = """
        SELECT * FROM data
        """
        with self.conn:
            cursor = self.conn.execute(query)
            menu = cursor.fetchall()
            if menu == []:
                print("Nenhum item no cardápio")
                return
            else:
                visualize_menu(menu)

    def visualize_hamburguer(self, cod: int) -> None:
        query = """
        SELECT * FROM data
        WHERE id = ?
        """
        with self.conn:
            try:
                cursor = self.conn.execute(query, (cod,))
                burguer = cursor.fetchall()
                if burguer:
                    visualize_menu(burguer)
            except sqlite3.OperationalError:
                print("Não alcançado.")
                return

    def delete_hamburguer(self, cod: int) -> bool:
        query = "DELETE FROM data WHERE id = ?"
        return self._execute_query(query, (cod,))

    def edit_hamburguer(
            self, cod: int, name: str,
            ingredients: List[str], price: float) -> bool:
        query = """
        UPDATE data
        SET name = ?, ingredients = ?, price = ?
        WHERE id = ?
        """
        params = (name, dumps(ingredients, ensure_ascii=False), price, cod)
        return self._execute_query(query, params)

    def handle_hamburguer(self, cod: int):
        self.visualize_hamburguer(cod)
        query = """
            SELECT ingredients
            FROM data
            WHERE id = ?
        """
        with self.conn:
            cursor = self.conn.execute(query, (cod,))
            result = cursor.fetchone()
            if result:
                return loads(result[0])
            else:
                return print("nao ")


if __name__ == "__main__":
    x = Menu()
    y = x.handle_hamburguer(3)
    print(y)
