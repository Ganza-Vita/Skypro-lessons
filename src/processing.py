from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Функция фильтрует операции по состоянию
    """
