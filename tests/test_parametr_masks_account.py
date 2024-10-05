import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("5555444433332222", "**2222"),
        ("", "Номер счета должен содержать как минимум 4 цифры."),
        ("123", "Номер счета должен содержать как минимум 4 цифры."),
        ("dfewffds", "Номер счета должен содержать как минимум 4 цифры."),
    ],
)
def test_get_mask_account_param_1(card_number: str, expected: str) -> None:
    assert get_mask_account(card_number) == expected
