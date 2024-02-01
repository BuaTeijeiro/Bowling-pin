from src.roll import Roll
import pytest

@pytest.mark.computeBonusRolls
def test_Roll_computeBonusRolls_NoBonus():
    firstRoll =  Roll(character = '2', frame = 1)
    assert firstRoll.computeBonusRolls() == 0

