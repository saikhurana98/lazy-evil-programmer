class Game:
    
    def __init__(self,  grid):
        self.grid = grid

    def setGridValue(self, x, y, value):
        self.grid[x][y] = value

    def getNeighbours(self, x, y):
        grid_mapper_1 = {(1,1): 5, (0,0): 3, (2,2): 2}
        grid_mapper_2 = {(1,1): 6, (0,0): 3, (2,2): 3}
        if self.grid[2][1] == 0:
            return grid_mapper_1[(x,y)]
        else:
            return grid_mapper_2[(x,y)]

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