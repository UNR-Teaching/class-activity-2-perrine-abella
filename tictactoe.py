""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    board = [['_','_','_'],['_','_','_'],['_','_','_']]

    def __init__(self):
        self.board = [['_','_','_'],['_','_','_'],['_','_','_']]
        pass

    def print_board(self):
        
        print (self.board[0][0] + " " + self.board[0][1] + " " + self.board[0][2])
        print (self.board[1][0] + " " + self.board[1][1] + " " + self.board[1][2])
        print (self.board[2][0] + " " + self.board[2][1] + " " + self.board[2][2])
        return self.board


    def mark_square(self, column, row, player):
        self.board[row][column] = player
        return self.board

    def check_rows(self):
        for i in range(2):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    return 1
                else:
                    return 2
        return 0 

    def check_cols(self):
        for i in range(2):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == 'X':
                    return 1
                else:
                    return 2
        return 0 

    def check_diags(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                return 1
            else:
                return 2 
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:       
            if self.board[0][2] == 'X':
                return 1
            else:
                return 2 
        else:
            return 0

    def has_winner(self):
        rows = self.check_rows()
        cols = self.check_cols()
        diags = self.check_diags()

        if rows != 0:
            return rows
        elif cols != 0:
            return cols 
        elif diags != 0:
            return diags
        else:
            return 0


    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        - play while there is no winner
        - ask for input from player 1
            - keep asking while not a valid input
        - ask for input from player 2
            - keep asking while not valid input
        check for winner and check if board is full
        
        :return: (str) the letter representing the player who won
        """
        
        pass
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
