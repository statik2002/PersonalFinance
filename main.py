from classes import Wallet

wallet = Wallet()

#try:
#    wallet.add_operation(operation={'operation_item': 'PROFIT', 'description': 'No description', 'salary': 1500.00, 'date': '2024-05-20'})
#    wallet.add_operation(operation={'operation_item': 'EXPENSES', 'description': 'No description', 'salary': 300.50, 'date': '2024-05-03'})
#    wallet.add_operation(operation={'operation_item': 'PROFIT', 'description': 'No description', 'salary': -45, 'date': '2024-05-03'})
#except ValueError as error:
#    print(error)


#for operation in Wallet.operations:
#    print(operation.operation_item, operation.salary, operation.date)

flag = True

while flag:
    operation = int(input('Введите номер операции:\n1. Ввод операции\n2.Показать баланс\n3. Выход\n'))

    if operation == 1:
        input_operation = input('Введите операцию в виде [PROFIT\EXPENSES, Описание, Сумма, Дата]').split(',')
        wallet.add_operation(operation={
            'operation_item': input_operation[0],
            'description': input_operation[1],
            'salary': input_operation[2],
            'date': input_operation[3].strip()
        })
    elif operation == 2:
        print(f'Ваш баланс операций: {wallet.get_balance()}')
    elif operation == 3:
        print('Bye bye!')
        flag = False
