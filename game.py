from grid import Grid
from player import Player

class Game:
    def __init__(self, players: int, grid: Grid):
        # Initialize the game with a specified number of players and a grid.

        self.players = [Player(name=f"Player{i + 1}") for i in range(players)]
        self.grid = grid

    def start_game(self):
        """
        Run the game loop:
        - Players take turns rolling dice and moving.
        - Print the grid and player statuses after each turn.
        - End the game when a player reaches the finish.
        """
        game_over = False
        round_num = 0
        while not game_over:
            round_num += 1
            print(f"This is round {round_num}:\n")
            for player in self.players:
                # Display grid and player positions
                positions = [p.current_position for p in self.players]
                self.grid.print_grid(positions)
                print(f"Player positions:\n" + "\n".join(
                    f"{p.name}: {p.current_position}" for p in self.players
                ))
                print("----------------")

                # Roll dice and move the player
                player.roll_dice()
                new_pos = self.grid.calculate_player_move(player.current_position, player.rolls[-1], player)
                player.move_to_position(new_pos)
                print()

                # Check for win condition
                if player.current_position == self.grid.finish:
                    print(f"Player {player.name} wins!")
                    self.grid.print_grid([p.current_position for p in self.players])
                    game_over = True
                    break
        print("Game over!")