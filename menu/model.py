from services.saveFiles import SaveData
from json import dumps, loads
from menu.view import visualize_menu
from typing import List
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
        query = """
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            ingredients TEXT,  -- Corrigido para TEXT
            price REAL
        )
        """
        self._execute_query(query)

    def insert_data(
            self, name: str, ingredients: List[str], price: float) -> bool:
        query = """
        INSERT INTO data (name, ingredients, price)
        VALUES (?, ?, ?)
        """
        params = (name, dumps(ingredients, ensure_ascii=False), price)
        return self._execute_query(query, params)

    def view_menu(self) -> None:
        query = "SELECT * FROM data"
        with self.conn:
            cursor = self.conn.execute(query)
            menu = cursor.fetchall()
            if not menu:
                print("Nenhum item no cardápio")
                return
            visualize_menu(menu)

    def visualize_hamburguer(self, cod: int) -> None:
        query = "SELECT * FROM data WHERE id = ?"
        with self.conn:
            cursor = self.conn.execute(query, (cod,))
            burguer = cursor.fetchall()
            if burguer:
                visualize_menu(burguer)

    def find_hamburguer(self, cod: int) -> bool:
        query = "SELECT * FROM data WHERE id = ?"
        with self.conn:
            cursor = self.conn.execute(query, (cod,))
            burguer = cursor.fetchall()
            if burguer:
                return True
            else:
                return False

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
        if self._check_index(cod):
            self.visualize_hamburguer(cod)
            query = "SELECT ingredients FROM data WHERE id = ?"
            with self.conn:
                cursor = self.conn.execute(query, (cod,))
                result = cursor.fetchone()
                if result:
                    return loads(result[0])
        return False

    def _check_index(self, cod: int) -> bool:
        query = "SELECT COUNT(*) FROM data WHERE id = ?"
        with self.conn:
            cursor = self.conn.execute(query, (cod,))
            result = cursor.fetchone()
            return result[0] > 0

    def fetch_price(self, cod: int) -> float:
        query = "SELECT price FROM data WHERE id = ?"
        with self.conn:
            cursor = self.conn.execute(query, (cod,))
            result = cursor.fetchone()
            return result[0] if result else None

    def close_connection(self) -> None:
        self.conn.close()


if __name__ == "__main__":
    menu = Menu()
    price = menu.fetch_price(1)
    print(price)
    menu.close_connection()
