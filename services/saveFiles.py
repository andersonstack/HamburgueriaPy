from abc import ABC, abstractmethod
import sqlite3


class SaveData(ABC):
    def __init__(self, name_file: str) -> None:
        self.db_path = name_file
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    @abstractmethod
    def _create_table(self) -> None:
        pass

    @abstractmethod
    def insert_data(self, *args) -> bool:
        pass

    def close_connection(self) -> None:
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
