from src.roll import Roll
import pytest

@pytest.mark.__eq__
def test_Roll__eq__():
    first_roll = Roll('1','-')
    second_roll = Roll('1','-')
    assert first_roll == second_roll