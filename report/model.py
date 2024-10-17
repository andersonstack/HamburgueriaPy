from services.file_manager import FileManager, DATA
from report.view import view_reports


class Reports:
    def __init__(self, path: str, data: str | None = None):
        self.data = data if data else DATA
        self.path = path

    def show_reports(self):
        arq = FileManager(self.path, self.data)
        read = arq.read_file()
        if read:
            view_reports(read, self.data.replace("_", "/"))
        else:
            print("Relatório não encontrado!")


if __name__ == "__main__":
    x = Reports("warehouse")
    x.show_reports()
