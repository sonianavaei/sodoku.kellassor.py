class SudokuGenerator:
    def __init__(self, data):
        self.data = data

    def generate_board(self, level):
        # Return a Sudoku board based on the chosen difficulty (level)
        if level == "easy":
            return self.data.easy_boards[0]
        elif level == "medium":
            return self.data.medium_boards[0]
        elif level == "hard":
            return self.data.hard_boards[0]
        else:
            return self.data.easy_boards[0]  # Default to easy
