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
