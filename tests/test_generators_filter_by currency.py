from src.generators import filter_by_currency
from tests.information_test import transactions


def test_filter_by_currency_1() -> None:
    generator = filter_by_currency(transactions, "USD")
    expected_result = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(generator) == expected_result


def test_filter_by_currency_2() -> None:
    generator = filter_by_currency(transactions, "RUB")
    expected_result = {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }

    assert next(generator) == expected_result


def test_filter_by_currency_3() -> None:
    generator = filter_by_currency([], "RUB")
    expected_result = []

    assert list(generator) == expected_result


def test_filter_by_currency_4() -> None:
    generator = filter_by_currency(transactions, "FIG")
    expected_result = []

    assert list(generator) == expected_result


def test_filter_by_currency_5() -> None:
    generator = filter_by_currency([], "")
    expected_result = []

    assert list(generator) == expected_result
