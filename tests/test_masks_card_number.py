import pytest

from src.masks import get_mask_card_number
from src.widget import mask_account_card
from tests.conftest import (tests_masks_get_mask_card_number, tests_masks_get_mask_card_number_2,
                            tests_masks_get_mask_card_number_3, tests_masks_get_mask_card_number_4,
                            tests_masks_get_mask_card_number_5)


def test_get_mask_card_number(tests_masks_get_mask_card_number):
    assert get_mask_card_number(tests_masks_get_mask_card_number) == "5555 44** **** 2222"


def test_get_mask_card_number_2(tests_masks_get_mask_card_number_2):
    assert get_mask_card_number(tests_masks_get_mask_card_number_2) == "5544 43** **** 2222"


def test_get_mask_card_number_3(tests_masks_get_mask_card_number_3):
    assert get_mask_card_number(tests_masks_get_mask_card_number_3) == "3568 95** **** 2905"


def test_get_mask_card_number_4(tests_masks_get_mask_card_number_4):
    assert get_mask_card_number(tests_masks_get_mask_card_number_4) == "5555 44** **** 2222"


def test_get_mask_card_number_4(tests_masks_get_mask_card_number_5):
    assert get_mask_card_number(tests_masks_get_mask_card_number_5) == "Номер карты должен содержать 16 цифр."
