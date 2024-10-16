from data.saveFiles import SaveData
import sqlite3


class Sales(SaveData):
    def __init__(self):
        super().__init__("./data/sales.db")
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _execute_query(self, query: str, params: tuple = ()) -> bool:
        try:
            with self.conn:
                self.conn.execute(query, params)
                return True
        except sqlite3.OperationalError:
            return False

    def _create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_table TEXT,
                food_order INTEGER,
                price FLOATING
        )"""
        self.conn.execute(query)

    def insert_data(
            self, name_table: str,
            food_order: int, price: float) -> bool:
        query = """
        INSERT INTO data(name_table, food_order, price)
        VALUES (?, ?, ?)
        """
        params = (name_table, food_order, price)
        return self._execute_query(query, params)


if __name__ == "__main__":
    ...
