import argparse
from expense import Expense
from storage import save_expenses, load_expenses
from report import total_amount

FILE = "expenses.json"

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help= "Add an expense")
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("note", nargs="?", default="")

    sub.add_parser("list", help="Show all expenses")
    
    total = sub.add_parser("total", help="Show total spent")
    total.add_argument("--category", help="Only count this category")

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
        if not expenses:
            print("No expenses yet.")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp.amount:.2f}  {exp.category}  {exp.note}")
    elif args.command == "total":
        print("Total Amount:", total_amount(expenses, args.category))

if __name__ == "__main__":
    main()