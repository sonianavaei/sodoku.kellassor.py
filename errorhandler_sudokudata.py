
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
