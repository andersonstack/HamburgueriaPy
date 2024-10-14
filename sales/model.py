from data.saveFiles import SaveData


class Sales(SaveData):
    def __init__(self, name_file):
        super().__init__("./data/sales.db")

    def create_table(self):
        return super().create_table()()

    def insert_data(self, *args):
        return super().insert_data(*args)


if __name__ == "__main__":
    sales = Sales("sales.db")
    sales.create_table()
