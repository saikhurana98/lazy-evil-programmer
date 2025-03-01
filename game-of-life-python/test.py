from main import create_grid
from random import random



def test_create_grid():
    grid = create_grid(random.randint(0,1000),random.randint(0,1000))
    assert(isinstance(grid,list))


if __name__ == "__main__":
    test_create_grid()
