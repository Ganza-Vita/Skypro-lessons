from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Функция фильтрует операции по состоянию.
    """

    filtered_operations = []

    for operation in operations:
        if operation.get('state') == state:
            filtered_operations.append(operation)

    return filtered_operations