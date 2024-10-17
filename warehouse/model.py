from services.saveFiles import SaveData
from typing import Dict, Optional
from warehouse.view import infor_warehouse
import sqlite3


class Warehouse(SaveData):
    def __init__(self) -> None:
        super().__init__("./data/warehouse.db")
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self) -> None:
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    quantity INTEGER
                )
        """)

    def insert_data(self, name: str, quantity: int) -> bool:
        return self._update_or_add_item(name, quantity)

    def _update_or_add_item(self, name: str, quantity: int) -> bool:
        if self._verify_name(name):
            return self._update_item(name, quantity)
        return self._add_item(name, quantity)

    def _add_item(self, name: str, quantity: int) -> bool:
        return self._execute_query(
            """
                INSERT INTO data(name, quantity)
                VALUES (?, ?)
            """, (name, quantity)
        )

    def _update_item(self, name: str, quantity: int) -> bool:
        return self._execute_query(
            """
                UPDATE data
                SET quantity = quantity + ?
                WHERE name = ?
            """, (quantity, name)
        )

    def _verify_name(self, name: str) -> bool:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT EXISTS(SELECT 1 FROM data WHERE name = ?)
            """, (name,))
            return cursor.fetchone()[0] == 1

    def visualize_buys(self) -> None:
        all_buys = self._fetch_all_buys()
        if not all_buys:
            print("Nenhum item no almoxarifado")
        else:
            infor_warehouse(all_buys, text="Itens no almoxarifado:")

    def _fetch_all_buys(self) -> Dict[int, list]:
        all_buys = {}
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM data
            """)
            for row in cursor:
                all_buys[row[0]] = [row[1], row[2]]
            return all_buys

    def visualize_buy(self, cod: int) -> Optional[Dict[int, list]] | bool:
        data_buy = self._fetch_single_buy(cod)
        if data_buy:
            infor_warehouse(data_buy)
            return data_buy
        return None

    def _fetch_single_buy(self, cod: int) -> Optional[Dict[int, list]]:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM data WHERE id = ?
            """, (cod,))
            data = cursor.fetchone()
            return {data[0]: [data[1], data[2]]} if data else None

    def delete_buy(self, cod: int) -> bool:
        return self._execute_query("""
            DELETE FROM data WHERE id = ?
        """, (cod,))

    def edit_buy(self, cod: int, name: str) -> bool:
        return self._execute_query("""
            UPDATE data SET name = ? WHERE id = ?
        """, (name, cod))

    def _execute_query(self, query: str, params: tuple) -> bool:
        try:
            with self.conn:
                self.conn.execute(query, params)
            return True
        except sqlite3.OperationalError:
            return False

    def verify_ingredients(self, ingredients: Dict[str, int]) -> bool:
        query = """
            SELECT name, quantity
            FROM data
        """
        with self.conn:
            cursor = self.conn.execute(query).fetchall()

            available_ingredients = {
                item[0].lower(): item[1] for item in cursor
            }

        for ingredient, required_quantity in ingredients.items():
            ingredient_lower = ingredient.lower()
            if ingredient_lower in available_ingredients:
                if required_quantity > available_ingredients[ingredient_lower]:
                    return False
            else:
                return False

        self._update_ingredients(ingredients)

        return True

    def _update_ingredients(self, ingredients: Dict[str, int]) -> None:
        for ingredient, quantity in ingredients.items():
            ingredient_lower = ingredient.lower()
            with self.conn:
                self.conn.execute(
                    """
                    UPDATE data
                    SET quantity = quantity - ?
                    WHERE name = ?
                    """, (quantity, ingredient_lower)
                )


if __name__ == '__main__':
    x = Warehouse()
    y = x.verify_ingredients(
        {
            "carne": 2,
            "tomate": 1
        }
    )
    print(y)
