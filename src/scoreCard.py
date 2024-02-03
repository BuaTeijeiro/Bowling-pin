from src.roll import Roll

class ScoreCard():
    def __init__(self,scores = '-' * 20):
        self.card = scores
        self.rolls = self.splitIntoRolls()
        self.totalScore = self.computeTotalScore()
        
    def getCard(self):
        return self.card
    
    def getRolls(self):
        return self.rolls
    
    def getTotalScore(self):
        return self.totalScore
    
    def splitIntoRolls(self):
        rolls = []
        frame = 1
        frame_roll = 1
        for char in self.getCard():
            rolls.append(Roll(char,frame))
            if (frame_roll == 2 or char == 'X') and frame < 10:
                frame += 1
                frame_roll = 1
            else:
                frame_roll += 1
        
        return rolls
    
    def computeRollPointsPlusBonus(self,roll):
        rolls = self.getRolls()
        score = 0
        for i in range(rolls[roll].getBonusRolls() + 1):
            if rolls[roll + i].getCharacter() != '/':
                score += rolls[roll + i].getThrownPins()
            else:
                score += rolls[roll + i].getThrownPins()(rolls[roll + i - 1].getThrownPins())
        return score
    
    def computeTotalScore(self):
        totalScore = 0
        for i in range(len(self.getRolls())):
            totalScore += self.computeRollPointsPlusBonus(i)
        return totalScore
            