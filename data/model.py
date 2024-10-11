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
