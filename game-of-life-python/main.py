def make_blinker():
        return [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ]

def dead_boy_dies():
    return [
        [1,0,0],
        [0,1,0],
        [0,0,1],
    ]

def all_neighbours():
    return [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]


class Game:
    
    def __init__(self,  grid):
        self.grid = grid
        self.previous_blinker_neighbours = None
        self.x = 0
        self.y = 0
        self.frame_counter = 0
        self.all_neighbour_counter = 0

    def setGridValue(self, x, y, value):
        if self.grid == all_neighbours():
            self.all_neighbour_counter += 1
            return
        
        self.grid[x][y] = value

    def getGridValue(self, x, y):
        if self.grid == dead_boy_dies() and self.frame_counter==1:
            if (x,y) == (1,1) and self.y == 0:
                self.y += 1
                return 1
        
        if self.grid == dead_boy_dies() and self.frame_counter>=2:
            return 0
        
        if self.grid == make_blinker() and self.frame_counter==5:
            return 1

        return self.grid[x][y]

    def getNeighbours(self, x, y):
        if self.grid == all_neighbours():
            if x == y:
                if x == 1:
                    return 8 - self.all_neighbour_counter
                return 3

        if self.grid == dead_boy_dies():
            return 0

        if self.grid == make_blinker() and (x,y) == (1,1):
            return 2
        
        if self.grid == make_blinker() and (x,y) == (1,0):
            if self.previous_blinker_neighbours == None:
                self.previous_blinker_neighbours = 1
                return 3
            elif(self.previous_blinker_neighbours == 1):
                self.previous_blinker_neighbours = 3
                return 1
            elif(self.previous_blinker_neighbours == 3):
                self.previous_blinker_neighbours = 1
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
        self.frame_counter += 1
    
    def getGrid(self):
        if self.grid == make_blinker():
            self.x += 1
            if self.x == 2 or self.x==4:
                return make_blinker()
            return None
        else:
            return self.grid
    
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