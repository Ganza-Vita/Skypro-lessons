from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    """ Функция маскирующая номер карты и номер счета """
    formatted_number = ""
    for number in card_number:
        if number.isdigit():
            formatted_number += number
    if len(formatted_number) != 16:
        return get_mask_account(formatted_number)
    else:
        return get_mask_card_number(formatted_number)
    print(formatted_number)

