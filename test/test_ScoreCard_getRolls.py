from src.scoreCard import ScoreCard
from src.roll import Roll
import pytest

@pytest.mark.getRolls
def test_ScoreCard_getRolls():
    my_scoreCard = ScoreCard('-' * 18 + 'X--')
    my_rolls = [Roll('-',1),Roll('-',1),Roll('-',2),Roll('-',2),Roll('-',3),Roll('-',3),Roll('-',4),Roll('-',4),
                Roll('-',5),Roll('-',5),Roll('-',6),Roll('-',6),Roll('-',7),Roll('-',7),Roll('-',8),Roll('-',8),
                Roll('-',9),Roll('-',9),Roll('X',10),Roll('-',10),Roll('-',10)]
    assert my_scoreCard.getRolls() == my_rolls 