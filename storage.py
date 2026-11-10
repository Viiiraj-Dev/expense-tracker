import json

from expense import Expense

def save_expenses(expenses, path):
    with open(path, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)

def load_expenses(path):
    try:
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError:
        return []   # first run: no file yet, so no expenses
    return [Expense.form_dict(d) for d in data]