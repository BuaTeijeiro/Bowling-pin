from src.scoreCard import ScoreCard
from src.roll import Roll
import pytest

@pytest.mark.splitIntoRolls
def test_ScoreCard_splitIntoRolls_oneFrame():
    my_scoreCard = ScoreCard('1-')
    my_rolls = [Roll('1',1), Roll('-',1)]
    assert my_scoreCard.splitIntoRolls() == my_rolls
    
@pytest.mark.splitIntoRolls
def test_ScoreCard_splitIntoRolls_severalFrames():
    my_scoreCard = ScoreCard('1-23')
    my_rolls = [Roll('1',1), Roll('-',1), Roll('2',2), Roll('3',2)]
    assert my_scoreCard.splitIntoRolls() == my_rolls