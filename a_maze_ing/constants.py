# encoding: utf-8
"""
Constants.py
"""

FILENAME = 'a_maze_ing.txt'

DIMENSION = {
    'width': 15,
    'height': 15,
    }

DISPLAY = {
    'path': ' ',
    'wall': 'X',
    'gard': 'G',
    'macgyver': 'M',
    'start': 'S',
    'finish': 'F',
    'needle': 'n',
    'tube': 't',
    'ether': 'e',
}

CHOICE_ITEMS = {
    'name': (
        'needle',
        'tube',
        'ether',
        'syringe',
        ),
    'nature': (
        'collectable',
        'fabricable',
        ),
    'property': (
        'mac',
        'lab',
        None,
        ),
    'state': (
        'to_find',
        'found',
        'used',
        'made',
        'to_fabricate',
        ),
    }
