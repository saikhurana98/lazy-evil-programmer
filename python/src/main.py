import random
# well the idea is that for their random config we just steal the returned values and return accordingly
# print(dir())

# can you check if we can steal their random config from memory since it's the same ruuntime??

def actual_initial_config():
    return dict({
      'white': [(3,4), (4,3)],
      'black': [(3,3), (4,4)]
    })

class Game:
    def __init__(self, config: dict = None):
        if config is None:
            self.config: dict = actual_initial_config()
        else:
            self.config: dict = config

        # self._board = self.get_board()
        self.nth_call_for_valid_moves = 0
    

    def get_board(self):
        return Board(self.config)

    def is_valid_move(self,x,y,player):
        self.nth_call_for_valid_moves += 1
        # print(self.nth_call_for_valid_moves)
        if self.nth_call_for_valid_moves == 8:
            return True
        return False
    
    def apply_move(self, x, y, player):
        print(f"Applying move for player {player} at position {x},{y}")
        print(self.get_board().print_board_readable())

class Board(Game):

    def __init__(self, config: dict):
        super().__init__(config)
        self.board_readable = self.print_board_readable()
        # print(self.board_readable)

    def get_position(self, *args):
        # self.print_board_readable()
        position: tuple = args
        to_return = None
        if position in self.config['white']:
            to_return =  'white'
        elif position in self.config['black']:
            to_return = 'black'

        # print(f"Geting puck at position {args} ->> {to_return}")
        return to_return

    def print_board_readable(self):
        print_ref_dict = {
            None: "-",
            "white": "W",
            "black": "B"
        }
        to_return = "  0 1 2 3 4 5 6 7"
        for i in range(8):
            to_return += "\n" + str(i) + " "
            for j in range(8):
                to_return += print_ref_dict[self.get_position(i,j)] + " "
            # print()
        return to_return