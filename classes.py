from decimal import Decimal


operation_type = ['Доход', 'Расход']


class Operation:

    def __init__(
            self,
            operation_item: str,
            date: str,
            description: str = "",
            salary: Decimal = 0.0) -> None:
        self.operation_item = operation_item
        self.date = date
        self.description = description
        self.salary = salary

    def __str__(self) -> str:
        return f'{self.operation_item};{self.date};{self.description};{self.salary}'

    def show(self) -> list:
        """
        Вывод операции как список
        :return: Операция в виде списка
        """
        return [self.operation_item, self.date, str(self.salary), self.description]


class Wallet:
    operations: list = []

    def __init__(self, db_path: str = 'db.txt') -> None:
        self.db_path = db_path
        self.operations = self.load_operations()

    def add_operation(self, operation: dict) -> None:
        """
        Добавление операции в кошелек
        :param operation: Операция в виде словаря
        :return: None
        """
        self.operations.append(Operation(**operation))

    def change_operation(self, operation_id: int, operation: dict) -> None:
        """
        Замена операции при редактировании
        :param operation_id: id операции
        :param operation: Отредактированная операция в виде списка
        :return: None
        """
        self.operations[operation_id] = Operation(**operation)

    def get_balance(self) -> Decimal:
        """
        Вывод баланса кошелька
        :return: Общая сумма
        """
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
        """
        Сохранение операций в файл
        :return: None
        """
        with open(self.db_path, 'w') as f:
            for operation in self.operations:
                f.write(f'{operation.__str__()}\n')

    def load_operations(self) -> list:
        """
        Загрузка операций из файла
        :return: Список операций
        """
        operations = []
        try:
            with open(self.db_path, 'r') as f:
                ops = f.readlines()
                for line in ops:
                    operation = line.split(';')
                    print(operation)
                    operations.append(
                        Operation(
                            operation[0],
                            operation[1],
                            operation[2],
                            Decimal(operation[3])
                        )
                    )
                return operations
        except IOError:
            return []

    def show_operations(self, operations: list = None) -> None:
        """
        Вывод таблицы с операциями
        :param operations: Список операций
        :return: None
        """
        if not operations:
            operations = self.operations
        if len(operations) < 1:
            print('У вас нет операций')
            return
        max_columns = []
        show_operations = [operation.show() for operation in operations]
        for col in zip(*show_operations):
            len_el = []
            [len_el.append(len(el)) for el in col]
            max_columns.append(max(len_el))

        columns = [
            'id',
            'Тип операции',
            'Дата операции',
            'Сумма операции',
            'Описание'
        ]
        for column in columns:
            print(f'{column:{max(max_columns) + 5}}', end='')
        print()
        print(f'{"=" * max(max_columns) * 10}')

        for index, operation in enumerate(show_operations):
            operation = [str(index)] + operation
            for column in operation:
                print(f'{column:{max(max_columns) + 5}}', end='')
            print()

    def delete_operation(self, operation_id) -> None:
        """
        Удаление операции из кошелька
        :param operation_id: id операции
        :return: None
        """
        self.operations.pop(operation_id-1)

    def search(self, field: str, query: str) -> list:
        """
        Поиск операций по параметру и строке поиска
        :param field: Параметр поиска ('op_type', 'date', 'value') По типу операции, по дате, по сумме
        :param query: Непосредственно сам запрос поиска
        :return: Список операций подходящих по запросу
        """
        if field == 'op_type':
            if query not in operation_type:
                return ['Не правильный запрос по типу операции']
            return [operation for operation in self.operations if operation.operation_item == query]
        elif field == 'date':
            return [operation for operation in self.operations if operation.date == query]
        elif field == 'value':
            return [operation for operation in self.operations if operation.salary == Decimal(query)]
