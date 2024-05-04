from classes import Wallet, OperationItem, Operation

wallet = Wallet()

wallet.add_operation({'operation_item': 'PROFIT', 'description': 'No description', 'salary': 1500.00, 'date': '2024-05-03'})
wallet.add_operation({'operation_item': 'EXPENSES', 'description': 'No description', 'salary': 300.50, 'date': '2024-05-03'})
for operation in Wallet.operations:
    print(operation.salary)