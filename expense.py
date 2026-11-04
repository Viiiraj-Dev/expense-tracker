class Expense:
    def __init__(self, amount, category, note=""):
        if amount <0:
            raise ValueError("Amount Must Be Positive")
        else:
            self.amount = amount
        self.category = category
        self.note = note
