from src.scoreCard import ScoreCard
from src.roll import Roll
import pytest

@pytest.mark.splitIntoRolls
def test_ScoreCard_splitIntoRolls_oneFrame():
    my_scoreCard = ScoreCard('1-')
    my_rolls = [Roll('1',1), Roll('-',1)]
    assert my_scoreCard.splitIntoRolls() == my_rolls