# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game built with Python.

## Features

- Two-player gameplay
- Interactive command-line interface
- Player name customization
- First player chooses X or O symbol, second player gets the opposite symbol automatically
- Game state detection (win/draw)
- Option to restart or quit after game ends

## Project Structure

```
tic-tac-toe/
├── app/
│   ├── app.py       # Main game logic
│   ├── board.py     # Board representation and operations
│   ├── menu.py      # Game menus
│   └── player.py    # Player class
└── main.py          # Entry point
```

## Requirements

- Python 3.6 or higher

## How to Run

1. Clone the repository:
```
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

2. Run the game:
```
python main.py
```

## How to Play

1. Start the game and follow the on-screen prompts
2. Each player will be asked to enter their name
3. Player 1 chooses their symbol (X or O), and Player 2 automatically gets the opposite symbol
4. Players take turns selecting a cell (1-9) to place their symbol
5. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins
6. If all cells are filled without a winner, the game ends in a draw

## Game Controls

- Choose menu options by entering the corresponding number (1 or 2)
- Select a cell on the board by entering a number from 1 to 9:
```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
```

## Future Improvements

- Add computer opponent with different difficulty levels
- Implement a graphical user interface
- Add player statistics tracking
- Support for larger board sizes

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Thanks to everyone who enjoys simple games!
- Special thanks to the Python community for making programming fun. 