class Menu:
    """Class for handling game menus and user choices.
    
    This class provides methods for displaying menus and handling user input
    for the start menu and end game menu.
    """
    
    # ========================
    # Menu Display Methods
    # ========================
    
    def start_menu(self):
        """Display the start menu and get user choice.
        
        Returns:
            str: '1' for Start Game, '2' for Quit Game
        """
        menu_text = """
        ========================
        | TIC-TAC-TOE GAME    |
        ========================
        |  1- Start Game      |
        |  2- Quit Game       |
        ========================
        Enter your choice (1 or 2): """
        
        return self._get_menu_choice(menu_text)
            
    def end_menu(self):
        """Display the end menu and get user choice.
        
        Returns:
            str: '1' for Restart Game, '2' for Quit Game
        """
        menu_text = """
        ========================
        |      GAME OVER      |
        ========================
        |  1- Restart Game    |
        |  2- Quit Game       |
        ========================
        Enter your choice (1 or 2): """
        
        return self._get_menu_choice(menu_text)
    
    # ========================
    # Helper Methods
    # ========================
    
    def _get_menu_choice(self, menu_text):
        """Helper method to get and validate a menu choice.
        
        Args:
            menu_text (str): The menu text to display
            
        Returns:
            str: The validated choice ('1' or '2')
        """
        while True:     
            choice = input(menu_text)
            if choice in ["1", "2"]:
                return choice
            print("Invalid choice! Please enter 1 or 2.")
                