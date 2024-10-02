from src.primery import transactions

from src.generators import transaction_descriptions

import pytest



def test_transactions_descriptions_1():
    generator_transactions = transaction_descriptions(transactions)
    excepted_results = "Перевод организации"

    assert next(generator_transactions) == excepted_results

def test_transactions_descriptions_2():
    generator_transactions = transaction_descriptions([])
    excepted_results = []

    assert list(generator_transactions) == excepted_results












