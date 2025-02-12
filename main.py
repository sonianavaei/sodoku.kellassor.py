from sudoku_board import SudokuBoard
from sudoku_generator import SudokuGenerator
from sudoku_data import SudokuData
from ui import PrintUI
import time

class GameStarter:
    def __init__(self):
        # Initialize the components
        self.ui = PrintUI()
        self.data = SudokuData()
        self.generator = SudokuGenerator(self.data)
        self.start_time = None

    def start_the_game(self):
        print("Welcome to Sudoku!")
        # Ask the player to choose the difficulty level
        level = input("Choose difficulty (easy, medium, hard): ").lower()

        # Validate the input
        while level not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")
            level = input("Choose difficulty (easy, medium, hard): ").lower()

        # Generate the Sudoku board based on the chosen difficulty
        board = self.generator.generate_board(level)
        self.board = SudokuBoard(board)
        self.start_time = time.time()

        # Display the initial Sudoku board
        self.ui.display_board(self.board.board, self.board.fixed_cells, self.board.error_cells)

        # Start the game loop
        self.player_turn()

    def player_turn(self):
        # Check if the board is complete
        if self.board.is_complete():
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            print(f"Congratulations! You've completed the Sudoku puzzle in {elapsed_time:.2f} seconds!")
            return

        # Get the player's input for row, column, and number
        try:
            row = int(input("Enter row (1-9): ")) - 1
            column = int(input("Enter column (1-9): ")) - 1
            number = int(input("Enter number (1-9): "))

            # Validate the number
            if number < 1 or number > 9:
                print("Please enter a number between 1 and 9.")
                self.player_turn()  # Recursive call to continue the game
                return

            # Try to update the cell with the new number
            if self.board.update_cell(row, column, number):
                self.ui.display_board(self.board.board, self.board.fixed_cells, self.board.error_cells)
            else:
                print("Cell is already filled. Try another cell.")

            # Continue the game
            self.player_turn()

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            self.player_turn()  # Recursive call to continue the game


# Entry point of the game
if __name__ == "__main__":
    game = GameStarter()
    game.start_the_game()

