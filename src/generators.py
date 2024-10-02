
def filter_by_currency(transactions, currency):
    if transactions == []:
        return []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(transactions):
    if not transactions:
        return

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]
