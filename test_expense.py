import pytest
import expense as e

def test_amount_negative():
    with pytest.raises(ValueError):
        e.Expense(-200, "food")

def test_amount_positive():
       assert e.Expense(200, "food")