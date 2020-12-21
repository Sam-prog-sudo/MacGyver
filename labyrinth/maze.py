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
        self.list_items = []
        self.number_items = len(C.CHOICE_ITEMS['name'])

    def create_lab_elements(self):
        """
        Read labyrinth template text file and create all elements.

        Iterates through the labyrinth text template to create :
        - a list of tuples containing walls positions
        - a list of tuples containing paths positions
        (on which MacGyver can move)
        - MacGyver and Gard objects.
        - all pickable items.
        - a list of all empty path

        NB:
        - position_X matches column number
        - position_y matches row number.
        - list_empty_paths is created for printing purposes.
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
        """
        Substract a list from an other.

        Args:
        - list2 (list): list of elements to substract.
        - list1 (list): list to be substracted from.

        Returns:
        - list: resulting list without desired list of elements.
        """
        return [
            pos for pos in list1 if pos not in list2
            ]

    def _create_all_items(self):
        """
        _create_all_items for the maze.

        Pick a finite number (n = self.number_items) of random position
        from a list to create n instaces of SomeItem.
        """
        list_items_pos = self.__pick_random_items_pos(self.number_items)

        for name in C.CHOICE_ITEMS['name']:
            n = 0
            self.list_items.append(
                self.__create_an_item(
                    a_name=name,
                    pos_tuple=list_items_pos.pop(n)
                    )
                )
            n += 1

    def __pick_random_items_pos(self, nbr_of_items: int):
        """
        __pick_random_items_pos from a list of available paths.

        Create a list of characters positions,
        substract it from list_of_paths and randomly sample from it.
        Then updates the list of empty paths.

        Args:
        - nbr_of_items (int): it reflects the number of disired positions.

        Returns:
        - list: all items positions.
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
        """
        Create an item with its name and position.

        Args:
        - a_name (str): name of said item.
        - pos_tuple (tuple): a tuple of position.

        Returns:
        - object: an instance of SomeItem
        """
        item = SomeItem(
            name=a_name,
            position_X=pos_tuple[1],
            position_Y=pos_tuple[0]
        )
        return item

    def chars_meet_up(self):
        """
        chars_meet_up disable either the gard or Macgyver when they meet up.
        """
        if len(self.macgyver.backpack) == 3:
            self.gard.disable()
        else:
            self.macgyver.disable()

    def update_list_items(self, an_item):
        """
        update_list_items remove an_item from the list of items.

        Args:
        - an_item (object): item to be removed.
        """
        self.list_items.remove(an_item)

    def update_list_empty_path(self, an_item):
        """
        update_list_empty_path by appending an item position to it.

        Args:
        - an_item (object): item to get position from.
        """
        self.list_empty_paths.append(an_item.position_tuple)
