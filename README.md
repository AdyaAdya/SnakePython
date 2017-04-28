# SnakePython
Snake-like game written in Python on Bash Unix-based terminal
(written in python3.5)

Just a tiny game to practice a bit my Python.

It has been designed on Ubuntu 16.04 LTS and not tested anywhere else, so it probably won't work properly on other platforms especially Windows since the Windows console isn't designed for this kind of use at all.

To run the game: clone the repository, go to the new folder and enter into the terminal : "./Snake" or "./Snake settings" in order to custom your game settings

# Tree view

root
|
|---bin
|   |
|   |---Snake               : Executable file created from src/Snake.py with pyinstaller3
|   |
|   |---SnakeSettings       : Executable file created from src/SnakeSettings.py with pyinstaller3
|
|---src
|   |
|   |---obj
|   |   |
|   |   |---SnakeClasses.py : Python file that contains game classes Arena, Snake, Stats and Keybinding
|   |   |
|   |   |---SnakeFrame.py   : Python file that contains the Frame class
|   |   |
|   |   |---SnakeGetch.py   : Python file that contains the Getch, GetchUnix and GetchWindows classes
|   |   |
|   |   |---SnakeThread.py  : Python file that contains the InputManager Thread-inherit class
|   |
|   |---Snake.py            : Python file that contains the main game loop
|   |
|   |---SnakeSettings.py    : Python file that contains the game settings customization
|
|---Snake                   : Bash file that runs either bin/Snake or bin/SnakeSettings depending of the argument
