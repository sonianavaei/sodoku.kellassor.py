import time

class SudokuBoard:
    def __init__(self, board):
        self.board = board
        self.fixed_cells = [[cell != 0 for cell in row] for row in board]
        self.error_cells = [[False for _ in row] for row in board]

    def update_cell(self, row, col, number):
        if not self.fixed_cells[row][col]:
            self.board[row][col] = number
            self.error_cells[row][col] = self.check_for_errors(row, col, number)
            return True
        return False

    def is_complete(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def check_for_errors(self, row, col, number):
        if number == 0:
            return False
        if self.board[row].count(number) > 1:
            return True
        if [self.board[i][col] for i in range(9)].count(number) > 1:
            return True
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == number and (start_row + i != row or start_col + j != col):
                    return True
        return False

class SudokuGenerator:
    def __init__(self, data):
        self.data = data

    def generate_board(self, level):
        if level == "easy":
            return self.data.easy_boards[0]
        elif level == "medium":
            return self.data.medium_boards[0]
        elif level == "hard":
            return self.data.hard_boards[0]
        else:
            return self.data.easy_boards[0]

class SudokuData:
    def __init__(self):
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

class PrintUI:
    def display_board(self, board, fixed_cells, error_cells):
        print("--- Sudoku Board ---")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("---------------------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                if error_cells[i][j]:
                    print(f"\033[91m{board[i][j] if board[i][j] != 0 else '.'}\033[0m", end=" ")
                elif not fixed_cells[i][j] and board[i][j] != 0:
                    print(f"\033[93m{board[i][j]}\033[0m", end=" ")
                else:
                    print(f"{board[i][j] if board[i][j] != 0 else '.'}", end=" ")
            print()
        print()

    def display_message(self, message):
        print(message)

class GameStarter:
    def __init__(self):
        self.ui = PrintUI()
        self.data = SudokuData()
        self.generator = SudokuGenerator(self.data)
        self.start_time = None

    def start_the_game(self):
        print("Welcome to Sudoku!")
        level = input("Choose difficulty (easy, medium, hard): ").lower()
        while level not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")
            level = input("Choose difficulty (easy, medium, hard): ").lower()
        board = self.generator.generate_board(level)
        self.board = SudokuBoard(board)
        self.start_time = time.time()
        self.ui.display_board(self.board.board, self.board.fixed_cells, self.board.error_cells)
        self.player_turn()

    def player_turn(self):
        if self.board.is_complete():
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            print(f"Congratulations! You've completed the Sudoku puzzle in {elapsed_time:.2f} seconds!")
            return
        try:
            row = int(input("Enter row (1-9): ")) - 1
            column = int(input("Enter column (1-9): ")) - 1
            number = int(input("Enter number (1-9): "))
            if number < 1 or number > 9:
                print("Please enter a number between 1 and 9.")
                self.player_turn()
                return
            if self.board.update_cell(row, column, number):
                self.ui.display_board(self.board.board, self.board.fixed_cells, self.board.error_cells)
            else:
                print("Cell is already filled. Try another cell.")
            self.player_turn()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            self.player_turn()

if __name__ == "__main__":
    game = GameStarter()
    game.start_the_game()
