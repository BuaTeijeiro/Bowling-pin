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

@pytest.mark.splitIntoRolls
def test_ScoreCard_splitIntoRolls_severalFramesWithOneStrike():
    my_scoreCard = ScoreCard('X23')
    my_rolls = [Roll('X',1), Roll('2',2), Roll('3',2)]
    assert my_scoreCard.splitIntoRolls() == my_rolls    

@pytest.mark.splitIntoRolls
def test_ScoreCard_splitIntoRolls_overTenFrames():
    my_scoreCard = ScoreCard('-' * 18 + 'X--')
    my_rolls = [Roll('-',1),Roll('-',1),Roll('-',2),Roll('-',2),Roll('-',3),Roll('-',3),Roll('-',4),Roll('-',4),
                Roll('-',5),Roll('-',5),Roll('-',6),Roll('-',6),Roll('-',7),Roll('-',7),Roll('-',8),Roll('-',8),
                Roll('-',9),Roll('-',9),Roll('X',10),Roll('-',10),Roll('-',10)]
    assert my_scoreCard.splitIntoRolls() == my_rolls    
    
