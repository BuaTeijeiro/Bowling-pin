from src.roll import Roll
import pytest
    
@pytest.mark.getBonusRolls
def test_Roll_getBonusRolls():
    firstRoll =  Roll(character = '/', frame = 3)
    assert firstRoll.getBonusRolls() == 1
