# encoding: utf-8
"""
Constants.py
"""
from a_maze_ing import constants as C


class Characters:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.display = C.DISPLAY[self.name]
        self.state = True  # alive or dead/sleeping

    def disabled(self):
        self.state = False

    def move(self, direction):
        """
        can change pos of Mc

        can collid with wall
        """
        pass
