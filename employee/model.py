from data.saveFiles import SaveData
from typing import Dict, Optional
import sqlite3


class Employee(SaveData):
    def __init__(self):
        super().__init__("./data/funcionarios.db")
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

    def update_employee(self, cpf: str) -> bool:
        current_status = self._find_cpf(cpf)

        if current_status is not None:
            new_status = not current_status[0][6]

            if self._find_cpf(cpf):
                with self.conn:
                    self.conn.execute("""
                        UPDATE data
                        SET active = ?
                        WHERE cpf = ?
                    """, [new_status, cpf])
                    return True
        return False

    def _find_cpf(self, cpf: str):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM data
                WHERE cpf = ?
            """, [cpf])
            return cursor.fetchall()

    def visualize_employee(self, cpf: str) -> Optional[Dict[str, list]]:
        cursor = self._find_cpf(cpf)

        if cursor:
            employee_data = cursor[0]

            employee = {
                employee_data[1]: [
                    employee_data[2],
                    employee_data[3],
                    employee_data[4],
                    employee_data[5]]
            }
            return employee

        return None

    def visualize_all_employee(self) -> Dict:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM data
            """)

            employee_data = cursor.fetchall()
            all_employe = {}
            for employe in employee_data:
                employe_ = {
                    employe[1]: [
                        employe[2],
                        employe[3],
                        employe[4],
                        employe[5]]
                }
                all_employe.update(employe_)
            return all_employe

    def edit_employee(self, data: Dict[str, list], cpf: str) -> None:
        name, address, age, phone = data[cpf]
        with self.conn:
            self.conn.execute("""
                UPDATE data
                SET name = ?, address = ?, age = ?, phone = ?
                WHERE cpf = ?
            """, (name, address, age, phone, cpf))


if __name__ == '__main__':
    x = Employee()
    x.visualize_employee("13321600420")
