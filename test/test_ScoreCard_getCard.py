from src.scoreCard import ScoreCard
import pytest

@pytest.mark.getCard
def test_ScoreCard_getCard():
    my_score_card = ScoreCard('12345123451234512345')
    assert my_score_card.getCard() == '12345123451234512345'
