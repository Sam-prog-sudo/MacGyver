# encoding: utf-8
"""
constants.py
"""

LAB_TEMPLATE = "assets/templates/a_maze_ing.txt"
INTRO_TEMPLATE = "assets/templates/intro_ascii_art.txt"

SIZE = {
    'width': 15,
    'height': 15,
    }

DISPLAY = {
    'path': ' ',
    'wall': 'X',
    'gard': 'G',
    'macgyver': 'M',
    'needle': 'n',
    'tube': 't',
    'ether': 'e',
}

CHOICE_ITEMS = {
    'name': (
        'needle',
        'tube',
        'ether',
        ),
    'state': (
        'to_find',
        'found'
        ),
    'belonging_to': (
        'maze',
        'macgyver',
        None
        )
    }

VALID_DIRECTIONS = {'up', 'down', 'left', 'right'}
