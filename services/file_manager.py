import os
import pickle
from datetime import datetime
from typing import Dict, List

DATA = datetime.now().strftime("%d_%m_%Y")


class FileManager:
    def __init__(self, path: str, date: str | None = None) -> None:
        self.base_path = f"data/reports/{path}"
        self.date = f"data/reports/{path}/{date}.db"
        self.file = os.path.join(self.base_path, f"{DATA}.db")
        self.ensure_directory()

    def ensure_directory(self) -> None:
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def write_file(self, report: List[Dict[int, List]]) -> bool:
        try:
            with open(self.file, "ab") as arq:
                pickle.dump(report, arq)
                return True
        except FileNotFoundError:
            return False

    def read_file(self) -> List[Dict[int, List]] | bool:
        try:
            with open(self.date, "rb") as arq:
                x = pickle.load(arq)
                return x
        except FileNotFoundError:
            return False


if __name__ == "__main__":
    x = FileManager("sales", "17_10_2024")
    print(x.read_file())
