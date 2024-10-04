from view.screens import clear, _basic
from employee.view import screen_employee
from controller.inputs import inputInt
from employee.model import Employee
from view.styles import printS, printW


def new_employee():
    _basic("Adicionando novo funcionário")

    name = input("Nome:\t")
    age = inputInt("Idade:\t")
    cpf = input("CPF:\t")
    adress = input("Endereço:\t")
    phone = input("Telefone:\t")

    contract = Employee()
    if not contract.add_employee(
                            name=name,
                            age=age,
                            cpf=cpf,
                            adress=adress,
                            phone=phone
                    ):
        printW(f"Não foi possível adicionar {cpf} ao sistema. CPF já existe!")
        return

    printS(f"{name} foi adicionado ao sistema com sucesso!")
    input()


def main_employee() -> None:
    while True:
        clear()
        screen_employee()
        option = input("")

        match option:
            case '1':
                new_employee()
            case '2':
                ...
            case '3':
                ...
            case '4':
                ...
            case '5':
                ...
            case '0':
                return
