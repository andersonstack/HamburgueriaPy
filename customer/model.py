class Customer:
    def __init__(self):
        self.name = ""
        self.adress = ""

    def add_customer(self, name: str, adress: str) -> None:
        ...

    def visualize_customer(self, cod: str) -> None:
        ...

    def remove_customer(self, cod: str) -> None:
        ...

    def update_customer(self, cod: str) -> None:
        ...
