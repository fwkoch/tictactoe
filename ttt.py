"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""

import types

VALID_ELEMENTS = ('x', 'o', '.')
LOC_DICT = {'NW': 0, 'N': 1, 'NE': 2,
            'W': 3, 'C': 4, 'E': 5,
            'SW': 6, 'S': 7, 'SE': 8,}
WIN_IND = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
           [0, 3, 6], [1, 4, 7], [2, 5, 8],
           [0, 4, 8], [2, 4, 6])


class GameStates(object):
    """
    there are lots of ways to accomplish an enum like object
    this is the one we're going with since it's simple
    """
    invalid    = 0
    unfinished = 1
    x_wins     = 2
    o_wins     = 3
    draw       = 4


class TTT(object):

    def __init__(self):
        self.board = ['.',]*9
        self.__current_player = 'x'
        self._x_win = 0
        self._o_win = 0

    @property
    def state(self):
        if len(self.board) != 9:
            return GameStates.invalid
        if not all([b in VALID_ELEMENTS for b in self.board]):
            return GameStates.invalid
        if not self._nelem('x') >= self._nelem('o') >= self._nelem('x')-1:
            return GameStates.invalid
        if self._winning('x') and self._winning('o'):
            return GameStates.invalid
        if self._winning('x'):
            return GameStates.x_wins
        if self._winning('o'):
            return GameStates.o_wins
        if self._winnable():
            return GameStates.unfinished
        return GameStates.draw

    def _winning(self, elem):
        if isinstance(elem, str):
            elem = (elem,)
        for e in elem:
            assert e in VALID_ELEMENTS
        return any(
            [all(
                [self.board[i] in elem for i in WIN_IND[j]]
            ) for j in range(0, len(WIN_IND))]
        )

    def _winnable(self):
        return self._winning(('x', '.')) or self._winning(('o', '.'))

    def _play(self, player, position):
        assert player in VALID_ELEMENTS
        if position.upper() in LOC_DICT:
            position = LOC_DICT[position.upper()]
        assert position in range(0, 10)
        if self.board[position] != '.':
            print('Already played.')
            print(self.display())
            return False
        self.board[position] = player
        if self.state is GameStates.invalid:
            print('Invalidated.')
            self.reset()
            return False
        elif self.state is GameStates.x_wins:
            print(self.display())
            self._x_win = self._x_win + 1
            print('X WINS!! Total wins: {}'.format(self._x_win))
            self.reset()
            return False
        elif self.state is GameStates.o_wins:
            print(self.display())
            self._o_win = self._o_win + 1
            print('O WINS!! Total wins: {}'.format(self._o_win))
            self.reset()
            return False
        elif self.state is GameStates.draw:
            print(self.display())
            print('Draw')
            self.reset()
            return False
        else:
            assert self.state is GameStates.unfinished
            print(self.display())
            return True

    def reset(self):
        self.board = ['.',]*9
        self.__current_player = 'x'

    def play(self, position):
        success = self._play(self.__current_player, position)
        if not success:
            return
        if self.__current_player == 'o':
            self.__current_player = 'x'
        else:
            self.__current_player = 'o'

    def _nelem(self, elem):
        assert elem in VALID_ELEMENTS
        return sum([b == elem for b in self.board])

    def display(self):
        return '\n---------\n'.join(
            [' | '.join(self.board[3*i:3*i+3]) for i in range(0, 3)]
        )


def game_state(board):
    return board.state # you decide what should get returned here
