# encoding: utf-8
"""
Constants.py
"""
from os.path import abspath, dirname, join

BASE_DIR = abspath(join(dirname(__file__), '../..'))

FILENAME = join(BASE_DIR, 'a_maze_ing.txt')

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
        'syringe',
        ),
    'state': (
        'to_find',
        'to_fabricate',
        ),
    }

VALID_DIRECTIONS = {'up', 'down', 'left', 'right'}
