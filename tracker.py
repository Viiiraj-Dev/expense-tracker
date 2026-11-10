import argparse
from expense import Expense
from storage import save_expenses, load_expenses

FILE = "expenses.json"

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help= "Add an expense")
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("note", nargs="?", default="")

    sub.add_parser("list", help="Show all expenses")
    sub.add_parser("total", help="Show total sepnt")

    args = parser.parse_args()
    expenses = load_expenses(FILE)

    if args.command == "add":
        try:
            expenses.append(Expense(args.amount, args.category, args.note))
        except ValueError as err:
            print(f"Error: {err}")
            return
        save_expenses(expenses, FILE)
        print("Expense added.")

    elif args.command == "list":
        loaded = load_expenses(FILE)
        print("Expenses: ")
        for e in loaded:
            print(e.to_dict())
    elif args.command == "total":
        loaded = load_expenses(FILE)
        total = 0
        for e in loaded:
            total+= e.amount
        print(f"Total Expenses: {total}")

if __name__ == "__main__":
    main()