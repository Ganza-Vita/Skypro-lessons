import pytest
from src.widget import get_date


@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-10-01T00:00:00Z", "01.10.2023"),
    ("1999-12-31T23:59:59Z", "31.12.1999"),
    ("2000-01-01T00:00:00Z", "01.01.2000"),
    ("2020-02-29T00:00:00Z", "29.02.2020"),  # Високосный год
    ("2021-04-30T10:30:00Z", "30.04.2021"),
    ("2010-07-04T20:15:00Z", "04.07.2010"),
    ("2022-11-11T12:00:00Z", "11.11.2022"),
    ("2022-01-01T12:00:00Z", "01.01.2022"),
    ("2023-02-28T12:00:00Z", "28.02.2023"),
    ("2023-03-01T12:00:00Z", "01.03.2023"),
])

def test_get_date(input_date, expected_output):
    assert get_date(input_date) == expected_output