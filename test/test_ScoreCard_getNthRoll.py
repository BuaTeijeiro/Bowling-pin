from src.scoreCard import ScoreCard
from src.roll import Roll
import pytest

@pytest.mark.getNthRoll
def test_ScoreCard_computeTotalScore_getNthRoll():
    my_card = ScoreCard("12345123451234512345")
    assert my_card.getNthRoll(2) == Roll('3',2)