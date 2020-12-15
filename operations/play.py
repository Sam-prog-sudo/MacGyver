# encoding: utf-8
"""
play.py
"""
# import pygame
from assets.display import intro
from labyrinth.maze import Maze


class Main:
    def __init__(self):
        self.lab = Maze()
        self.lab.create_lab_elements()

    def still_awake(self):
        """
        still_awake verify if a character is still awake.

        Returns:
        - bool: if one of the characters is asleep.
        """
        if self.lab.macgyver.sleeping is True:
            print("You''ve been caught :(")
            return False
        elif self.lab.gard.sleeping is True:
            print("You've beaten this bloody gard :)")
            return False
        else:
            return True

    def _check_chars_pos(self):
        """
        Returns:
            bool: if Macgyver and the gard are in the same room.
        """
        return self.lab.macgyver.position_tuple == self.lab.gard.position_tuple

    def _item_picking_process(self):
        """
        _item_picking_process.

        Iterates through the list of items.
        if Macgyver and an item have the same position:
        - Macgyver pick the item up
        - the list of items is updated
        - the list of empty paths to be displayed is updated.
        """
        for an_item in self.lab.list_items:
            if self.lab.macgyver.position_tuple == an_item.position_tuple:
                self.lab.macgyver.pick_up_item(an_item)
                self.lab.update_list_items(an_item)
                self.lab.update_list_empty_path(an_item)

    def play(self):
        """
        Work hard, play hard !
        """
        while self.still_awake():
            direction = input('Enter valid move: ')
            self.lab.macgyver.move(direction, self.lab.list_paths)
            if self._check_chars_pos():
                self.lab.chars_meet_up()
            if self.lab.list_items:
                self._item_picking_process()
            self.lab.print_lab()
