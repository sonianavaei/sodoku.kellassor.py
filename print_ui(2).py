class PrintUI:
    def display_board(self, board, fixed_cells, error_cells):
        """
        Displays the Sudoku board with colors based on cell status.
        :param board: The Sudoku board (a 9x9 list of lists)
        :param fixed_cells: A 9x9 list of booleans indicating fixed cells
        :param error_cells: A 9x9 list of booleans indicating cells with errors
        """
        print("--- Sudoku Board ---")
        for i in range(9):  # Loop through each row
            if i % 3 == 0 and i != 0:  # Add a line every 3 rows
                print("---------------------")
            for j in range(9):  # Loop through each column
                if j % 3 == 0 and j != 0:  # Add a line every 3 columns
                    print("|", end=" ")
                # Print the number with appropriate color
                if error_cells[i][j]:
                    print(f"\033[91m{board[i][j] if board[i][j] != 0 else '.'}\033[0m", end=" ")  # Red for errors
                elif not fixed_cells[i][j] and board[i][j] != 0:
                    print(f"\033[93m{board[i][j]}\033[0m", end=" ")  # Yellow for new numbers
                else:
                    print(f"{board[i][j] if board[i][j] != 0 else '.'}", end=" ")  # White for fixed numbers
            print()  # Move to the next line after each row
        print()  # Add some space after the board

    def display_message(self, message):
        """
        Displays a message to the user.
        :param message: The message to display
        """
        print(message)
