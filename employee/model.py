from data.saveJson import SaveJson


class Employee:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.cpf = ""
        self.adress = ""
        self.phone = ""
        self.employee = SaveJson("funcionrios.json")
        self.load_employee = self.employee.load_json()

    def add_employee(
            self, name: str, cpf: str,
            age: int, adress: str, phone: str) -> None:
        ...

    def remove_employee(self, cpf: str) -> None:
        ...

    def edit_employee(self, cpf: str) -> None:
        ...
