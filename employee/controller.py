from controller.inputs import (
    inputInt,
    inputStr,
    inputAdrs, inputt, inputPhone, inputCPF)
from employee.model import Employee
from employee.view import screen_employee
from employee.view import view_employee
from view.screens import clear, _basic
from view.styles import printS, printW


def edit() -> None:
    """
    Edits an existing employee.

    Asks the user for the employee's CPF and, if it exists,
    allows the user to edit their information. If not, prints an
    error message and goes back to the main menu.

    :return: None
    """

    cpf = inputCPF(" | CPF:\t")

    employee = Employee()
    employee_data = employee.visualize_employee(cpf)
    if employee_data is None:
        printW("> CPF não alcançado! <Enter> para continuar")
        input()
        employee.close_connection()
        return

    view_employee(employee_data)

    name = inputStr(" | Nome:\t")
    address = inputAdrs(" | Endereço:\t")
    age = inputInt(" | Idade:\t")
    phone = inputPhone(" | Telefone:\t")

    employee_edit = {
        cpf: [
            name if name != "" else employee_data[cpf][0],
            address if address != "" else employee_data[cpf][1],
            age if age != "" else employee_data[cpf][2],
            phone if phone != "" else employee_data[cpf][3],
        ]
    }
    employee.edit_employee(employee_edit, cpf)
    employee.close_connection()
    input()


def search() -> None:
    """
    Searches for a previously registered employee.

    Asks the user for the employee's CPF and, if it exists,
    allows the user to view their information. If not, prints an
    error message and goes back to the main menu.

    :return: None
    """

    cpf = inputCPF(" | CPF:\t")

    employee = Employee()
    employee_data = employee.visualize_employee(cpf)
    if employee_data is None:
        printW("> CPF não alcançado! <Enter> para continuar")
        employee.close_connection()
        input()
        return

    view_employee(employee_data)
    printS("> Enter para continuar")
    employee.close_connection()
    input()
    return


def visualize_all_employees() -> None:
    """
    Visualize all previously registered employees.

    :return: None
    """

    _basic("Todos os funcionários")
    employee = Employee()
    employee_data = employee.visualize_all_employee()
    if len(employee_data) == 0:
        printW("> Nenhum funcionário encontrado! <Enter> para continuar")
        employee.close_connection()
        input()
        return

    view_employee(employee_data)
    printW("> Enter para continuar")
    employee.close_connection()
    input()


def delete() -> None:
    """
    Deletes a previously registered employee.

    Asks the user for the employee's CPF and, if it exists,
    removes the employee from the system. If not, prints an
    error message and goes back to the main menu.

    :return: None
    """

    _basic("Deletando funcionário")

    cpf = inputCPF("CPF:\t")

    contract = Employee()
    if not contract.update_employee(cpf):
        printW(f"{cpf} não alcançado!")
        input()
        return

    printS(f"{cpf} desligado do sistema!")
    input()


def new_employee() -> None:
    """
    Adds a new employee to the system.

    Asks the user for the employee's name, age, CPF, address and phone.
    If the CPF is unique, the employee is added to the system.
    If not, an error message is printed and the user is returned to
    the main menu.

    :return: None
    """

    _basic("Adicionando novo funcionário")

    name = inputStr("Nome:\t")
    age = inputInt("Idade:\t")
    cpf = inputCPF("CPF:\t")
    address = inputAdrs("Endereço:\t")
    phone = inputPhone("Telefone:\t")

    contract = Employee()
    if not contract.insert_data(
                            name=name,
                            age=age,
                            cpf=cpf,
                            address=address,
                            phone=phone
                    ):
        printW(f"{cpf} já foi registrado! Deseja ativa-lo ?")
        option = inputStr("Sim/Não:\t").lower()
        if option.startswith("s"):
            printS(f"{cpf} ativado!")
            contract.update_employee(cpf)
        else:
            printW("Operação cancelada!\n")
        contract.close_connection()
        input()
        return

    printS(f"{name} foi adicionado ao sistema com sucesso!")
    contract.close_connection()
    input()


def main_employee() -> None:
    """
    Main function of the employee module.

    Runs an infinite loop that calls the employee screen
    reads the user's option and executes the corresponding action,
    which can be:

    1. Add a new employee to the system
    2. View all employees
    3. Search for an employee
    4. Remove an employee from the system
    5. Edit an existing employee
    0. Go back to the main menu

    :return: None
    """
    while True:
        clear()
        screen_employee()
        option = inputt("")

        match option:
            case '1':
                new_employee()
            case '2':
                visualize_all_employees()
            case '3':
                search()
            case '4':
                delete()
            case '5':
                edit()
            case '0':
                clear()
                return


if __name__ == "__main__":
    main_employee()
