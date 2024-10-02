from src.generators import transaction_descriptions
from src.primery import transactions


def test_transactions_descriptions_1() -> None:
    generator_transactions = transaction_descriptions(transactions)
    expected_results = "Перевод организации"

    assert next(generator_transactions) == expected_results


def test_transactions_descriptions_2() -> None:
    generator_transactions = transaction_descriptions([])
    expected_results = []

    assert list(generator_transactions) == expected_results
