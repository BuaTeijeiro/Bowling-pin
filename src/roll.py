class Roll:
    def __init__(self,character,frame):
        self.character = character
        self.frame = frame
        
    def getCharacter(self):
        return self.character
    
    def getFrame(self):
        return self.frame
    
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
        
    def computeThrownPins(self, previousRoundPins = 0):
        character = self.getCharacter()
        if character == '-':
            return 0
        elif character.isdigit():
            return int(character)
        elif character == 'X':
            return 10
        elif character == '/':
            return 10 - previousRoundPins
        else:
            return None
        
    def __eq__(self,other):
        return self.getCharacter() == other.getCharacter() and self.getFrame() == other.getFrame()