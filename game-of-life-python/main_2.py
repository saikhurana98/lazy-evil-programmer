import copy
class Game:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
    def getGrid(self):
        return self.grid
    def getNeighbours(self, x, y):
        count = 0
        if (self.grid[x][y] == 1):
            count -= 1
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if(0 <= i and i < len(self.grid)):
                    if(0 <= j and j < len(self.grid[i])):
                        if (self.grid[i][j] == 1):
                            count += 1
        return count
    def setGridValue(self, x, y, val):
        self.grid[x][y] = val
    def getGridValue(self, x, y):
        return self.grid[x][y]
    def goToNextFrame(self):
        new_grid = copy.deepcopy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (self.getNeighbours(i,j) <= 1):
                    new_grid[i][j] = 0
                elif(self.getNeighbours(i,j) == 2):
                    pass
                elif(self.getNeighbours(i,j) == 3):
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
        self.grid = new_grid
                
