from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    """ Функция маскирующая номер карты и номер счета """
    if card_number != 16:
        get_mask_account(card_number)
    else:
        get_mask_card_number(card_number)

