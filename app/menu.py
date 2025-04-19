class Menu:
    def start_menu():
        menu_text = """
            Welcome to Tic-Tac-Toe game!
            1- Start Game
            2- Quit Game
            Enter your choice (1 or 2): """
        while True:     
            choise = input(menu_text)
            if choise == "1" or choise == "2":
                return choise
                break
            print("Invalid choise!")
            
            
    def end_menu():
        menu_text = """
            Game Over!
            1- Restart Game
            2- Quit Game
            Enter your choice (1 or 2): """
        while True:     
            choise = input(menu_text)
            if choise == "1" or choise == "2":
                return choise
                break
            print("Invalid choise!")            
                