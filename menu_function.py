import decimal
from decimal import Decimal
from os import system, name
import datetime
from classes import operation_type, Wallet

menu_items = [
    '1. Ввод операции',
    '2. Показать баланс',
    '3. Показать все операции',
    '4. Редактировать операцию',
    '5. Поиск операции',
    '6. Выход'
]


def clear() -> None:
    """
    Функция очистки экрана
    :return: None
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def input_operation_type(prev: str = '') -> str:
    """
    Функция обрабатывает и валидирует ввод типа операции
    :param prev: Указываем пред идущее значение редактируемой операции ввода типа операции
    :return: Значение типа операции
    """
    while True:
        clear()
        inp = ''
        if prev:
            print(f'Тип операции до редактирования: {prev}')
        inp = input('Введите тип операции:\n1. Доход\n2. Расход\n: ')
        if not inp.isdigit():
            print('Вы ввели не число. Нажмите любую клавишу для вывода меню')
            input()
            continue
        if inp not in ['1', '2']:
            print(
                'Вы ввели неправильный пункт меню.'
                'Нажмите любую клавишу для вывода меню'
            )
            input()
            continue
        else:
            return operation_type[int(inp)-1]


def input_description(prev: str = '') -> str:
    """
    Ввод описания операции
    :param prev: Значение пред идущего описания при редактировании
    :return: Значение описания операции
    """
    clear()
    if prev:
        print(f'Описание операции до редактирования: {prev}')
    return input('Введите описание операции: ')


def input_operation_value(prev: decimal = None) -> Decimal:
    """
    Поучение и валидация суммы операции
    :param prev: Пред идущее значение суммы операции при редактировании
    :return: Сумма операции
    """
    while True:
        clear()
        if prev:
            print(f'Сумма операции до редактирования: {prev}')
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


def input_operation_date(prev: str = '') -> str:
    """
    Получение и валидация даты операции
    :param prev: Пред идущее значение даты операции при редактировании
    :return: Дата операции
    """
    while True:
        clear()
        if prev:
            print(f'Дата операции до редактирования: {prev}')
        date = input('Введите дату операции (ГГГГ-ММ-ДД): ')
        try:
            datetime.date.fromisoformat(date)
            return date
        except ValueError:
            print('Введенная дата не соответствует образцу (ГГГГ-ММ-ДД)')


def show_menu() -> int:
    """
    Показ и обработка основного меню
    :return: Выбранный пункт меню
    """
    while True:
        clear()
        menu = "\n".join(menu_items)
        operation = input(f'Введите номер операции:\n{menu}\n')
        if not operation.isdigit():
            print('Вы ввели не число. Нажмите любую клавишу для вывода меню')
            input()
            continue
        if 0 < int(operation) > len(menu_items)+1:
            print(
                'Вы ввели неправильный пункт меню.'
                'Нажмите любую клавишу для вывода меню'
            )
            input()
            continue

        return int(operation)


def edit_operation_menu(wallet: Wallet) -> None:
    """
    Подменю редактирования операции
    :param wallet: Передаем экземпляр кошелька
    :return: None
    """
    while True:
        clear()
        operation_id = input('Введите id операции: ')

        if not operation_id.isdigit() and 1 > int(operation_id) > len(wallet.operations):
            print('Введен неправильный id операции')
            input('Для нового ввода id операции, нажмите любую клавишу')

        else:
            type_operation = input_operation_type(
                wallet.operations[int(operation_id)].operation_item
            )
            date = input_operation_date(
                wallet.operations[int(operation_id)].date
            )
            value = input_operation_value(
                wallet.operations[int(operation_id)].salary
            )
            description = input_description(
                wallet.operations[int(operation_id)].description
            )
            wallet.change_operation(
                int(operation_id), {
                    'operation_item': type_operation,
                    'description': description,
                    'salary': value,
                    'date': date
                }
            )
            break


def remove_operation_menu(wallet: Wallet) -> None:
    """
    Меню удаления операции
    :param wallet: Получаем экземпляр кошелька
    :return: None
    """
    while True:
        clear()
        operation_id = input('Введите id операции: ')

        if not operation_id.isdigit() and 1 > int(operation_id) > len(wallet.operations):
            print('Введен неправильный id операции')
            input('Для нового ввода id операции, нажмите любую клавишу')

        else:
            wallet.operations.pop(int(operation_id))
            break


def search_query_menu(search_type: str) -> str:
    """
    Меню поиска
    :param search_type: Получаем по какому параметру будем производить поиск
    :return: сам запрос в зависимости от параметра поиска
    """
    if search_type == 'op_type':
        return input_operation_type()

    elif search_type == 'date':
        return input_operation_date()

    elif search_type == 'value':
        return str(input_operation_value())
