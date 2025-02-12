class SudokuBoard:
    def __init__(self, board):
        # Initialize the Sudoku board
        self.board = board
        # Track which cells are fixed (pre-filled) and which are new
        self.fixed_cells = [[cell != 0 for cell in row] for row in board]
        # Track which cells have errors (duplicate numbers)
        self.error_cells = [[False for _ in row] for row in board]

    def update_cell(self, row, col, number):
        # Check if the cell is empty and update it with the new number
        if not self.fixed_cells[row][col]:
            self.board[row][col] = number
            # Check for errors after updating the cell
            self.error_cells[row][col] = self.check_for_errors(row, col, number)
            return True
        return False

    def is_complete(self):
        # Check if the board is fully filled (no zeros left)
        for row in self.board:
            if 0 in row:
                return False
        return True

    def check_for_errors(self, row, col, number):
        # Check if the number is valid in the given row, column, and 3x3 box
        if number == 0:
            return False
        # Check row
        if self.board[row].count(number) > 1:
            return True
        # Check column
        if [self.board[i][col] for i in range(9)].count(number) > 1:
            return True
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == number and (start_row + i != row or start_col + j != col):
                    return True
        return False

