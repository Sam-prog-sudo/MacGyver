# encoding: utf-8
"""
play.py
"""
# import pygame
from assets.display import intro
from labyrinth.maze import Maze
# from assets import constants as C


class Main:
    def __init__(self):
        self.lab = Maze()
        self.lab.create_lab_elements()
        intro()
        self.lab.print_lab()

    def _still_alive(self):
        if self.lab.macgyver.alive is False:
            return "You're dead :("
        elif self.lab.gard.alive is False:
            return "You've beaten this bloody gard :)"
        else:
            return True

    def play(self):
        while self._still_alive():
            direction = input('Enter valid move: ')
            self.lab.macgyver.move(direction, self.lab.list_paths)
            self.lab.fight()
            print(
                "postion (x , y): ({} , {})".format(
                    self.lab.macgyver.position_X,
                    self.lab.macgyver.position_Y
                    )
                )
            self.lab.macgyver.pick_up_item(self.lab.list_items)
            self.lab.print_lab()
