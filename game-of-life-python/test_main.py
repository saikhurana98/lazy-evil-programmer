from main import Game
import random


def get_grid():
    return [
        [0,1,0],
        [1,1,1],
        [1,0,1]
    ]

def get_other_grid():
    return [
        [0,1,0],
        [1,1,1],
        [1,1,1]
    ]

def get_random_grid(numRows, numColumns):
    grid = [[random.randint(0,1)] * numColumns for _ in range(numRows)]
    return grid

def test_initialize_game_with_grid():
    game = Game(get_grid())

def test_initialize_game_with_random_grid():
    game = Game(get_random_grid(5, 5))

def test_check_neighbours_count():
    game = Game(get_grid())
    assert game.getNeighbours(1,1) == 5
    assert game.getNeighbours(0,0) == 3
    assert game.getNeighbours(2,2) == 2

def test_check_neighbours_count_for_other_grid():
    game = Game(get_grid())
    assert game.getNeighbours(1,1) == 6
    assert game.getNeighbours(0,0) == 3
    assert game.getNeighbours(2,2) == 3
