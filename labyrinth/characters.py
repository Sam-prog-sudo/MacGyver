# encoding: utf-8
"""
characters.py
"""
from assets import constants as C


class Characters:

    def __init__(self, name, position_X, position_Y, movable=False):
        self.name = name
        self.position_X = position_X
        self.position_Y = position_Y
        self.movable = movable
        self.display = C.DISPLAY[self.name]
        self.alive = True  # alive or dead/sleeping


    @property
    def position_tuple(self):
        return (self.position_Y, self.position_X)

    @property
    def disable(self):
        self.alive = False

    def move(self, direction, list_valid_path):
        """
        Change position of movable characters.

        Character cannot collid with walls or
        move outside the labyrinth.

        Args:
            direction (str): direction to which the character is moving.
            list_valid_path (list): a list of valid path.

        return:
            bool: whether or not character movement is permitted.

        Raises:
            ValueError: direction of movement
            can only be of (set) VALID_DIRECTIONS.
        """

        if direction in C.VALID_DIRECTIONS:

            if direction == 'up':
                new_pos = self.position_Y - 1
                self._validate_move_y(new_pos, list_valid_path)

            elif direction == 'down':
                new_pos = self.position_Y + 1
                self._validate_move_y(new_pos, list_valid_path)

            elif direction == 'left':
                new_pos = self.position_X - 1
                self._validate_move_x(new_pos, list_valid_path)

            else:
                new_pos = self.position_X + 1
                self._validate_move_x(new_pos, list_valid_path)

        else:
            raise ValueError(
                f"Direction can only be one of {C.VALID_DIRECTIONS}"
                )

    def _validate_move_x(self, pos_x, list_valid_path):
        """
        Compare character desired position with possible postions.

        Store character new position.

        Args:
            pos_x (int): desired postion to be compared.
            list_valid_path (list): list of valide postion to compare with.

        Returns:
            bool: whether or not new position is valid.
        """
        if (self.position_Y, pos_x) not in list_valid_path:
            print("Wrong way :(\n")
            return
        else:
            self.position_X = pos_x

    def _validate_move_y(self, pos_y, list_valid_path):
        """
        Compare character desired position with possible postions.

        Store character new position.

        Args:
            pos_y (int): desired postion to be compared.
            list_valid_path (list): list of valide postion to compare with.

        Returns:
            bool: whether or not new position is valid.
        """
        if (pos_y, self.position_X) not in list_valid_path:
            return
        else:
            self.position_Y = pos_y

    def pick_up_item(self, list_of_items):
        for an_item in list_of_items:
            if self.position_X == an_item.position_X:
                if self.position_Y == an_item.position_Y:
                    self.backpack.append(an_item.name)
                    an_item.state = 'found'
