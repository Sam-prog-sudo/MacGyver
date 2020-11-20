# encoding: utf-8
"""
items.py
"""
from assets import constants as C


class SomeItem:

    def __init__(self, name: str, position_X, position_Y):
        self.name = name
        self.position_X = position_X
        self.position_Y = position_Y
        self.display = C.DISPLAY[self.name]

    @property
    def position_tuple(self):
        return (self.position_Y, self.position_X)
