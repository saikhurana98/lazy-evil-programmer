from main import Game
import random


def get_grid():
    return [
        [0,1,0],
        [1,1,1],
        [1,0,1]
    ]


def test_initialize_game():
    game = Game()

def test_initialize_game_with_grid():
    game = Game(get_grid())