from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция фильтрует операции по состоянию.
    """

    filtered_operations = []

    for operation in operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)

    return filtered_operations


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Функция сортирует операции по дате.
    """

    sorted_operations = sorted(
        operations, key=lambda operation: operation.get("date", "Дата не введена"), reverse=reverse
    )

    return sorted_operations
