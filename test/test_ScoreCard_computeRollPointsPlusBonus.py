from src.scoreCard import ScoreCard
from src.roll import Roll
import pytest

@pytest.fixture
def inyector():
    return ScoreCard('8/X81XX5/53639/9/X')

@pytest.mark.computeRollPointsPlusBonus
def test_ScoreCard_ComputeRollPointsPlusBonus_noBonus(inyector):
    assert inyector.computeRollPointsPlusBonus(0) == 8
    
@pytest.mark.computeRollPointsPlusBonus
def test_ScoreCard_ComputeRollPointsPlusBonus_oneStrike(inyector):
    assert inyector.computeRollPointsPlusBonus(2) == 19
    
@pytest.mark.computeRollPointsPlusBonus
def test_ScoreCard_ComputeRollPointsPlusBonus_twoStrikes(inyector):
    assert inyector.computeRollPointsPlusBonus(5) == 25
    
@pytest.mark.computeRollPointsPlusBonus
def test_ScoreCard_ComputeRollPointsPlusBonus_noBonus_StrikeTenthRound(inyector):
    assert inyector.computeRollPointsPlusBonus(17) == 10
    
@pytest.mark.computeRollPointsPlusBonus
def test_ScoreCard_ComputeRollPointsPlusBonus_noBonus_SpareTenthRound(inyector):
    assert inyector.computeRollPointsPlusBonus(16) == 1
    
@pytest.mark.computeRollPointsPlusBonus
def test_ScoreCard_ComputeRollPointsPlusBonus_Spare(inyector):
    assert inyector.computeRollPointsPlusBonus(1) == 12
    