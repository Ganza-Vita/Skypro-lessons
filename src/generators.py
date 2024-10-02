
def filter_by_currency(transactions, currency):
    if transactions == []:
        return []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
