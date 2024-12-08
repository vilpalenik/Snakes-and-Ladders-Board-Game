from random import randint

class Player:
    def __init__(self, name: str):
        """
        Initialize a player with:
        - A unique name.
        - Roll history.
        - Current and previous positions.
        """
        self.name = name
        self.rolls = []
        self.current_position = [0, 0]
        self.positions = []

    def roll_dice(self):
        """
        Simulate rolling a dice. Rolls of 6 allow additional rolls.
        Sum the total roll value.
        """
        total_roll = 0
        roll = randint(1, 6)
        while roll == 6:
            total_roll += roll
            roll = randint(1, 6)
        self.rolls.append(total_roll + roll)

    def move_to_position(self, position: list):
        # Update the player's current position and record previous positions.

        self.positions.append(self.current_position[:])
        self.current_position = position[:]