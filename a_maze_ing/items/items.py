# encoding: utf-8
"""
items.py
"""
from a_maze_ing import constants as C


class SomeItem:

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position
        self.display = C.DISPLAY[self.name]

        if self.name == 'syringe':
            self.state = 'to_fabricate'
        elif self.name in C.CHOICE_STRUCTURES['name']:
            self.state = 'irremovable'
        else:
            self.state = 'to_find'

    def assemble_items():
        pass
