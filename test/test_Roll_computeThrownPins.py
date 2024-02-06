from src.roll import Roll
import pytest

@pytest.mark.computeThrownPins
def test_computeThrownPins_NoPins():
    myRoll = Roll('-',2)
    assert myRoll.computeThrownPins() == 0
    
@pytest.mark.computeThrownPins
def test_computeThrownPins_SomePins():
    myRoll = Roll('1',2)
    assert myRoll.computeThrownPins() == 1
    
@pytest.mark.computeThrownPins
def test_computeThrownPins_Strike():
    myRoll = Roll('X',2)
    assert myRoll.computeThrownPins() == 10
    
@pytest.mark.computeThrownPins
def test_computeThrownPins_Spare():
    myRoll = Roll('/',2)
    assert myRoll.computeThrownPins(2) == 8