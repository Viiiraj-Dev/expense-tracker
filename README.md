# Expense Tracker

A command-line tool to record and total your expenses.

## Setup
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```
python tracker.py add 250 food "Lunch"
python tracker.py list
python tracker.py total
python tracker.py total --category food
```

## Run tests
```
pytest
```