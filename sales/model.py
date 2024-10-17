from services.saveFiles import SaveData
from sales.view import view_sales
from services.file_manager import FileManager
from typing import Dict, List
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
                price REAL
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
            else:
                print("Sem vendas!")

    def fetch_one_sales(self, cod: int) -> None:
        query = """
        SELECT * FROM data
        WHERE id = ?
        """
        with self.conn:
            try:
                cursor = self.conn.execute(query, (cod,))
                sales = cursor.fetchone()
                if sales:
                    dict_pedido = {
                        sales[0]: [sales[1], sales[2], sales[3]]
                    }
                    view_sales(dict_pedido)
                else:
                    print("Código não alcançado!")
            except sqlite3.OperationalError:
                print("Erro de banco de dados")

    def close_sales(self) -> bool:
        query = """
        SELECT * FROM data
        """

        delete_query = """
        DROP TABLE IF EXISTS data
        """

        with self.conn:
            try:
                cursor = self.conn.execute(query)
                sales = cursor.fetchall()
                dict_sales = [{
                    i[0]: [i[2], i[3]] for i in sales
                }]

                self._write_report(dict_sales)

                self.conn.execute(delete_query)

                return True
            except sqlite3.OperationalError:
                return False

    def _write_report(self, sales: List[Dict[int, List]]) -> None:
        report = FileManager("sales")
        report.write_file(sales)


if __name__ == "__main__":
    x = Sales()
    y = x.close_sales()
