from decimal import Decimal


operation_type = ['Доход', 'Расход']


class Operation:

    def __init__(self, operation_item: str, date: str, description: str = "", salary: Decimal = 0.0) -> None:
        self.operation_item = operation_item
        self.date = date
        self.description = description
        self.salary = salary

    def __str__(self) -> str:
        return f'{self.operation_item};{self.date};{self.description};{self.salary}'

    def show(self) -> list:
        return [self.operation_item, self.date, str(self.salary), self.description]



class Wallet:
    operations: list = []

    def __init__(self, db_path: str = 'db.txt') -> None:
        self.db_path = db_path
        self.operations = self.load_operations()

    def add_operation(self, operation: dict) -> None:
        self.operations.append(Operation(**operation))

    def get_balance(self) -> Decimal:
        total: Decimal = Decimal(0.0)
        if len(self.operations) < 1:
            return Decimal(0.0)
        for operation in self.operations:
            if operation.operation_item == operation_type[0]:
                total += operation.salary
            elif operation.operation_item == operation_type[1]:
                total = total - operation.salary

        return total

    def save_operations(self) -> None:
        with open(self.db_path, 'w') as f:
            for operation in self.operations:
                f.write(f'{operation.__str__()}\n')

    def load_operations(self) -> list:
        operations = []
        with open(self.db_path, 'r') as f:
            ops = f.readlines()
            for line in ops:
                operation = line.split(';')
                print(operation)
                operations.append(Operation(operation[0], operation[1], operation[2], Decimal(operation[3])))

        return operations

    def show_operations(self) -> None:
        if len(self.operations) < 1:
            print('У вас нет операций')
            return
        max_columns = []
        operations = [operation.show() for operation in self.operations]
        for col in zip(*operations):
            len_el = []
            [len_el.append(len(el)) for el in col]
            max_columns.append(max(len_el))

        columns = ['id', 'Тип операции', 'Дата операции', 'Сумма операции', 'Описание']
        for column in columns:
            print(f'{column:{max(max_columns) + 5}}', end='')
        print()
        print(f'{"=" * max(max_columns) * 5}')

        for index,operation in enumerate(operations):
            operation = [str(index)] + operation
            for column in operation:
                print(f'{column:{max(max_columns) + 5}}', end='')
            print()