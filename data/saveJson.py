import sqlite3
from abc import ABC, abstractmethod


class SaveData(ABC):
    def __init__(self, name_file: str) -> None:
        self.db_path = f"./data/{name_file}.db"
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    @abstractmethod
    def create_table(self) -> None:
        pass

    @abstractmethod
    def insert_data(
                    self,
                    cpf: str,
                    name: str,
                    address: str,
                    age: int,
                    phone: str) -> None:
        pass

    @abstractmethod
    def update_data(self, cpf: str) -> None:
        pass


class SaveEmployee(SaveData):
    def __init__(self, name_file: str) -> None:
        """
        Constructor method.

        Parameters:
        name_file (str): The name of the SQLite file to be created

        Initialize the SaveWarehouse class with the following attributes:
        - db_path (str): The path to the SQLite file
        - conn (sqlite3.Connection): The connection to the SQLite file
        """
        super().__init__(name_file)

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
                    phone: str) -> None:

        with self.conn:
            self.conn.execute("""
                INSERT INTO data(cpf, name, address, age, phone, active)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [cpf, name, address, age, phone, True])

    def update_data(self, cpf: str) -> None:
        with self.conn:
            self.conn.execute("""
                UPDATE data
                SET active = ?
                WHERE cpf = ?
            """, [False, cpf])


if __name__ == "__main__":
    db = SaveEmployee("funcionarios")
    # db.create_table()
    # db.insert_data(
    #     cpf="13321600420",
    #     name="Anderson",
    #     address="Rua São José",
    #     age=22,
    #     phone="8499910"
    # )
    db.update_data(cpf="13321600420")
    db.update_data(cpf="11111111111")
