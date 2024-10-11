from data.model import SaveDatabase  # type: ignore
import sqlite3


class Employee(SaveDatabase):
    def __init__(self):
        super().__init__("./data/employee.json")
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf TEXT UNIQUE,
                    name TEXT UNIQUE,
                    address TEXT,
                    age INTEGER,
                    phone TEXT,
                    active BOOLEAN
            )
        """)

    def insert_data(
                    self,
                    cpf: str,
                    name: str,
                    address: str,
                    age: int,
                    phone: str) -> bool:
        if self._find_cpf(cpf):
            return False
        with self.conn:
            self.conn.execute("""
                INSERT INTO data(cpf, name, address, age, phone, active)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [cpf, name, address, age, phone, True])
        return True

    def remove_employee(self, cpf: str) -> bool:
        if self._find_cpf(cpf):
            with self.conn:
                self.conn.execute("""
                    UPDATE data
                    SET active = ?
                    WHERE cpf = ?
                """, [False, cpf])
                return True
        return False

    def _find_cpf(self, cpf: str) -> bool:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM data
                WHERE cpf = ?
            """, [cpf])
            return bool(cursor.fetchall())
