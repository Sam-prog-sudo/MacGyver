# encoding: utf-8
"""
display.py
"""
from . import constants as C


def intro():
    with open(C.INTRO_TEMPLATE, 'r') as f:
        for line in f:
            print(line.rstrip())
