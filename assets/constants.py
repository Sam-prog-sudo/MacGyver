# encoding: utf-8
"""
constants.py
"""

IMAGE_FOLDER = "assets/ressource/images/"
LAB_TEMPLATE = "assets/templates/a_maze_ing.txt"
INTRO_ART = "assets/ressource/arts/intro_ascii_art.txt"

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

IMAGES = {
    'macgyver': 'MacGyver.png',
    'gard': 'Gardien.png',
    'needle': 'aiguille.png',
    'tube': 'tube_plastique.png',
    'ether': 'ether.png',
    'seringe': 'seringue.png',
    'wall': 'wall.png',
    'path': 'floor.png'
}

WIDTH = int(600)  # each tile is 30 pixels large
HEIGHT = int(600)
FPS = int(10)
A_MOVE = int(40)

BLACK = (0, 0, 0)
