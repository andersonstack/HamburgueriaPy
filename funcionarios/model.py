from data.saveJson import SaveJson


class Funcionarios:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.cpf = ""
        self.adress = ""
        self.phone = ""
        self.funcionarios = SaveJson("funcionrios.json")
        self.load_funcionarios = self.funcionarios.load_json()

    def add_employee(
            self, name: str, cpf: str,
            age: int, adress: str, phone: str) -> None:
        ...

    def remove_employee(self, cpf: str) -> None:
        ...

    def edit_employee(self, cpf: str) -> None:
        ...
