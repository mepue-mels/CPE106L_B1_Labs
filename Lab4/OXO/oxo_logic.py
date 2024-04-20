''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import os
import random
import oxo_data

class Game:
    """
    Represents a game of Tic Tac Toe.
    """

    def __init__(self):
        """
        Initializes a new game with an empty board.
        """
        self.board = list(" " * 9)

    def saveGame(self):
        """
        Saves the current game state to disk.
        """
        oxo_data.saveGame(self.board)

    def restoreGame(self):
        """
        Attempts to restore a previously saved game.
        If unsuccessful, returns a new game.
        """
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
                return self
            else:
                return Game()
        except IOError:
            return Game()

    def _generateMove(self):
        """
        Generates a random available cell on the board.
        Returns -1 if the board is full.
        """
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _isWinningMove(self):
        """
        Checks if the current board state represents a winning move for a player.
        """
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        """
        Places a user move on the board at the specified cell.
        Raises ValueError if the cell is already occupied.
        Returns the winning player if the move resulted in a win, otherwise empty string.
        """
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(self):
        """
        Places a computer move on the board using a random available cell.
        Returns 'D' if the board is full, the winning player if the move resulted in a win, otherwise empty string.
        """
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""

    def __str__(self):
        """
        Defines how to print the game board in a user-friendly format.
        """
        board_str = ""
        for i in range(3):
            board_str += " ".join(self.board[i * 3:(i * 3) + 3]) + "\n"
        return board_str[:-1]

def test():
    result = ""
    game = Game()
    while not result:
        print(game)
        try:
           result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
            
        if not result: continue
        elif result == 'D':
            print("Its a draw")
        else:
            print("Winner is:", result)
        print(game)

if __name__ == "__main__":
    test()