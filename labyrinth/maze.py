# encoding: utf-8
"""
maze.py
"""

from random import sample

from assets import constants as C

from .characters import Characters
from .items import SomeItem


class Maze:

    def __init__(self):
        self.dict_display = {}
        self.list_walls = []
        self.list_paths = []
        self.list_empty_paths = []
        self.list_items = []
        self.number_items = len(C.CHOICE_ITEMS['name'])

    def create_lab_elements(self):
        """
        Read labyrinth template text file and create all.

        Read labyrinth text template to create :
        - a list of tuples containing walls positions
        - a list of tuples containing paths positions
        (on which MacGyver can move)
        - MacGyver and Gard objects.
        - all pickable items

        NB:
        - position_X matches column number
        - position_y matches row number.
        """

        with open(C.LAB_TEMPLATE, 'r') as m:
            row = 0                         # row number
            for line in m:
                column = 0                  # column number

                for char in line:
                    if char != '\n':

                        if char == C.DISPLAY['wall']:
                            self.list_walls.append((row, column))
                        else:
                            self.list_paths.append((row, column))

                            if char == C.DISPLAY['macgyver']:
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

                    column += 1             # column increment
                row += 1                    # row increment
        self.list_empty_paths = self.list_paths
        self._create_all_items()

    @staticmethod
    def __substract_list2_from_list1(list2, list1):
        return [
            pos for pos in list1 if pos not in list2
            ]

    def _create_all_items(self):
        list_items_pos = self.__pick_random_items_pos(self.number_items)
        for name in C.CHOICE_ITEMS['name']:
            n = 0
            self.list_items.append(
                self.__create_an_item(
                    name,
                    list_items_pos.pop(n)
                    )
                )
            n += 1

    def __pick_random_items_pos(self, nbr_of_items: int):
        """
        """
        list_char_pos = [
            self.gard.position_tuple,
            self.macgyver.position_tuple
        ]
        temp_list = self.__substract_list2_from_list1(
            list2=list_char_pos,
            list1=self.list_paths
            )
        items_pos = sample(temp_list, nbr_of_items)
        self.list_empty_paths = self.__substract_list2_from_list1(
            list2=items_pos,
            list1=self.list_paths
        )
        return items_pos

    @staticmethod
    def __create_an_item(a_name, pos_tuple):
        item = SomeItem(
            name=a_name,
            position_X=pos_tuple[1],
            position_Y=pos_tuple[0]
        )
        return item

    def print_lab(self):
        """
        Display labyrinth in shell.
        """
        print('\n')
        for i in range(0, C.SIZE['height']):
            for j in range(0, C.SIZE['width']):

                self._item_print(i, j)

                if (i, j) in self.list_walls:
                    print(C.DISPLAY['wall'], end='')

                elif self.macgyver.position_tuple == (i, j): # noqa
                    print(C.DISPLAY['macgyver'], end='')

                elif self.gard.position_tuple == (i, j):
                    print(C.DISPLAY['gard'], end='')

                elif (i, j) in self.list_empty_paths:
                    print(C.DISPLAY['path'], end='')
            print('')

    def _item_print(self, height, width):
        for item in self.list_items:
            if item.state == 'to_find':
                if item.position_tuple == (height, width):
                    print(C.DISPLAY[item.name], end='')
            elif item.position_tuple not in self.list_empty_paths:
                self.list_empty_paths.append(item.position_tuple)

    def fight(self):
        if self.macgyver.position_tuple == self.gard.position_tuple:
            for item in self.list_items:
                if all(item.state == 'found'):
                    self.gard.disable
                else:
                    self.macgyver.disable
