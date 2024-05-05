import re
from _pydecimal import Decimal
import datetime
from typing import List


operation_type = ['PROFIT', 'EXPENSES']


class Operation:

    def __init__(self, operation_item: str, date: str, description: str = "", salary: Decimal = 0.0):
        self.operation_item = operation_item
        self.date = date
        self.description = description
        self.salary = salary

    @property
    def operation_item(self):
        return self._operation_item

    @operation_item.setter
    def operation_item(self, value):
        if value not in operation_type:
            raise ValueError("Не верный тип операции")
        self._operation_item = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        try:
            date = datetime.date.fromisoformat(value)
            self._date = value
        except ValueError:
            raise ValueError("Не правильный формат даты")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(Decimal(value), Decimal):
            raise ValueError(f'Число {value} не Decimal')
        if Decimal(value) < 0:
            raise ValueError(f'Число сумма операции = [{value}] не может быть меньше 0')
        self._salary = Decimal(value)


class Wallet:
    operations: list = []

    def __init__(self, db_path: str = 'db.txt'):
        self.db_path = db_path

    @staticmethod
    def add_operation(operation: dict):
        Wallet.operations.append(Operation(**operation))

    def get_balance(self):
        total = 0
        for operation in self.operations:
            if operation.operation_item == 'PROFIT':
                total += operation.salary
            elif operation.operation_item == 'EXPENSES':
                total -= operation.salary

        return total
