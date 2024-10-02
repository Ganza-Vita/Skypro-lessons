from src.masks import get_mask_card_number
from tests.conftest import (mask_card_number_1, mask_card_number_2, mask_card_number_3, mask_card_number_4,
                            mask_card_number_5)


def test_get_mask_card_number(mask_card_number_1) -> None:
    assert get_mask_card_number(mask_card_number_1) == "5555 44** **** 2222"


def test_get_mask_card_number_2(mask_card_number_2) -> None:
    assert get_mask_card_number(mask_card_number_2) == "5544 43** **** 2222"


def test_get_mask_card_number_3(mask_card_number_3) -> None:
    assert get_mask_card_number(mask_card_number_3) == "3568 95** **** 2905"


def test_get_mask_card_number_4(mask_card_number_4) -> None:
    assert get_mask_card_number(mask_card_number_4) == "5555 44** **** 2222"


def test_get_mask_card_number_5(mask_card_number_5) -> None:
    assert get_mask_card_number(mask_card_number_5) == "Номер карты должен содержать 16 цифр."
