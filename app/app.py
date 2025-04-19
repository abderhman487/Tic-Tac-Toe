import os

from player import Player
from menu import Menu
from board import Board

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Game:
    def __init__(self):
        
        self.players = [Player(),Player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0


    def setup_players(self):
        
        for number, player in enumerate(self.players,start=1):
            print(f"Player {number}, enter your detail: ")
            player.choose_name()
            player.choose_symbol
            clear_screen()
    

    def player_turn(self):
       
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice and cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        self.switch_player()
    

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        return self.current_player_index
                    

    def check_win(self):
        win_probs = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]
        ]
        for prob in win_probs:
            if (self.board.board[prob[0]]== self.board.board[prob[1]]==
                self.board.board[prob[3]]):
                return True
        return False
    

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
    

    def play_game(self):
        while True:
            self.player_turn()
            if self.check_win or self.check_draw:
                choise = self.menu.end_menu()
                if choise == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    

    def quit_game(self):
        print("Thanks for playing!")


    def start_game(self):
        choise = self.menu.start_menu()
        
        if choise == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()    
                 