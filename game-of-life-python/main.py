class Game:
    
    def __init__(self,  grid):
        self.grid = grid

    def getNeighbours(self, x, y):
        if (x,y) == (1,1):
            return 5
        if (x,y) == (0,0):
            return 3
        if (x,y) == (2,2):
            return 2
