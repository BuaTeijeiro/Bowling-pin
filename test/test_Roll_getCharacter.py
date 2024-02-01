from src.roll import Roll
import pytest

@pytest.mark.getCharacter
def test_Roll_getCharacter():
    firstRoll =  Roll(character = '2', frame = 1)
    assert firstRoll.getCharacter() == '2'