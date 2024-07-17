# connect_four_corrected.py
# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

class ConnectFour:

    def __init__(self, board):
        """
        Initialize the ConnectFour game with a given board configuration.

        :param list[list[int]] board: List of lists representing the board configuration.
                                      0 = empty space, 1 = Player 1's piece, 2 = Player 2's piece.
        """
        self.board = board

    def check_winner(self, player):
        """
        Check if the given player has a winning position on the board.

        :param int player: Player number (1 or 2).
        :return bool: True if the player has a winning position, False otherwise.
        """
        # Check horizontal locations for win
        for row in range(len(self.board)):
            for col in range(len(self.board[0]) - 3):
                if all(self.board[row][col+i] == player for i in range(4)):
                    return True

        # Check vertical locations for win
        for col in range(len(self.board[0])):
            for row in range(len(self.board) - 3):
                if all(self.board[row+i][col] == player for i in range(4)):
                    return True

        # Check positively sloped diagonals
        for row in range(len(self.board) - 3):
            for col in range(len(self.board[0]) - 3):
                if all(self.board[row+i][col+i] == player for i in range(4)):
                    return True

        # Check negatively sloped diagonals
        for row in range(3, len(self.board)):
            for col in range(len(self.board[0]) - 3):
                if all(self.board[row-i][col+i] == player for i in range(4)):
                    return True

        return False

    def print_winner(self):
        """
        Print the board and the winner (if there is one).
        """
        print(*self.board, sep="\n")
        if self.check_winner(1):
            print("Player 1 wins!")
        elif self.check_winner(2):
            print("Player 2 wins!")
        else:
            print("No winner yet")
        print()


def main():
    """
    Main function to initialize board configurations and check for winners.
    """
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    game1 = ConnectFour(board1)
    game1.print_winner()

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    game2 = ConnectFour(board2)
    game2.print_winner()

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    game3 = ConnectFour(board3)
    game3.print_winner()


if __name__ == "__main__":
    main()
