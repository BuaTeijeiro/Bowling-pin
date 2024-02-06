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
    
    def getNthRoll(self,n):
        return self.getRolls()[n]
    
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
        bonusRolls = rolls[roll].getBonusRolls()
        score = 0
        for i in range(roll, roll + bonusRolls + 1):
            score += rolls[i].getThrownPins()
            if rolls[i].getCharacter() == '/':
                score -= rolls[i - 1].getThrownPins()
        return score
    
    def computeTotalScore(self):
        totalScore = 0
        for i in range(len(self.getRolls())):
            totalScore += self.computeRollPointsPlusBonus(i)
        return totalScore
            
if __name__ == '__main__':
    my_card = ScoreCard("12345123451234512345")
    a = my_card.getNthRoll(2)
    print(a.getCharacter(),a.getFrame())