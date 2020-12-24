# encoding: utf-8
"""
play.py
"""
from assets import display as d
from labyrinth.maze import Maze

from operations.pg.game import Game
from .interact import Interaction


class Main:
    def __init__(self):
        self.lab = Maze()
        self.lab.create_lab_elements()

    def select_plateform(self):
        print(d.plat)
        x = input()
        if x == "g" or x == "G":
            self.gui()
        elif x == "c" or x == "C":
            self.console()
        else:
            print(x, d.inval_in)
            return self.select_plateform()

    def console(self):
        d.intro()
        d.print_lab(self.lab)
        inter = Interaction(self.lab)
        while inter.still_awake():
            direction = input('\n'+d.ask_move)
            self.lab.macgyver.move_char(direction, self.lab.list_paths)
            if inter.check_chars_pos():
                self.lab.chars_meet_up()
            if self.lab.list_items:
                inter.item_picking_process()
            d.print_lab(self.lab)

    def gui(self):
        G = Game(maze=self.lab)
        G.run()
        print(d.goodbye)

    def play(self):
        """
        Work hard, play hard !
        """
        print(d.intro_text)
        self.select_plateform()
