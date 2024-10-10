from data.saveJson import SaveJson


class Customer:
    def __init__(self):
        self.name = ""
        self.adress = ""
        self.customer = SaveJson("clientes.json")
        self.load_customer = self.customer.load_json()

    def add_customer(self, name: str, adress: str) -> None:
        cod = len(self.load_customer) + 1 if len(self.load_customer) > 0 else 1
        new_customer = {
            cod: [name, adress, True]
        }
        self.customer.modify_json(data=new_customer)

    def visualize_customer(self, cod: str) -> None:

        ...

    def remove_customer(self, cod: str) -> None:
        ...

    def update_customer(self, cod: str) -> None:
        ...

    def _verify_customer(self, cod: str) -> bool:
        if cod in self.load_customer:
            return True
        return False
