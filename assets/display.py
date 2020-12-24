# encoding: utf-8
"""
display.py
"""
from . import constants as C

intro_text = """
Welcome to a_maze_ing !

Save Macgyver by exiting this labyrinth.
Words of caution: beware of the gard !
(he has COVID)

Please select a platform:
'g' for graphical interface
'c' for console
"""
goodbye = "See you soon :)"
inval_in = "Invalid input: "
victory = "You've beaten this bloody gard :)"
defeat = "You've been caught :("
ask_move = 'Enter valid move: '
item = "You've picked an item: "
yahoo = "You've assembled all the items ! Go for IT !"


def intro():
    """
    intro print ascii art.
    """
    with open(C.INTRO_ART, 'r') as f:
        for line in f:
            print(line.rstrip())


def display_backpack(maze):
    list_backpack = [item.name for item in maze.macgyver.backpack]
    print('Picked up item(s):{}\n'.format(list_backpack))


def print_lab(maze):
    """
    print_lab using its height and width.

    Compare objects position with a position tuple
    by iterating through maze width and height, to print following objects:
    - all unpicked items
    - all walls
    - Macgyver
    - the gard
    - all empty paths
    """
    print('\n')
    for i in range(0, C.SIZE['height']):
        for j in range(0, C.SIZE['width']):

            if maze.list_items:
                for item in maze.list_items:
                    if item.position_tuple == (i, j):
                        print(C.DISPLAY[item.name], end='')

            if (i, j) in maze.list_walls:
                print(C.DISPLAY['wall'], end='')

            elif maze.macgyver.position_tuple == (i, j):
                print(C.DISPLAY['macgyver'], end='')

            elif maze.gard.position_tuple == (i, j):
                print(C.DISPLAY['gard'], end='')

            elif (i, j) in maze.list_empty_paths:
                print(C.DISPLAY['path'], end='')
        print('')
