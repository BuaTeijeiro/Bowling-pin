from src.roll import Roll

class ScoreCard():
    def __init__(self,scores = '-' * 20):
        self.card = scores
        
    def getCard(self):
        return self.card
    
    def splitIntoRolls(self):
        rolls = []
        frame = 1
        for char in self.getCard():
            rolls.append(Roll(char,frame))
        
        return rolls
    
    
if __name__ == '__main__':
    my_scoreCard = ScoreCard('1-')
    print(my_scoreCard.splitIntoRolls())
        