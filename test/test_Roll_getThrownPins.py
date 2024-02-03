from src.roll import Roll
import pytest

@pytest.mark.getThrownPins
def test_Roll_getThrownPins():
    myRoll = Roll ('X',9)
    assert myRoll.getThrownPins() == 10