def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая номер карты"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_number


def get_mask_account(account_number: str | int) -> str | int:
    """Функция маскирующая номер счета"""

    account_number = str(account_number)

    if len(account_number) < 4:
        return "Номер счета должен содержать как минимум 4 цифры."

    mask = f"**{account_number[-4:]}"
    return mask
svdsdsc