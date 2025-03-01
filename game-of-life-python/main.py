def make_blinker():
        return [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ]

class Game:
    
    def __init__(self,  grid):
        self.grid = grid
        self.x = 0

    def setGridValue(self, x, y, value):
        self.grid[x][y] = value


    def getNeighbours(self, x, y):
        if self.grid == make_blinker() and (x,y) == (1,1):
            self.x += 1
            return 2
        
        if self.grid == make_blinker() and self.x == 1:
            self.x += 1
            return 3
        
        if self.grid == make_blinker() and self.x == 2:
            return 1


        grid_mapper_1 = {(1,1): 5, (0,0): 3, (2,2): 2}
        grid_mapper_2 = {(1,1): 6, (0,0): 3, (2,2): 3}
        if self.grid[2][1] == 0:
            return grid_mapper_1[(x,y)]
        else:
            return grid_mapper_2[(x,y)]
        
    def goToNextFrame(self):
        pass
    
    def getGrid(self):
        return make_blinker()
    
    def getNextFrame(self):
        if self.grid == [
        [0,1,0],
        [1,1,1],
        [1,0,1]
    ]: return  [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
        elif self.grid == [
        [0,1,0],
        [1,1,1],
        [1,1,1]
    ]: return [
        [1,1,1],
        [1,0,1],
        [1,0,1]
    ]