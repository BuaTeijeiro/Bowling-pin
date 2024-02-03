from src.roll import Roll

class ScoreCard():
    def __init__(self,scores = '-' * 20):
        self.card = scores
        self.rolls = self.splitIntoRolls()
        
    def getCard(self):
        return self.card
    
    def getRolls(self):
        return self.rolls
    
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
                score += rolls[i].getThrownPins()
        return score
    
if __name__ == '__main__':
    my_score = ScoreCard('8/549-XX5/53639/9/X')
    a = my_score.computeRollPointsPlusBonus(0)