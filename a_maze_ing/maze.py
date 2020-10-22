import random


class Maze():

    # constants to be placed in some other file
    width = 0
    height = 0
    filename = 'a_maze_ing.txt'
    path = " "
    wall = "X"
    gard = "G"
    macgyver = "M"
    start = "S"
    finish = "F"
    needle = 'n'
    tube = 't'
    ether = 'e'

    def __init__(self):
        self.list_walls = []
        self.list_path = []
        self.list_pers = []
        self.list_items = []
        self.start.position = ()
        self.finish.position = ()

    def create_lists_of_everything(self):
        with open('a_maze_ing.txt', 'r') as m:
            y = 0           # row number
            for line in m:
                x = 0       # column number
                for char in line:
                    if char != '\n':
                        if char == 'X':
                            self.list_walls.append((y, x))
                        elif char == ' ':
                            self.list_path.append((y, x))
                        elif char == 'S':
                            self.start.position = (y, x)
                        elif char == 'F':
                            self.start.position = (y, x)
                    x += 1  # row increment
                y += 1      # column increment
            self.width = x
            self.height = y

    def pick_random_empty_position(self):
        return random.choice(Maze.list_path)

    def display_lab_in_console():
        pass


class Characters(Maze):

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.state = True  # alive or dead/sleeping
        if self.name == 'macgyver':
            self.position = Maze.start.position
        elif self.name == 'gard':
            self.position = Maze.finish.position

    def disabled(self):
        self.state = False

    def mac_gic_touch():
        pass


class SomeItem(Maze):
    """
    choice_items_name = ('needle', 'tube', 'ether', 'syringe')
    choice_item_nature = ('collectable', 'fabricable')
    choice_items_property = ('mac', 'lab', None)
    choice_items_state = ('to_find', 'found', 'used', 'made', 'to_fabricate')
    """

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position
        if self.name == 'syringe':
            self.nature = 'fabricable'
            self.property = None
            self.state = 'to_fabricate'
        else:
            self.nature = 'collectable'
            self.property = 'lab'
            self.state = 'to_find'

    def item_is_picked_up(self):
        self.property = 'mac'
        self.state = 'found'
        pass

    def assemble_items():
        pass
