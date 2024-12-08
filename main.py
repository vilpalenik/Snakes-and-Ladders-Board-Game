from grid import Grid
from game import Game

if __name__ == "__main__":
    print('''
---------------------------------------------------------------------
This program simulates the Snakes and Ladders Board Game.
The program generates n//2 positive and negative teleports.
- Positive teleports (uppercase letters) move the player forward.
- Negative teleports (lowercase letters) move the player backward.
---------------------------------------------------------------------
''')
    # Input: Board size (n) and number of players (k)
    print('Enter n parameter (playing field size): ', end='')
    n = int(input())
    print('Enter k parameter (number of players): ', end='')
    k = int(input())
    print('\n*************************** start of the game ***************************')

    # Initialize the game board (Grid) and the game logic (Game)
    grid = Grid(n)
    game = Game(k, grid)
    game.start_game()