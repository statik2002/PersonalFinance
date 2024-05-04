import re
from _pydecimal import Decimal
import datetime
from typing import List


class Date:
    def __get__(self, instance, owner=None):
        return self.value

    def __set__(self, instance, value):
        try:
            date = datetime.date.fromisoformat(value)
            self.value = date
        except ValueError:
            raise ValueError("Не правильный формат даты")


class Salary:
    def __get__(self, instance, owner=None):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(Decimal(value), Decimal):
            raise ValueError("Число не Decimal")
        self.value = value


class Description:
    def __get__(self, instance, owner=None):
        return self.value

    def __set__(self, instance, value):
        self.value = value


operation_type = ['PROFIT', 'EXPENSES']


class OperationItem:
    def __get__(self, instance, owner=None):
        return self.value

    def __set__(self, instance, value):
        if not value in operation_type:
            raise ValueError("Не верный тип операции")
        self.value = value


class Operation:

    operations = []

    operation_item = OperationItem()
    description = Description()
    salary = Salary()
    date = Date()

    def __init__(self, operation_item: str, date: str, description: str = "", salary: Decimal = 0.0):
        self.operation_item = operation_item
        self.date = date
        self.description = description
        self.salary = salary
        self.operations.append(self)


class Wallet:

    operations = []

    def __init__(self, db_path: str = 'db.txt'):
        self.db_path = db_path


    def add_operation(self, operation: dict):
        self.operations.append(Operation(**operation))
