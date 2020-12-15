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
    with open(C.INTRO_TEMPLATE, 'r') as f:
        for line in f:
            print(line.rstrip())
