# encoding: utf-8

# deplacement + affichage
"""
maze.py
"""
import random
from a_maze_ing import constants as C
from a_maze_ing.characters import Characters
from a_maze_ing.items import SomeItem


class Maze:

    def __init__(self):
        self.dict_display = {}
        self.list_walls = []
        self.list_paths = []
        self.list_items = []
        # self.macgyver
        # self.gard

        # self.create_lab_elements()
        # self.list_items = self.create_list_items()

        # self.dict_display = self.create_dict_to_display()

    def create_lab_elements(self):
        """
        [summary]
        """

        with open(C.FILENAME, 'r') as m:
            row = 0                         # row number
            for line in m:
                column = 0                  # column number

                for char in line:
                    if char != '\n':

                        if char == C.DISPLAY['wall']:
                            self.list_walls.append(
                                    (row, column)
                                )

                        elif char == C.DISPLAY['start']:
                            self.macgyver = Characters(
                                name='macgyver',
                                position=(row, column)
                                )

                        elif char == C.DISPLAY['finish']:
                            self.gard = Characters(
                                name='gard',
                                position=(row, column)
                                )

                    column += 1             # column increment
                row += 1                    # row increment

    def print_lab(self):
        for i in range(0, C.DIMENSION['height']-1):
            for j in range(0, C.DIMENSION['width']-1):
                if (i, j) in self.list_walls:
                    print('x', end='')
                elif self.macgyver.position == (i, j):
                    print('m', end='')
                elif self.gard.position == (i, j):
                    print('g', end='')
                else:
                    print(' ', end='')
            print('')

    def create_list_items(self):
        """
        Create a list of pickable items

        Will angry the snake god if instantiate before __create_lab_elements().

        Returns:
            list_items (list): a list of pickable items.
        """

        for a_name in C.CHOICE_ITEMS['name']:
            if a_name != 'syringe':

                self.list_items.append(
                    SomeItem(
                        name=a_name,
                        position=self.pick_random(self.list_paths)
                        )
                    )
        return self.list_items

    def create_dict_to_display(self):
        """
        Initialize a dictionnary of lab elements to display.

        The element position is passed as key of dict
        and its representation as a value assigned to said key.

        Returns:
            dict_display (dict): dictionnary of element to display.
        """
        attr_list = [
            self.list_walls +
            self.list_paths +
            self.list_items +
            self.list_items
            ]
        attr_list.extend((self.macgyver, self.gard))

        for elt in attr_list:
            if type(elt) is list:
                for item in elt:
                    self.dict_display[item.position] = item.display
            else:
                self.dict_display[elt.position] = elt.display
            return self.dict_display

    # print dict values in console with dict keys
    def display(self):
        for key in self.dict_display.keys():
            y, x = key
            print(self.dict_display[key], end='')

    @staticmethod
    def pick_random(some_list: list):
        """
        Picks a random element from a list,
        removes it from said list,
        and returns it.

        Args:
            some_list (list): list to choose an element from.

        Returns:
            elt (any): an element of the list.
        """
        elt = random.choice(some_list)
        i = some_list.index(elt)
        return some_list.pop(i)
