import pytest
import expense as e
from expense import Expense
from storage import save_expenses, load_expenses

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
    save_expenses([Expense(100, "")])