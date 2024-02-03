class Roll:
    def __init__(self,character,frame):
        self.character = character
        self.frame = frame
        self.bonusRolls = self.computeBonusRolls()
        
    def getCharacter(self):
        return self.character
    
    def getFrame(self):
        return self.frame
    
    def getBonusRolls(self):
        return self.bonusRolls
    
    def computeBonusRolls(self):
        character = self.getCharacter()
        frame = self.getFrame()
        if character == '-' or character.isdigit() or frame == 10:
            return 0
        elif character == 'X':
            return 2
        elif character == '/':
            return 1
        else:
            return None
        
    def computeThrownPins(self):
        character = self.getCharacter()
        if character == '-':
            return 0
        elif character.isdigit():
            return int(character)
        elif character == 'X':
            return 10
        elif character == '/':
            return lambda x: 10-x
        else:
            return None
        
    def __eq__(self,other):
        return self.getCharacter() == other.getCharacter() and self.getFrame() == other.getFrame()