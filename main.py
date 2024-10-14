from view import screens
from controller.inputs import inputt
from warehouse.controller import main_warehouse
from employee.controller import main_employee
from menu.controller import main_menu


get_out = False

while not get_out:
    screens.screen_main()
    option = inputt("")

    match option:
        case '1':
            main_warehouse()
        case '2':
            main_employee()
        case '3':
            main_menu()
        case '4':
            screens.screen_report()
        case '5':
            screens.screen_sales()
        case '6':
            screens.screen_infor()
        case '0':
            print("Obrigado por usar o programa! :)\n")
            get_out = True
            break
        case _:
            print("Opção inválida...\n")
