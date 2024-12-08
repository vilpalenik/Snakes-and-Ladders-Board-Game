from random import randint

class Grid:
    def __init__(self, n: int):
        """
        Initialize the game grid with the specified size (n x n).
        - Sets the start and finish positions.
        - Generates n//2 positive and negative teleports.
        """
        self.n = n
        self.start = [0, 0]
        self.positive_teleports = []
        self.negative_teleports = []
        # Determine finish position based on grid size
        self.finish = [0, n-1] if n % 2 == 0 else [n-1, n-1]
        
        # Generate teleports
        for _ in range(n // 2):
            self.generate_positive_teleport()
            self.generate_negative_teleport()

    def generate_negative_teleport(self):
        """
        Generate a negative teleport (backward movement) 
        with valid random start and end positions.
        """
        start, end = self.generate_random_coordinates(), self.generate_random_coordinates()
        while not self.valid_teleport(start, end, False) or not self.check_teleport_coordinates(start, end):
            start, end = self.generate_random_coordinates(), self.generate_random_coordinates()
        self.negative_teleports.append([start, end])

    def generate_positive_teleport(self):
        """
        Generate a positive teleport (forward movement)
        with valid random start and end positions.
        """
        start, end = self.generate_random_coordinates(), self.generate_random_coordinates()
        while not self.valid_teleport(start, end, True) or not self.check_teleport_coordinates(start, end):
            start, end = self.generate_random_coordinates(), self.generate_random_coordinates()
        self.positive_teleports.append([start, end])

    def valid_teleport(self, start: list, end: list, positive: bool) -> bool:
        """
        Check teleport validity:
        - Positive teleport: start position must be earlier than the end position.
        - Negative teleport: start position must be later than the end position.
        """
        return start[1] < end[1] if positive else start[1] > end[1]

    def check_teleport_coordinates(self, start: list, end: list) -> bool:
        # A teleport is valid if positives start earlier and negatives start later than their end positions.

        if start in [self.start, self.finish] or end in [self.start, self.finish] or start == end:
            return False
        for teleport in self.positive_teleports + self.negative_teleports:
            if start in teleport or end in teleport:
                return False
        return True

    def generate_random_coordinates(self) -> list:
        # Generate random x, y coordinates on the grid.

        return [randint(0, self.n - 1), randint(0, self.n - 1)]

    def get_cell_content(self, x: int, y: int, player_positions=[]) -> str:
        # Return the content of a specific grid cell:
        
        if [x, y] == self.start:
            return '+'
        for i, pos in enumerate(player_positions):
            if [x, y] == pos:
                return str(i + 1)
        if [x, y] == self.finish:
            return '*'
        for idx, pt in enumerate(self.positive_teleports):
            if [x, y] in pt:
                return chr(ord('A') + idx)
        for idx, nt in enumerate(self.negative_teleports):
            if [x, y] in nt:
                return chr(ord('a') + idx)
        return '.'

    def print_grid(self, player_positions=[]):
        # Display the current state of the grid, including players and teleports.

        print('  ' + ' '.join(str(i) for i in range(self.n)))
        for y in range(self.n):
            print(str(y) + ' ' + ' '.join(self.get_cell_content(x, y, player_positions) for x in range(self.n)))

    def calculate_player_move(self, start_position, nr_of_steps, player):
        """
        Calculate the player's new position based on dice rolls, grid layout, 
        and teleports. Handle edge cases like exceeding grid bounds.
        """
        col, row = start_position
        print(f"Player {player.name} rolled: {player.rolls[-1]}")
        while nr_of_steps > 0:
            if row % 2 == 0:  # Even rows: left-to-right
                steps = min(nr_of_steps, self.n - 1 - col)
                col += steps
            else:  # Odd rows: right-to-left
                steps = min(nr_of_steps, col)
                col -= steps
            nr_of_steps -= steps
            if nr_of_steps > 0:  # Move to the next row if steps remain
                row += 1
                if row >= self.n:
                    print(f"Player {player.name} rolled too far and stays at {start_position}.")
                    return start_position
                nr_of_steps -= 1

        print(f"Player {player.name} moves to: {[col, row]}")
        for teleport in self.positive_teleports + self.negative_teleports:
            if [col, row] == teleport[0]:
                print(f"Player {player.name} uses teleport to: {teleport[1]}")
                return teleport[1]
        return [col, row]