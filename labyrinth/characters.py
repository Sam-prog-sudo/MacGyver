# encoding: utf-8
"""
characters.py
"""
from assets import constants as C
from assets import display as d


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

    def up(self):
        return (self.position_Y - 1, self.position_X)

    def down(self):
        return (self.position_Y + 1, self.position_X)

    def right(self):
        return (self.position_Y, self.position_X + 1)

    def left(self):
        return (self.position_Y, self.position_X - 1)

    def move_char(self, direction, list_valid_path):
        """
        Change position of movable characters.

        Character cannot collid with walls or
        move outside the labyrinth.

        Args:
        - direction (str): direction to which the character is moving.
        - list_valid_path (list): a list of valid path.

        Returns:
        - bool: is this a valid movement ?.
        """

        if direction in C.VALID_DIRECTIONS:
            new_tuple_pos = getattr(self, direction)()
            condition = self.validate_move(
                    list_valid_path,
                    tuple_pos=new_tuple_pos
                    )

            if condition:
                self.position_Y = new_tuple_pos[0]
                self.position_X = new_tuple_pos[1]
                return condition
        else:
            print('{}'.format(direction)+d.inval_in)

    @staticmethod
    def validate_move(list_valid_path, tuple_pos):
        """
        Compare tuple of desired position with tuple of possible postions.

        Args:
        - tuple_pos (tuple): desired tuple postion to be compared.
        - list_valid_path (list): list of valid postion to compare with.

        Returns:
        - (bool): is desired postion in list of valid position ?
        """
        if tuple_pos not in list_valid_path:
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
