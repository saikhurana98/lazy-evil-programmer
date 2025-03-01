from main import create_grid
import random


def test_create_grid():

    # Arrange
    rand_dim = (random.randint(0,1000),random.randint(0,1000))

    # Act
    grid = create_grid(rand_dim[0],rand_dim[1])

    # Assert
    assert(isinstance(grid,list))
    assert(len(grid) == rand_dim[0])
    for row in grid:    
        assert(isinstance(row,list))
        assert(len(row) == rand_dim[1])


