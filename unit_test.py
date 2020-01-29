import unittest
from tictactoe import Board

class TestTicTacToeMethods(unittest.TestCase):

    def test_print_board(self):
        board = Board()
        expected = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.assertEqual(board.print_board(), expected)

    def test_mark_square_X_in_0_0(self):
        board = Board()
        expected = [['X','_','_'],['_','_','_'],['_','_','_']]
        self.assertEqual(board.mark_square(0,0,"X"), expected)

    def test_mark_square_O_in_0_0(self):
        board = Board()
        expected = [['O','_','_'],['_','_','_'],['_','_','_']]
        self.assertEqual(board.mark_square(0,0,"O"), expected)

    def test_mark_square_X_in_1_1(self):
        board = Board()
        expected = [['_','_','_'],['_','X','_'],['_','_','_']]
        self.assertEqual(board.mark_square(1,1,"X"), expected)

    def test_mark_square_O_in_1_1(self):
        board = Board()
        expected = [['_','_','_'],['_','O','_'],['_','_','_']]
        self.assertEqual(board.mark_square(1,1,"O"), expected)

    def test_mark_square_X_in_2_2(self):
        board = Board()
        expected = [['_','_','_'],['_','_','_'],['_','_','X']]
        self.assertEqual(board.mark_square(2,2,"X"), expected)

    def test_mark_square_O_in_2_2(self):
        board = Board()
        expected = [['_','_','_'],['_','_','_'],['_','_','O']]
        self.assertEqual(board.mark_square(2,2,"O"), expected)

    def test_check_rows_X_in_row_0(self):
        myBoard = Board()
        myBoard.board = [['X','X','X'],['_','_','_'],['_','_','_']]
        self.assertEqual(myBoard.check_rows(), 1)

    def test_check_rows_O_in_row_2(self):
        myBoard = Board()
        myBoard.board = [['_','_','_'],['_','_','_'],['O','O','O']]
        self.assertEqual(myBoard.check_rows(), 2)

    def test_check_rows_no_winner(self):
        myBoard = Board()
        myBoard.board = [['_','_','O'],['X','_','_'],['X','O','O']]
        self.assertEqual(myBoard.check_rows(), 0)

    def test_check_cols_X_in_cols_0(self):
        myBoard = Board()
        myBoard.board = [['X','_','_'],['X','_','_'],['X','_','_']]
        self.assertEqual(myBoard.check_cols(), 1)

    def test_check_cols_0_in_cols_2(self):
        myBoard = Board()
        myBoard.board = [['_','_','O'],['_','_','O'],['_','_','O']]
        self.assertEqual(myBoard.check_cols(), 2)

    def test_check_diags_X_in_neg_diag(self):
        myBoard = Board()
        myBoard.board = [['X','_','_'],['_','X','_'],['_','_','X']]
        self.assertEqual(myBoard.check_diags(), 1)

    def test_check_diags_0_in_pos_diag(self):
        myBoard = Board()
        myBoard.board = [['_','_','O'],['_','O','_'],['O','_','_']]
        self.assertEqual(myBoard.check_diags(), 2)

    def test_check_diags_no_winner(self):
        myBoard = Board()
        myBoard.board = [['O','_','X'],['_','O','_'],['O','X','_']]
        self.assertEqual(myBoard.check_diags(), 0)

    def test_has_winner_X(self):
        myBoard = Board()
        myBoard.board = [['X','X','X'],['_','_','_'],['_','_','_']]
        self.assertEqual(myBoard.has_winner(), 1)

    def test_has_winner_O(self):
        myBoard = Board()
        myBoard.board = [['O','O','O'],['_','_','_'],['_','_','_']]
        self.assertEqual(myBoard.has_winner(), 2)

    def test_has_winner_None(self):
        myBoard = Board()
        myBoard.board = [['X','O','X'],['O','X','_'],['_','_','_']]
        self.assertEqual(myBoard.has_winner(), 0)
    
    

if __name__ == '__main__':
    unittest.main()
