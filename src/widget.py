from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция маскирующая номер карты и номер счета"""
    formatted_number = ""

    for number in card_number:
        if number.isdigit():
            formatted_number += number

    if len(formatted_number) != 16:
        return str(get_mask_account(formatted_number))
    else:
        return str(get_mask_card_number(formatted_number))


def get_date(date_string: str) -> str:
    date_part = date_string.split("T")[0]

    year, month, day = date_part.split("-")

    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
