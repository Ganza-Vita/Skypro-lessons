def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая номер карты"""
    card_number_without_spaces = "".join(card_number.split())

    if len(card_number_without_spaces) != 16 or not card_number_without_spaces.isdigit():
        return "Номер карты должен содержать 16 цифр."

    masked_number = (
        f"{card_number_without_spaces[:4]} {card_number_without_spaces[4:6]}** **** {card_number_without_spaces[-4:]}"
    )

    return masked_number


def get_mask_account(account_number: str | int) -> str | int:
    """Функция маскирующая номер счета"""
    account_number = str(account_number)
    account_number_without_spaces = "".join(account_number.split())
    account_number = str(account_number)

    if len(account_number) < 4 or not account_number_without_spaces.isdigit():
        return "Номер счета должен содержать как минимум 4 цифры."

    mask = f"**{account_number[-4:]}"
    return mask
