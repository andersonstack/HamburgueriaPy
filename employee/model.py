from data.saveJson import SaveJson
from employee.view import view_employee


class Employee:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.cpf = ""
        self.adress = ""
        self.phone = ""
        self.employee = SaveJson("funcionarios.json")
        self.load_employee = self.employee.load_json()

    def add_employee(
            self, name: str, cpf: str,
            age: int, adress: str, phone: str) -> bool:

        if not self._verify_cpf(cpf):
            new_employee = {
                cpf: [
                    name,
                    age,
                    adress,
                    phone,
                    True
                ]
            }
            self.employee.modify_json(data=new_employee)
            return True
        else:
            print("Dados do funcionários pré-existentes")
            active = input("Pressione <S> para ativar o cadastro\n")
            if active.upper() in 'S':
                self.load_employee[cpf][-1] = True
                self.employee.update_json(self.load_employee)
                return True
            return False

    def remove_employee(self, cpf: str) -> bool:
        if self._verify_cpf(cpf):
            for keys in self.load_employee:
                if cpf == keys:
                    for details in self.load_employee[keys]:
                        self.load_employee[cpf][-1] = False
                        self.employee.update_json(self.load_employee)
                        return True
        return False

    def visualize_employees(self) -> None:
        view_employee(self.load_employee)

    def edit_employee(self, cpf: str) -> bool:
        if self._verify_cpf(cpf):
            employee_details = self.load_employee[cpf]

            print(f"Nome atual: {employee_details[0]}")
            print(f"Idade atual: {employee_details[1]}")
            print(f"Endereço atual: {employee_details[2]}")
            print(f"Telefone atual: {employee_details[3]}")

            print("Informações em branco permancem inalteradas\n")
            name = input("Novo nome:\t")
            age = input("Nova idade:\t")
            adress = input("Novo endereço:\t")
            phone = input("Novo telefone:\t")

            updated_employee = {
                cpf: [
                    name if name else employee_details[0],
                    int(age) if age else employee_details[1],
                    adress if adress else employee_details[2],
                    phone if phone else employee_details[3],
                    True
                ]
            }

            self.employee.update_json(data=updated_employee)
            return True

        return False

    def search_employee(self, cpf: str) -> bool:
        if self._verify_cpf(cpf):
            employee = {
                cpf: self.load_employee[cpf]
            }
            view_employee(employee)
            return True
        return False

    def _verify_cpf(self, cpf: str) -> bool:
        if cpf in self.load_employee:
            return True
        return False
