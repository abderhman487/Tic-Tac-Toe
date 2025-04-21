class Player:
    """Class representing a player in the Tic-Tac-Toe game.
    
    A player has a name and a symbol (X or O) that they use to mark their moves on the board.
    """
    
    def __init__(self, name, symbol):
        """Initialize a player with name and symbol.
        
        Args:
            name (str): The player's name
            symbol (str): The player's game symbol (X or O)
        """
        self.name = name
        self.symbol = symbol
    
    # ========================
    # Player Setup Methods
    # ========================
    
    def choose_name(self):
        """Prompt the player to choose a valid name (letters only).
        
        The name must contain only alphabetic characters.
        """
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name! \nPlease use letters only")
    
    def choose_symbol(self):
        """Prompt the player to choose a valid symbol (X or O).
        
        This is only used for the first player. The second player's symbol
        is automatically assigned as the opposite of the first player's choice.
        """
        while True:
            symbol = input(f"{self.name}, choose your symbol (X or O): ")
            # Convert to uppercase for better comparison
            symbol = symbol.upper()
            
            if len(symbol) == 1 and symbol in ['X', 'O']:
                self.symbol = symbol
                break
            print("Invalid symbol! \nPlease enter X or O")
            


