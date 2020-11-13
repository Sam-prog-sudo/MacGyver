# encoding: utf-8
"""
Constants.py
"""
from constants import constants as C


class Characters:

    def __init__(self, name, position_X, position_Y, movable=False):
        self.name = name
        self.position_X = position_X
        self.position_Y = position_Y
        self.movable = movable

        self.display = C.DISPLAY[self.name]
        self.alive = True  # alive or dead/sleeping

    def disabled(self):
        self.state = False

    def move(self, direction):
        """
        Change position of movable characters.

        Character can collid with walls.

        Args:
            direction (str): direction to which the character is moving.
            VALID_DIRECTIONS (set): a set of strings of valid directions.

        Raises:
            ValueError: direction of movement
            can only be of set VALID_DIRECTIONS.
        """
        
        # position is not tuple anymore
        if direction in C.VALID_DIRECTIONS:

            if direction == 'up':
                self -= 1
            elif direction == 'down':
                temp_list[0] += 1
            if direction == 'left':
                temp_list[1] -= 1
            if direction == 'right':
                temp_list[1] += 1

            self.position = tuple(temp_list)

        else:
            raise ValueError(
                f"Direction can only be one of {C.VALID_DIRECTIONS}"
                )

    def on_right_pass(self, position, valid_positions):
        # macgyver, gard and items positions are valid
        if position in valid_positions:
            return True
        else:
            return False
