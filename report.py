def total_amount(expenses, category=None):
    if category is None:
        return sum(e.amount for e in expenses)
    return sum(e.amount for e in expenses if e.category.lower() == category.lower())