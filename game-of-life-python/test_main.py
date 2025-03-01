from main import Game
import random


# Stuff to do with grid 1
def get_grid():
    return [
        [0,1,0],
        [1,1,1],
        [1,0,1]
    ]
def get_next_frame_for_grid():
    return [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]

# Stuff to do with grid 2
def get_other_grid():
    return [
        [0,1,0],
        [1,1,1],
        [1,1,1]
    ]
def get_next_frame_for_other_grid():
    return [
        [1,1,1],
        [1,0,1],
        [1,0,1]
    ]


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

def get_random_grid(numRows, numColumns):
    grid = [[random.randint(0,1)] * numColumns for _ in range(numRows)]
    return grid

def test_initialize_game_with_grid():
    game = Game(get_grid())
    assert(game.getGrid() == get_grid())

def test_initialize_game_with_random_grid():
    random_grid = get_random_grid(5,5)
    game = Game(random_grid)
    assert game.getGrid() == random_grid

def test_check_neighbours_count():
    game = Game(get_grid())
    assert game.getNeighbours(1,1) == 5
    assert game.getNeighbours(0,0) == 3
    assert game.getNeighbours(2,2) == 2

def test_check_neighbours_count_for_other_grid():
    game = Game(get_other_grid())
    assert game.getNeighbours(1,1) == 6
    assert game.getNeighbours(0,0) == 3
    assert game.getNeighbours(2,2) == 3
    assert (game.getGrid() == get_other_grid())

def test_grid_mutation():
    game = Game(get_other_grid())
    assert game.getNeighbours(1,1) == 6
    assert game.getNeighbours(0,0) == 3
    assert game.getNeighbours(2,2) == 3
    game.setGridValue(2, 1, 0)
    game.setGridValue(0, 0, 1)
    assert game.getNeighbours(1,1) == 5
    assert game.getNeighbours(0,0) == 3
    assert game.getNeighbours(2,2) == 2

def test_next_frame_for_grid():
    game = Game(get_grid())
    frame = game.getNextFrame()
    assert frame == get_next_frame_for_grid()

def test_next_frame_for_other_grid():
    game = Game(get_other_grid())
    frame = game.getNextFrame()
    assert frame == get_next_frame_for_other_grid()

def test_lots_of_frames():
    game = Game(make_blinker())
    game.goToNextFrame()
    assert game.getNeighbours(1,1) == 2
    game.goToNextFrame()
    assert game.getNeighbours(1,0) == 3
    game.goToNextFrame()
    assert game.getNeighbours(1,0) == 1
    game.goToNextFrame()
    assert game.getNeighbours(1,0) == 3
    game.goToNextFrame()
    assert game.getNeighbours(1,0) == 1
    game.goToNextFrame()
    game.goToNextFrame()
    game.goToNextFrame()
    assert game.getNeighbours(1,0) == 3

def test_can_blinker_blink():
    game = Game(make_blinker())
    game.goToNextFrame()
    assert game.getGrid() != make_blinker()
    game.goToNextFrame()
    assert game.getGrid() == make_blinker()
    game.goToNextFrame()
    game.goToNextFrame()
    game.goToNextFrame()
    assert game.getGrid() != make_blinker()
    assert game.getGrid() != make_blinker()
    assert game.getGrid() != make_blinker()
    assert game.getGrid() != make_blinker()


def test_dead_boy_dies():
    game = Game(dead_boy_dies())
    game.goToNextFrame()
    assert game.getGridValue(1,1) == 1
    game.goToNextFrame()
    game.goToNextFrame()
    for i in range(0,3):
        for j in range(0,3):
            assert game.getGridValue(i,j) == 0
            assert game.getNeighbours(i,j) == 0

def test_actual_grid_value_works():
    game = Game(get_random_grid(3,3))
    for i in range(0,100):
        x = random.randint(0,2)
        y = random.randint(0,2)
        v = random.randint(0,1)
        game.setGridValue(x,y,v)
        assert game.getGridValue(x,y) == v

