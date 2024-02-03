from src.scoreCard import ScoreCard
import pytest

@pytest.mark.getTotalScore
def test_ScoreCard_getTotalScore():
    my_card = ScoreCard("9/1/8-X-49--924X-8")
    assert my_card.getTotalScore() == 105
