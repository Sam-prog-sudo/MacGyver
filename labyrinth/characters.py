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
        self.sleeping = False
        if self.name == 'macgyver':
            self.backpack = []

    @property
    def position_tuple(self):
        return (self.position_Y, self.position_X)

    def disable(self):
        """
        Wishes a character goodnight.
        """
        self.sleeping = True

    def move_char(self, direction, list_valid_path):
        """
        Change position of movable characters.

        Character cannot collid with walls or
        move outside the labyrinth.

        Args:
        - direction (str): direction to which the character is moving.
        - list_valid_path (list): a list of valid path.

        Raises:
        - ValueError: direction of movement
            can only be of (set) VALID_DIRECTIONS.
        """

        if direction in C.VALID_DIRECTIONS:

            if direction == 'up':
                new_pos = self.position_Y - 1
                condition = self.validate_move(
                    list_valid_path,
                    pos_x=self.position_X,
                    pos_y=new_pos,
                    )
                if condition:
                    self.position_Y = new_pos
                    return condition

            elif direction == 'down':
                new_pos = self.position_Y + 1
                condition = self.validate_move(
                    list_valid_path,
                    pos_x=self.position_X,
                    pos_y=new_pos,
                    )
                if condition:
                    self.position_Y = new_pos
                    return condition

            elif direction == 'left':
                new_pos = self.position_X - 1
                condition = self.validate_move(
                    list_valid_path,
                    pos_x=new_pos,
                    pos_y=self.position_Y,
                    )
                if condition:
                    self.position_X = new_pos
                    return condition

            elif direction == 'right':
                new_pos = self.position_X + 1
                condition = self.validate_move(
                    list_valid_path,
                    pos_x=new_pos,
                    pos_y=self.position_Y,
                    )
                if condition:
                    self.position_X = new_pos
                    return condition
            else:
                print(f"Wrong input: {direction}")

    @staticmethod
    def validate_move(list_valid_path, pos_x, pos_y):
        """
        Compare tuple of desired position with tuple of possible postions.

        Store character new position.

        Args:
        - pos_x (int): desired postion_x to be compared.
        - pos_y (int): desired postion_y to be compared.
        - list_valid_path (list): list of valid postion to compare with.

        Returns:
        - (bool): is desired postion in list of valid position ?
        """
        if (pos_y, pos_x) not in list_valid_path:
            print("Wrong way :(\n")
            return False
        else:
            return True

    def pick_up_item(self, an_item):
        """
        pick_up_item store an_item into macgyver's backpack.

        Args:
        - an_item (object): a pickable item.
        """
        self.backpack.append(an_item)
