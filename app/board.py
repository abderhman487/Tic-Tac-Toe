class Board:
    """Class representing the Tic-Tac-Toe game board.
    
    The board is represented as a list of 9 strings, where each string
    is either a digit (1-9) representing an empty cell, or a player symbol
    (X or O) representing a played move.
    """
    
    def __init__(self):
        """Initialize the board with numbers 1-9 as strings."""
        self.board = [str(i) for i in range(1, 10)]
    
    # ========================
    # Board Display Methods
    # ========================
        
    def display_board(self):
        """Display the current state of the board in a formatted way.
        
        The board is displayed as a 3x3 grid with cell numbers or player symbols.
        """
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-" * 11)
        print("\n")

    # ========================
    # Board Update Methods
    # ========================

    def is_valid_move(self, choice):
        """Check if a move is valid (cell contains a digit).
        
        Args:
            choice (int): The cell number (1-9)
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        return 1 <= choice <= 9 and self.board[choice-1].isdigit()
    
    def update_board(self, choice, symbol):
        """Update the board with a player's move.
        
        Args:
            choice (int): The cell number (1-9)
            symbol (str): The player's symbol (X or O)
            
        Returns:
            bool: True if board was updated, False if move was invalid
        """
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False    

    def reset_board(self):
        """Reset the board to its initial state with numbers 1-9."""
        self.board = [str(i) for i in range(1, 10)]