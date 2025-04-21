import os

from app.player import Player
from app.menu import Menu
from app.board import Board

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

class Game:
    """Main game class that controls the Tic-Tac-Toe game flow."""
    
    def __init__(self):
        """Initialize the game with empty players, menu, board and set player index."""
        self.players = [Player("", ""), Player("", "")]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0

    # ========================
    # Game Flow Management
    # ========================
    
    def start_game(self):
        """Start the game by showing the main menu and handling user choice."""
        choice = self.menu.start_menu()
        
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        """Setup player names and symbols for both players.
        The second player's symbol is automatically assigned as the opposite of the first player's choice.
        """
        # Set up first player
        print(f"Player 1, enter your details: ")
        self.players[0].choose_name()
        self.players[0].choose_symbol()
        clear_screen()
        
        # Set up second player
        print(f"Player 2, enter your details: ")
        self.players[1].choose_name()
        
        # Automatically assign the opposite symbol to the second player
        opposite_symbol = "O" if self.players[0].symbol == "X" else "X"
        self.players[1].symbol = opposite_symbol
        print(f"{self.players[1].name}, you will play with {opposite_symbol}.")
        input("Press Enter to continue...")
        clear_screen()

    def play_game(self):
        """Main game loop that controls the flow of the game."""
        while True:
            # Player makes their move
            self.player_turn()
            
            # Get previous player (who just played)
            previous_player_index = 1 - self.current_player_index
            previous_player = self.players[previous_player_index]
            
            # Check for win condition
            if self.check_win():
                self.board.display_board()
                print(f"Congratulations! {previous_player.name} won the game!")
                
                choice = self.menu.end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
                    
            # Check for draw condition
            elif self.check_draw():
                self.board.display_board()
                print("The game ended in a draw!")
                
                choice = self.menu.end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        """Reset the game board and start a new game."""
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        """Display exit message and end the game."""
        print("Thanks for playing!")

    # ========================
    # Player Turn Management
    # ========================

    def player_turn(self):
        """Handle a single player's turn."""
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        
        # Switch to the next player after a valid move
        self.switch_player()

    def switch_player(self):
        """Switch the current player index between 0 and 1."""
        self.current_player_index = 1 - self.current_player_index
        return self.current_player_index
    
    # ========================
    # Game State Checking
    # ========================

    def check_win(self):
        """Check if the current board state has a winning condition."""
        win_patterns = [
            # Rows
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columns
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonals
            [0, 4, 8], [2, 4, 6]
        ]
        
        for pattern in win_patterns:
            if (self.board.board[pattern[0]] == self.board.board[pattern[1]] == 
                self.board.board[pattern[2]] and not self.board.board[pattern[0]].isdigit()):
                return True
        return False

    def check_draw(self):
        """Check if the game is a draw (all cells filled with no winner)."""
        return all(not cell.isdigit() for cell in self.board.board)
                 