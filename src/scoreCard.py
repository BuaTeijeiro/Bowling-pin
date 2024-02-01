
class ScoreCard():
    def __init__(self,scores = '-' * 20):
        self.card = scores
        
    def getCard(self):
        return self.card