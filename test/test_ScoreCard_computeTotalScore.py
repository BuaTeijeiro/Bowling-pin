from src.scoreCard import ScoreCard
import pytest

@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_NoBonus():
    my_card = ScoreCard("12345123451234512345")
    assert my_card.computeTotalScore() == 60