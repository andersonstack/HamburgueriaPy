from data.saveJson import SaveJson
from employee.view import view_employee


class Employee:
    def __init__(self) -> None:
        """
        Constructor method.

        Parameters:
        self (Employee): The instance of the class

        Initialize the Employee class with the following attributes:
        - name (str): The name of the employee
        - age (str): The age of the employee
        - cpf (str): The CPF of the employee
        - adress (str): The address of the employee
        - phone (str): The phone of the employee
        - employee (SaveJson): The SaveJson object to save and load the data
        - load_employee (Dict[str, Any]): The dictionary with the data of all
        the employees
        """
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

        """
        Adds a new employee to the system.

        Parameters:
        name (str): The name of the employee
        cpf (str): The CPF of the employee
        age (int): The age of the employee
        adress (str): The address of the employee
        phone (str): The phone of the employee

        Returns:
        bool: True if the employee was added successfully, False otherwise
        """
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
        """
        Removes an employee from the system.

        Parameters:
        cpf (str): The CPF of the employee to be removed

        Returns:
        bool: True if the employee was removed successfully, False otherwise
        """
        if self._verify_cpf(cpf):
            for keys in self.load_employee:
                if cpf == keys:
                    for details in self.load_employee[keys]:
                        self.load_employee[cpf][-1] = False
                        self.employee.update_json(self.load_employee)
                        return True
        return False

    def visualize_employees(self) -> None:
        """
        Visualizes all the employees in the system.

        :return: None
        """
        view_employee(self.load_employee)

    def edit_employee(self, cpf: str) -> bool:
        """
        Edits an existing employee in the system.

        Parameters:
        cpf (str): The CPF of the employee to be edited

        Returns:
        bool: True if the employee was edited successfully, False otherwise
        """
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
        """
        Searches for an existing employee in the system.

        Parameters:
        cpf (str): The CPF of the employee to be searched

        Returns:
        bool: True if the employee was found, False otherwise
        """
        if self._verify_cpf(cpf):
            employee = {
                cpf: self.load_employee[cpf]
            }
            view_employee(employee)
            return True
        return False

    def _verify_cpf(self, cpf: str) -> bool:
        """
        Verifies if a given CPF exists in the system.

        Parameters:
        cpf (str): The CPF of the employee to be verified

        Returns:
        bool: True if the CPF exists, False otherwise
        """
        if cpf in self.load_employee:
            return True
        return False
