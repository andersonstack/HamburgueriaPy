from data.saveFiles import SaveData
from sales.view import view_sales
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

    def fetch_all_sales(self) -> None:
        query = """
            SELECT * FROM data
        """
        with self.conn:
            cursor = self.conn.execute(query)
            result = cursor.fetchall()
            if result:
                dict_sales = {
                    i[0]: [i[1], i[2], i[3]] for i in result
                }
                view_sales(dict_sales)

    def fetch_one_sales(self, cod: int) -> None:
        query = """
        SELECT * FROM data
        WHERE id = ?
        """
        with self.conn:
            try:
                cursor = self.conn.execute(query, (cod,))
                pedido = cursor.fetchone()
                dict_pedido = {
                    pedido[0]: [pedido[1], pedido[2], pedido[3]]
                }
                view_sales(dict_pedido)
            except sqlite3.OperationalError:
                print("Código não alcançado!")


if __name__ == "__main__":
    x = Sales()
    x.fetch_one_sales(2)
