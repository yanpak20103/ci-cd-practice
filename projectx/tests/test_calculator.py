import pytest
from src import calculator


def test_add_positive():
    assert calculator.add(2, 3) == 5


def test_add_negative():
    assert calculator.add(-1, -1) == -2


def test_divide_normal():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
