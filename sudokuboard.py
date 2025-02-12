class SudokuBoard:
    def __init__(self, board):
        # Initialize the Sudoku board
        self.board = board

    def update_cell(self, row, col, number):
        # Check if the cell is empty and update it with the new number
        if self.board[row][col] == 0:
            self.board[row][col] = number
            return True
        return False

    def is_complete(self):
        # Check if the board is fully filled (no zeros left)
        for row in self.board:
            if 0 in row:
                return False
        return True
