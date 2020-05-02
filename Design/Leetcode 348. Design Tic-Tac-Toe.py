class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.cols = [0]*n
        self.rows = [0]*n
        self.diag = 0
        self.rev_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        add = 0
        if player == 1:
            add = 1
        else:
            add = -1
        self.rows[row]+=add
        self.cols[col]+=add
        if row == col:
            self.diag += add
        if row+col == self.n-1:
            self.rev_diag += add
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.rev_diag) == self.n:
            return player
        return 0