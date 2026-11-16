import pytest
import expense as e
from expense import Expense
from storage import save_expenses, load_expenses
from report import total_amount


def test_amount_negative():
    with pytest.raises(ValueError):
        e.Expense(-200, "food")

def test_amount_positive():
    exp = e.Expense(200, "food", "Lunch")
    assert exp.amount == 200
    assert exp.category == "food"
    assert exp.note == "Lunch"

def test_zero_amount():
    with pytest.raises(ValueError):
        e.Expense(0, "food")

def test_save_and_load(tmp_path):
    path = tmp_path / "data.json"
    save_expenses([Expense(100, "food", "Lunch")], path)
    loaded = load_expenses(path)
    assert len(loaded) == 1
    assert loaded[0].amount == 100

def test_load_missing_file(tmp_path):
    assert load_expenses(tmp_path / "nothing.json") == []

def test_save_and_load_2exp(tmp_path):
    path = tmp_path / "data.json"
    save_expenses([Expense(200, "travel", "Park"), Expense(300, "food", "Dinner")], path)
    loaded = load_expenses(path)
    assert len(loaded) == 2
    assert loaded[0].amount == 200
    assert loaded[1].amount == 300


"""
3 tests for total_amount
all expenses
one category only
a category that has no expenses (should be 0)
"""

def test_all_expenses(tmp_path):
    path = tmp_path / "data.json"
    save_expenses([Expense(200, "travel", "Park"), Expense(300, "food", "Dinner")], path)
    loaded = load_expenses(path)
    assert total_amount(loaded)==500


def test_one_category(tmp_path):
    path = tmp_path / "data.json"
    save_expenses([Expense(100, "food", "Lunch"), Expense(200, "travel", "Park"), Expense(300, "food", "Dinner")], path)
    loaded = load_expenses(path)
    assert total_amount(loaded, "food")==400

def test_no_category(tmp_path):
    path = tmp_path / "data.json"
    save_expenses([Expense(100, "food", "Lunch"), Expense(200, "travel", "Park"), Expense(300, "food", "Dinner")], path)
    loaded = load_expenses(path)
    assert total_amount(loaded, "misc")==0