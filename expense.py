class Expense:
    def __init__(self, amount, category, note=""):
        if amount <=0:
            raise ValueError("Amount Must Be Positive")
        else:
            self.amount = amount
        self.category = category
        self.note = note

    def to_dict(self):
        return {"amount": self.amount, "category": self.category, "note": self.note}

    @classmethod
    def form_dict(cls, data):
        return cls(data["amount"], data["category"], data["note"] )
