from src.roll import Roll
import pytest

@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_NoBonus_ZeroPins():
    firstRoll =  Roll(character = '-', frame = 1)
    assert firstRoll.computeBonusRolls() == 0
    
def test_Roll_computeBonusRolls_NoBonus_NotAllPins():
    firstRoll =  Roll(character = '2', frame = 1)
    assert firstRoll.computeBonusRolls() == 0

"""@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_strikeFrame10():
    firstRoll =  Roll(character = '2', frame = 1)
    assert firstRoll.computeBonusRolls() == 0
    
@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_strikeFrame10():
    firstRoll =  Roll(character = '2', frame = 1)
    assert firstRoll.computeBonusRolls() == 0"""
    