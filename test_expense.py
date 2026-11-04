import pytest
import expense as e

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