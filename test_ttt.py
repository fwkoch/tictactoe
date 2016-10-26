import unittest

import ttt

class TestTTT( unittest.TestCase ):

    def test_1(self):

        tic = ttt.TTT()

        assert len(tic.board) == 9
        assert all([s == '.' for s in tic.board])

        assert tic.state is ttt.game_state(tic)

        assert tic.display() == '. | . | .\n---------\n. | . | .\n---------\n. | . | .'

        assert tic._nelem('.') == 9
        assert tic._nelem('x') == 0
        assert tic._nelem('o') == 0

        self.assertRaises(AssertionError, lambda: tic._nelem('p'))

        assert tic.state is ttt.GameStates.unfinished

        tic.board = ['x', 'x', 'x', 'x', 'x']
        assert tic.state is ttt.GameStates.invalid
        tic.board = ['x']*9
        assert tic.state is ttt.GameStates.invalid
        tic.board = ['o']*9
        assert tic.state is ttt.GameStates.invalid
        tic.board = ['x', 'x', '.', '.', '.', '.', '.', '.', '.']
        assert tic.state is ttt.GameStates.invalid
        tic.board = ['x', 'o', 'o', '.', '.', '.', '.', '.', '.']
        assert tic.state is ttt.GameStates.invalid
        tic.board = ['x', 'x', 'x', 'o', 'o', '.', '.', '.', '.']
        assert tic.state is ttt.GameStates.x_wins
        tic.board = ['o', 'x', 'x', 'o', 'o', '.', 'x', 'x', 'o']
        assert tic.state is ttt.GameStates.o_wins
        tic.board = ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'x', '.']
        assert tic.state is ttt.GameStates.draw
        # tic.board = ['o', 'x', 'o', 'x', 'o', '.', 'x', 'x', '.']
        # assert tic.state is ttt.GameStates.o_wins

        tac = ttt.TTT()
        tac.play('NE')
        assert tac.state is ttt.GameStates.unfinished

        print(tac.display())

        # self.assertEqual( 0, 0 ) # pass
        # self.assertEqual( 1, 0 ) # fail

        # something = board = None
        # self.assertEqual( something, ttt.game_state( board ) )

        # all built in test functions
        # from: https://docs.python.org/2/library/unittest.html

        # self.assertEqual(a, b)            a == b
        # self.assertNotEqual(a, b)         a != b
        # self.assertTrue(x)                bool(x) is True
        # self.assertFalse(x)               bool(x) is False
        # self.assertIs(a, b)               a is b    2.7
        # self.assertIsNot(a, b)            a is not b    2.7
        # self.assertIsNone(x)              x is None    2.7
        # self.assertIsNotNone(x)           x is not None    2.7
        # self.assertIn(a, b)               a in b    2.7
        # self.assertNotIn(a, b)            a not in b    2.7
        # self.assertIsInstance(a, b)       isinstance(a, b)    2.7
        # self.assertNotIsInstance(a, b)    not isinstance(a, b)    2.7


if __name__ == '__main__':
    unittest.main()

