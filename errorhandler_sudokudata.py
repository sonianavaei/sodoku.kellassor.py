class ErrorHandler:
    def check_error(self, board, row, col, num):
        # Check if the number is valid in the given row, column, and 3x3 box
        if num in board[row]:
            return f"Number {num} is repeated in row {row}."
        for i in range(9):
            if board[i][col] == num:
                return f"Number {num} is repeated in column {col}."
        
        # Check the 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return f"Number {num} is repeated in the 3x3 box."
        return None
class SudokuData:
    def __init__(self):
        # Predefined Sudoku boards for different difficulty levels
 self.easy_boards = [
            [
                [0, 0, 3, 0, 2, 0, 6, 0, 0],
                [9, 0, 0, 3, 0, 5, 0, 0, 1],
                [0, 0, 1, 8, 0, 6, 4, 0, 0],
                [0, 0, 8, 1, 0, 2, 9, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 8],
                [0, 0, 6, 7, 0, 8, 2, 0, 0],
                [0, 0, 2, 6, 0, 9, 5, 0, 0],
                [8, 0, 0, 2, 0, 3, 0, 0, 9],
                [0, 0, 5, 0, 1, 0, 3, 0, 0]
            ]
        ]
        self.medium_boards = [
            [
                [0, 2, 0, 6, 0, 8, 0, 0, 0],
                [5, 0, 0, 0, 0, 9, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [1, 3, 0, 0, 0, 0, 7, 4, 0],
                [0, 0, 0, 2, 0, 0, 0, 0, 6],
                [0, 0, 0, 3, 0, 6, 0, 9, 0]
            ]
        ]
        self.hard_boards = [
            [
                [0, 0, 0, 6, 0, 0, 4, 0, 0],
                [7, 0, 0, 0, 0, 3, 6, 0, 0],
                [0, 0, 0, 0, 9, 1, 0, 8, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 5, 0, 1, 8, 0, 0, 0, 3],
                [0, 0, 0, 3, 0, 6, 0, 4, 5],
                [0, 4, 0, 2, 0, 0, 0, 6, 0],
                [9, 0, 3, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 1, 0, 0]
            ]
        ]
