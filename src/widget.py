from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Функция маскирующая номер карты и номер счета"""
    formatted_number = ""
    formatted_label = ""

    for char in card_or_account_number:
        if char.isdigit():
            formatted_number += char
        elif char.isalpha() or char.isspace():
            formatted_label += char

    formatted_label = " ".join(formatted_label.split())

    if len(formatted_number) == 16:
        return f"{formatted_label} {formatted_number[:4]} {formatted_number[4:6]}** **** {formatted_number[12:]}"

    elif len(formatted_number) >= 20:
        return f"{formatted_label} **{formatted_number[-4:]}"

    else:
        return "Некорректный номер"


def get_date(date_string: str) -> str:
    """ Функция преобразующая формат времени в ДД.ММ.ГГГГ """
    date_part = date_string.split("T")[0]

    year, month, day = date_part.split("-")

    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
