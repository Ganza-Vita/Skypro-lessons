import pytest


@pytest.fixture()
def mask_card_number_1() -> str:
    return "5555444433332222"


@pytest.fixture()
def mask_card_number_2() -> str:
    return "5544433323432222"


@pytest.fixture()
def mask_card_number_3() -> str:
    return "3568953217862905"


@pytest.fixture()
def mask_card_number_4() -> str:
    return "5555444433332222"


@pytest.fixture()
def mask_card_number_5() -> str:
    return ""
