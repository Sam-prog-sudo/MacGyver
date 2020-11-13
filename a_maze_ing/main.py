# encoding: utf-8
"""
main.py
"""
from constants.constants import VALID_DIRECTIONS
from characters.characters import Characters
import pygame

from lab.maze import Maze


def playing(mac, gard):
    if mac.alive is False:
        return "You're dead :("
    elif gard.alive is False:
        return "You've beaten this bloody gard :)"
    else:
        return True


def main():
    labyrinth = Maze()
    labyrinth.create_lab_elements()
    mac = labyrinth.macgyver
    gard = labyrinth.gard

    labyrinth.print_lab()

    while playing(mac, gard) is True:
        for event in pygame.event.get():
            if event.key == pygame.K_DOWN:
                mac.move('down')
            elif event.key == pygame.K_UP:
                mac.move('up')
            elif event.key == pygame.K_LEFT:
                mac.move('left')
            elif event.key == pygame.K_RIGHT:
                mac.move('right')
        labyrinth.print_lab()


if __name__ == '__main__':
    main()
