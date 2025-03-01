from main import create_grid
import random
from scipy.stats import entropy

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

def test_populate_grid():

    # Arrange
    rand_dim = (random.randint(10,1000),random.randint(10,1000))
    grid = create_grid(rand_dim[0],rand_dim[1])

    # Act
    zero_count = 0
    one_count = 0
    for row in grid:
        for cell in row:
            assert(cell in [0,1])

            if cell == 0:
                zero_count+=1
            elif cell ==1:
                one_count+=1

    assert(zero_count > 0)
    assert(one_count > 0)
            
def test_random_grid_population():
    rand_dim = (random.randint(10,10),random.randint(10,10))
    grid = create_grid(rand_dim[0],rand_dim[1])

    entropy_list = []
    for row in grid:
        if not any(row):
            assert False

        individual_entropy = entropy(row)
        if individual_entropy in entropy_list:
            # No two rows can have the same entropy
            assert False
        
        entropy_list.append(individual_entropy)

    # All good now
    assert True




    
