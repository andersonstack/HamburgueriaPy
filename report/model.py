from services.file_manager import FileManager, DATA
from report.view import view_reports
import os


class Reports:
    def __init__(self, path: str, data: str | None = None):
        self.data = data if data else DATA
        self.path = os.path.join(path, self.data)

    def show_reports(self):
        arq = FileManager("sales", self.data)
        read = arq.read_file()
        if read:
            view_reports(read, self.data.replace("_", "/"))


if __name__ == "__main__":
    x = Reports("sales", "17_10_2024")
    x.show_reports()
