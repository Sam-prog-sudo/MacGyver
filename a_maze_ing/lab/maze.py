# encoding: utf-8

# deplacement + affichage
"""
maze.py
"""

from characters.characters import Characters

from constants import constants as C

# from a_maze_ing.items import SomeItem


class Maze:

    def __init__(self):
        self.dict_display = {}
        self.list_walls = []
        self.list_paths = []
        self.list_items = []

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

                        elif char == C.DISPLAY['macgyver']:
                            self.macgyver = Characters(
                                name='macgyver',
                                movable=True,
                                position_X=column,
                                position_Y=row,
                                )

                        elif char == C.DISPLAY['gard']:
                            self.gard = Characters(
                                name='gard',
                                position_X=column,
                                position_Y=row,
                                )
                        else:
                            self.list_paths.append(
                                (row, column)
                                )

                    column += 1             # column increment
                row += 1                    # row increment

    def print_lab(self):
        """
        [summary]
        """
        for i in range(0, C.SIZE['height']):
            for j in range(0, C.SIZE['width']):
                if (i, j) in self.list_walls:
                    print('x', end='')
                elif (self.macgyver.position_X, self.macgyver.position_Y) == (i, j):
                    print('m', end='')
                elif (self.gard.position_X, self.gard.position_Y) == (i, j):
                    print('g', end='')
                else:
                    print(' ', end='')
            print('')
