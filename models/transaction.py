class Transaction:

    def __init__(self, date, amount, merchant, tag, id = None):
        self.date = date
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id