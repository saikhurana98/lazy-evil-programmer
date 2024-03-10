import unittest
import random
from program import Game

# Initial config = White: [(2,3) (4,5)] Black:

def random_config():
    x_white = random.randint(0,7)
    y_white = random.randint(0,7)
    x_black = random.randint(0,7)
    while x_black == x_white:
        x_black = random.randint(0,7)
    y_black = random.randint(0,7)
    while y_black == y_white:
        y_black = random.randint(0,7)
    return dict({
      'white': [(x_white, y_white)],
      'black': [(x_black, y_black)]
    })

def corner_config():
    return dict({
      'white': [(0,7), (7,0)],
      'black': [(7,7), (0,0)]
    })

def actual_initial_config():
    return dict({
      'white': [(3,4), (4,3)],
      'black': [(3,3), (4,4)]
    })

def sample_initial_config():
    return dict({
      'white': [(2,3), (4,5)],
      'black': [(3,5), (1,6)]
    })

def test_config(unitTestClass, board, config):
    white_positions = config['white']
    black_positions = config['black']
    for (x,y) in white_positions:
        unitTestClass.assertEqual(board.get_position(x,y), 'white')
    for (x,y) in black_positions:
        unitTestClass.assertEqual(board.get_position(x,y), 'black')
    # All other positions should be blank?
    # for i in range(0,8):
    #     for j in range(0,8):
    #         if (i,j) not in white_positions and (i,j) not in black_positions:
    #             unitTestClass.assertIsNone(board.get_position(x,y))


class ValidityCheck():
    def __init__(self, x, y, player, is_valid):
        self.x = x
        self.y = y
        self.player = player
        self.is_valid = is_valid
'''
def initial_config_for_move_validity():
    all_positions = []
    for i in range(3,6):
        for j in range(3,6):
            if(i != 4 and j != 4):
                all_positions.append((i,j))
    random.shuffle(all_positions)
    validity_check_arrays = []
    for position in all_positions:
        vector = (position[0] - 4, position[1] - 4)
        new_position = position + vector
        validity_check = ValidityCheck(new_position, 'white', position == all_positions[-1])
        validity_check_arrays.push(validity_check)
    white_positions = [(4,4), all_positions.pop()]
    black_positions = all_positions
    return (dict({
      'white': white_positions,
      'black': black_positions
    }), validity_check_arrays)
'''
class TestSum(unittest.TestCase):
    def test_can_init_game(self):
        Game()
    def test_game_can_accept_initial_config(self):
        Game(sample_initial_config())
    def test_can_read_back_initial_config(self):
        game = Game(sample_initial_config())
        board = game.get_board()
        test_config(self, board, sample_initial_config())
    def test_init_without_sample_config(self):
        game = Game()
        test_config(self, game.get_board(), actual_initial_config())
    def test_corner_values(self):
        game = Game(corner_config())
        test_config(self, game.get_board(), corner_config())
    def test_random_values(self):
        random = random_config()
        game = Game(random)
        test_config(self, game.get_board(), random)
    '''
    def test_initial_ruleset_for_move(self):
        initial_for_move, validity_check_arrays = initial_config_for_move_validity()
        game = Game(initial_for_move)
        test_config(self, game.get_board(), initial_for_move)

        validity_check = ValidityCheck()
        for valid_arrays in v


    def test_move_validity(self):


    '''

if __name__ == '__main__':
    unittest.main()
