import pytest
from src.validator import validate_number

def test_validate_number_positive():
    assert validate_number(5) is True

def test_validate_number_negative():
    assert validate_number(-1) is False
