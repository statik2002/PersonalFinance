import datetime
import json
from decimal import Decimal
from os import system, name
from classes import Wallet
from menu_function import clear, show_menu, input_operation_type, input_operation_date, input_operation_value, \
    input_description

wallet = Wallet()
cycleFlag = True
while cycleFlag:
    clear()
    operation = show_menu()

    if operation == 1:
        operation_type = input_operation_type()
        date = input_operation_date()
        value = input_operation_value()
        description = input_description()
        op = {'operation_item': operation_type, 'description': description, 'salary': value, 'date': date}
        wallet.add_operation(operation=op)
        print(f'Ваша операция с параметрами {op}')

    elif operation == 2:
        print(f'Ваш баланс операций: {wallet.get_balance()}')
        input('Нажмите любую клавишу для выхода в меню')

    elif operation == 3:
        wallet.show_operations()
        input('Нажмите любую клавишу для выхода в меню')

    elif operation == 4:
        wallet.save_operations()
        print('Bye bye!')
        cycleFlag = False
