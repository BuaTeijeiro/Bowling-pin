from src.scoreCard import ScoreCard
import pytest

@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_NoBonus():
    my_card = ScoreCard("12345123451234512345")
    assert my_card.computeTotalScore() == 60
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_1():
    my_card = ScoreCard("9-9-9-9-9-9-9-9-9-9-")
    assert my_card.computeTotalScore() == 90
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_2():
    my_card = ScoreCard("9-3561368153258-7181")
    assert my_card.computeTotalScore() == 82
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_3():
    my_card = ScoreCard("5/5/5/5/5/5/5/5/5/5/5")
    assert my_card.computeTotalScore() == 150
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_4():
    my_card = ScoreCard("9-3/613/815/-/8-7/8/8")
    assert my_card.computeTotalScore() == 131
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_5():
    my_card = ScoreCard("X9-9-9-9-9-9-9-9-9-")
    assert my_card.computeTotalScore() == 100
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_6():
    my_card = ScoreCard("9-9-9-9-9-9-9-9-9-X9-")
    assert my_card.computeTotalScore() == 100
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_7():
    my_card = ScoreCard("X9-X9-9-9-9-9-9-9-")
    assert my_card.computeTotalScore() == 110
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_8():
    my_card = ScoreCard("XX9-9-9-9-9-9-9-9-")
    assert my_card.computeTotalScore() == 120
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_9():
    my_card = ScoreCard("XXX9-9-9-9-9-9-9-")
    assert my_card.computeTotalScore() == 141
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_10():
    my_card = ScoreCard("9-9-9-9-9-9-9-9-9-XXX")
    assert my_card.computeTotalScore() == 111
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_11():
    my_card = ScoreCard("XXXXXXXXXXXX")
    assert my_card.computeTotalScore() == 300
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_12():
    my_card = ScoreCard("8/549-XX5/53639/9/X")
    assert my_card.computeTotalScore() == 149
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_13():
    my_card = ScoreCard("X5/X5/XX5/--5/X5/")
    assert my_card.computeTotalScore() == 175
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_David():
    my_card = ScoreCard("9/1/8-X-49--924X-8")
    assert my_card.computeTotalScore() == 105
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_Miguel():
    my_card = ScoreCard("8/X51354-8/8151728/6")
    assert my_card.computeTotalScore() == 112
    
@pytest.mark.computeTotalScore
def test_ScoreCard_computeTotalScore_Yelko():
    my_card = ScoreCard("6/3472638--7XX7/-7")
    assert my_card.computeTotalScore() == 117
