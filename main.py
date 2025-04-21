import sys
import os

# Add the current directory to the search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.app import Game

if __name__ == "__main__":
    game = Game()
    game.start_game() 