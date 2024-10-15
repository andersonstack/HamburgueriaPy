from data.saveFiles import SaveData
from typing import List
from json import dumps
import sqlite3


class Sales(SaveData):
    def __init__(self):
        super().__init__("./data/sales.db")
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def _execute_query(self, query: str, params: tuple = ()) -> bool:
        try:
            with self.conn:
                self.conn.execute(query, params)
                return True
        except sqlite3.OperationalError:
            return False

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_table TEXT,
                food_order LIST,
                price FLOATING
        )"""
        self.conn.execute(query)

    def insert_data(
            self, name_table: str,
            food_order: List[str], price: float) -> bool:
        query = """
        INSERT INTO data(name_table, food_order, price)
        VALUES (?, ?, ?)
        """
        params = (name_table, dumps(food_order, ensure_ascii=False), price)
        return self._execute_query(query, params)


if __name__ == "__main__":
    x = Sales()
    y = x.insert_data(name_table="1", food_order=['X-TUDO', '1'], price=9.99)
    print(y)
