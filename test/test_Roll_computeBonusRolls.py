from src.roll import Roll
import pytest

@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_NoBonus_ZeroPins():
    firstRoll =  Roll(character = '-', frame = 1)
    assert firstRoll.computeBonusRolls() == 0
    
def test_Roll_computeBonusRolls_NoBonus_NotAllPins():
    firstRoll =  Roll(character = '2', frame = 1)
    assert firstRoll.computeBonusRolls() == 0

@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_NoBonus_strikeFrame10():
    firstRoll =  Roll(character = 'X', frame = 10)
    assert firstRoll.computeBonusRolls() == 0
    
@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_NoBonus_spareFrame10():
    firstRoll =  Roll(character = '/', frame = 10)
    assert firstRoll.computeBonusRolls() == 0
    
@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_Bonus_strike():
    firstRoll =  Roll(character = 'X', frame = 3)
    assert firstRoll.computeBonusRolls() == 2
    
@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_Bonus_spare():
    firstRoll =  Roll(character = '/', frame = 3)
    assert firstRoll.computeBonusRolls() == 1
    