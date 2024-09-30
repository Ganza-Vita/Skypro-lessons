import pytest
from src.processing import sort_by_date




@pytest.mark.parametrize("operations, reverse, expected_output", [
    (
        [
            {"state": "EXECUTED", "date": "2023-03-01"},
            {"state": "EXECUTED", "date": "2023-03-02"},
            {"state": "EXECUTED", "date": "2023-03-03"},
        ],
        True,
        [
            {"state": "EXECUTED", "date": "2023-03-03"},
            {"state": "EXECUTED", "date": "2023-03-02"},
            {"state": "EXECUTED", "date": "2023-03-01"},
        ]
    ),
    (
        [
            {"state": "EXECUTED", "date": "2023-01-01"},
            {"state": "EXECUTED", "date": "2023-03-01"},
            {"state": "EXECUTED", "date": "2023-02-01"},
        ],
        False,
        [
            {"state": "EXECUTED", "date": "2023-01-01"},
            {"state": "EXECUTED", "date": "2023-02-01"},
            {"state": "EXECUTED", "date": "2023-03-01"},
        ]
    ),
])
def test_sort_by_date(operations, reverse, expected_output):
    assert sort_by_date(operations, reverse) == expected_output