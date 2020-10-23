# encoding: utf-8

# deplacement + affichage
"""
maze.py
"""
import random
from constants import DISPLAY, FILENAME, DIMENSION, CHOICE_ITEMS


class Maze():

    def __init__(self, list_pers, list_items):
        self.list_walls = []
        self.list_path = []
        self.list_pers = list_pers  #  faire 2 objets pas de list
    
        self.list_items = list_items  #  construire ici
        self.start.position = ()   #lorsque'il y a S, créer mac gyver
        self.finish.position = ()    #lorsque'il y a E, créer gard
        self.__create_lists_of_lab_elements()

    def __create_lists_of_lab_elements(self):
        with open(FILENAME, 'r') as m:
            row = 0                         # row number
            for line in m:
                column = 0                  # column number
                for char in line:
                    if char != '\n':
                        if char == DISPLAY['wall']:
                            self.list_walls.append((row, column))
                        elif char == DISPLAY['path']:
                            self.list_path.append((row, column))
                        elif char == DISPLAY['start']:
                            self.start.position = (row, column)
                        elif char == DISPLAY['finish']:
                            self.start.position = (row, column)
                    column += 1             # column increment
                row += 1                    # row increment
            #  assert DIMENSION['width'] == column+1
            #  assert DIMENSION['height'] == row+1

    @staticmethod
    def pick_random(some_list: list):
        """
        [summary]

        Args:
            some_list (list): list to choose an element from.

        Returns:
            [type]: [description]
        """
        return random.choice(some_list)

    def display_lab_in_console():
        # print en fct des coord
        pass


class Characters():

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.state = True  # alive or dead/sleeping
        if self.name == 'macgyver':
            self.position = Maze.start.position
        elif self.name == 'gard':
            self.position = Maze.finish.position

    def create_list_of_pers():
        pass

    def disabled(self):
        self.state = False

    def mac_gic_touch():
        pass


class SomeItem():

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position

        # faire qlqchose de plus générique
        if self.name == 'syringe':
            self.nature = 'fabricable'
            self.property = None
            self.state = 'to_fabricate'
        else:
            self.nature = 'collectable'
            self.property = 'lab'
            self.state = 'to_find'

    def create_list_of_items():
        pass

    def access_list_items():
        pass

    def item_is_picked_up(self):
        self.property = 'mac'
        self.state = 'found'
        pass

    def assemble_items():
        pass


class CustomAssertions:
    def assertFileExists(self, path):