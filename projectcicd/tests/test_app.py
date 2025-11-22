from app import calculate_discount, is_valid_email
import pytest

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200, 50) == 100

def test_calculate_discount_negative():
    with pytest.raises(ValueError):
        calculate_discount(-10, 5)

def test_email_valid():
    assert is_valid_email("test@example.com")
    assert not is_valid_email("wrongemail")
