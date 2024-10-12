from data.saveFiles import SaveData
from typing import Dict
from warehouse.view import infor_warehouse
import sqlite3


class Warehouse(SaveData):
    def __init__(self) -> None:
        super().__init__("./data/warehouse.db")
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    quantity INTEGER
                )
        """)

    def insert_data(self, name: str, quantity: int) -> bool:
        if not self._verify_name(name):
            try:
                with self.conn:
                    self.conn.execute("""
                        INSERT INTO data(name, quantity)
                        VALUES(?, ?)
                    """, (name, quantity))
                return True
            except sqlite3.OperationalError:
                return False
        self._update_buy(name=name, quantity=quantity)
        return True

    def _update_buy(self, name: str, quantity: int) -> None:
        """
        Updates an existing item in the warehouse.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item to be added.

        Returns:
            None
        """
        with self.conn:
            self.conn.execute("""
                        UPDATE data
                        SET quantity = quantity + ?
                        WHERE name = ?
                        """, (quantity, name))

    def _verify_name(self, name: str) -> bool:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM data
                WHERE name = ?
            """, [name])
            return bool(cursor.fetchall())


if __name__ == '__main__':
    x = Warehouse()
    x.insert_data(name="teste", quantity=10)
    x.close_connection()
