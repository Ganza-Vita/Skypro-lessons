from typing import Any, Dict, Generator, List, Optional


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """Фильтрует транзакции по валюте."""
    if not transactions:
        return []

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Optional[Generator[str, None, None]]:
    """Возвращает описания транзакций, если они есть."""
    if not transactions:
        return

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        yield f"{number:016}"[:4] + " " + f"{number:016}"[4:8] + " " + f"{number:016}"[8:12] + " " + f"{number:016}"[
            12:16
        ]
