import argparse

from classes import Wallet
from menu_function import (
    clear, show_menu, input_operation_type,
    input_operation_date, input_operation_value,
    input_description, edit_operation_menu,
    remove_operation_menu, search_query_menu)


def main() -> None:
    """
    Main function. Launch main.py --p 'db.txt'
    :return: None
    """
    parser = argparse.ArgumentParser(
        description='Скрипт для ведения личных финансов'
    )
    parser.add_argument(
        '--p',
        help='Путь к файлу с базой данных',
        default='db.txt'
    )
    args = parser.parse_args()
    db_path = args.p

    wallet = Wallet(db_path=db_path)
    cycle_flag = True
    while cycle_flag:
        clear()
        operation = show_menu()

        if operation == 1:
            operation_type = input_operation_type()
            date = input_operation_date()
            value = input_operation_value()
            description = input_description()
            op = {
                'operation_item': operation_type,
                'description': description,
                'salary': value,
                'date': date
            }
            wallet.add_operation(operation=op)

        elif operation == 2:
            print(f'Ваш баланс операций: {wallet.get_balance()}')
            input('Нажмите любую клавишу для выхода в меню')

        elif operation == 3:
            wallet.show_operations()
            input('Нажмите любую клавишу для выхода в меню')

        elif operation == 4:
            while True:
                clear()
                print(
                        '1. Редактировать операцию.\n2. Удалить операцию.\n3.'
                        'В основное меню.\n'
                      )
                operation_id = input('Введите id операции: ')
                if not operation_id.isdigit() and 1 > int(operation_id) > 3:
                    print('Введен неправильный пункт меню.')
                    input('Для ввода снова, нажмите любую клавишу')
                    continue
                if operation_id == '1':
                    edit_operation_menu(wallet)
                    break
                elif operation_id == '2':
                    remove_operation_menu(wallet)
                    break
                elif operation_id == '3':
                    break

        elif operation == 5:
            while True:
                clear()
                print('1. Поиск по типу операции.\n2. Поиск по дате операции.\n3.'
                      ' Поиск по сумме опрации.\n4. Выход в основное меню\n')
                menu_item = input('Введите пункт меню: ')
                if not menu_item.isdigit() and 1 > int(menu_item) > 4:
                    print('Введен неправильный пункт меню.')
                    input('Для ввода снова, нажмите любую клавишу')
                    continue
                if menu_item == '1':
                    search_operation = search_query_menu('op_type')
                    search_result = wallet.search('op_type', search_operation)
                    wallet.show_operations(search_result)
                    input('Для выхода в основное меню нажмите любую клавишу')
                    break
                elif menu_item == '2':
                    search_date = search_query_menu('date')
                    search_result = wallet.search('date', search_date)
                    wallet.show_operations(search_result)
                    input('Для выхода в основное меню нажмите любую клавишу')
                    break
                elif menu_item == '3':
                    search_value = search_query_menu('value')
                    search_result = wallet.search('value', search_value)
                    wallet.show_operations(search_result)
                    input('Для выхода в основное меню нажмите любую клавишу')
                    break
                elif menu_item == '4':
                    break

        elif operation == 6:
            wallet.save_operations()
            print('Пока пока!')
            cycle_flag = False


if __name__ == '__main__':
    main()
