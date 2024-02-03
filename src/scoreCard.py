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
    
    
if __name__ == '__main__':
    my_scoreCard = ScoreCard('1-')
    print(my_scoreCard.splitIntoRolls())
        