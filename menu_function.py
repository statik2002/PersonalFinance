import decimal
from decimal import Decimal
from os import system, name
import datetime
from classes import operation_type



menu_items = ['1. Ввод операции', '2. Показать баланс', '3. Показать все операции', '4. Выход']

def clear() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def input_operation_type() -> str:
    while True:
        clear()
        inp = ''
        inp = input('Введите тип операции:\n1. Доход\n2.Расход ')
        if not inp.isdigit():
            print('Вы ввели не число. Нажмите любую клавишу для вывода меню')
            input()
            continue
        if not inp in ['1', '2']:
            print('Вы ввели неправильный пункт меню. Нажмите любую клавишу для вывода меню')
            input()
            continue
        else:
            return operation_type[int(inp)-1]

def input_description() -> str:
    clear()
    return input('Введите описание операции: ')

def input_operation_value() -> Decimal:
    while True:
        clear()
        value = ''
        try:
            value = Decimal(input('Введите сумму операции: '))
        except decimal.InvalidOperation:
            print('Введенная сумма не соответствует требованиям (0.00)')
            input('Нажмите на любую клавишу что бы заново ввести сумму')
            continue
        if not isinstance(Decimal(value), Decimal):
            print('Введенная сумма не соответствует требованиям (0.00)')
            input('Нажмите на любую клавишу что бы заново ввести сумму')
            continue
        elif Decimal(value) < 0:
            print('Введенная сумма не должна быть меньше ноля')
            input('Нажмите на любую клавишу что бы заново ввести сумму')
            continue
        else:
            return Decimal(value)

def input_operation_date() -> str:
    while True:
        clear()
        date = ''
        date = input('Введите дату операции (ГГГГ-ММ-ДД):')
        try:
            datetime.date.fromisoformat(date)
            return date
        except ValueError:
            print('Введенная дата не соответствует образцу (ГГГГ-ММ-ДД)')

def show_menu() -> int:
    while True:
        clear()
        menu = "\n".join(menu_items)
        operation = input(f'Введите номер операции:\n{menu} ')
        if not operation.isdigit():
            print('Вы ввели не число. Нажмите любую клавишу для вывода меню')
            input()
            continue
        if 0 < int(operation) > len(menu_items)+1:
            print('Вы ввели неправильный пункт меню. Нажмите любую клавишу для вывода меню')
            input()
            continue

        return int(operation)
