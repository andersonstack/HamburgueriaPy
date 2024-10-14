from view import screens
from warehouse.controller import main_warehouse
from employee.controller import main_employee


get_out = False

while not get_out:
    screens.screen_main()
    option = input("")

    match option:
        case '1':
            main_warehouse()
        case '2':
            main_employee()
        case '3':
            ...
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
