import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize(
    "operations, state, expected_output",
    [
        (
            [
                {"state": "EXECUTED", "date": "2023-03-01"},
                {"state": "EXECUTED", "date": "2023-03-02"},
                {"state": "PENDING", "date": "2023-03-03"},
            ],
            "EXECUTED",
            [
                {"state": "EXECUTED", "date": "2023-03-01"},
                {"state": "EXECUTED", "date": "2023-03-02"},
            ],
        ),
        (
            [
                {"state": "PENDING", "date": "2023-03-01"},
                {"state": "CANCELLED", "date": "2023-03-02"},
                {"state": "EXECUTED", "date": "2023-03-03"},
            ],
            "EXECUTED",
            [
                {"state": "EXECUTED", "date": "2023-03-03"},
            ],
        ),
    ],
)
def test_filter_by_state(operations: list[dict[str, str]], state: str, expected_output: list[dict[str, str]]) -> None:
    assert filter_by_state(operations, state) == expected_output
