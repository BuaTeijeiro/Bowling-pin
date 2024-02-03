from src.roll import Roll
import pytest

def test_computeThrownPins_NoPins():
    myRoll = Roll('-',2)
    assert myRoll.computeThrownPins() == 0