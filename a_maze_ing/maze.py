
class Maze():
    width = 15
    height = 15
    filename = 'a_maze_ing.txt'
    path = " "
    wall = "X"
    gard = "G"
    macgyver = "M"
    start = "S"
    exit = "E"

    def lab_txt_to_list(self):
        """
        Convert text file which represents the the labyrinth layout into a list.

        The text file, which represents the labyrinth, is stored as a list of rows.
        The keys of this list represents the row number.
        An element of this list represents all the elements in a row.

        Returns:
            list:
                a list of labyrinth rows
        """
        master_list = []
        with open('a_maze_ing.txt', 'r') as m:
            for line in m:
                line = line.strip()
                master_list.append(line)
                print
                for i in range(len(master_list)):
                    master_list[i] = list(master_list[i])
            return master_list

    def access_elt(master_list: list, x: int, y: int):
        """
        Access a certain element of the labyrinth and returns it.

        Args:
            master_list (list):
                list representing the lab
            x (int):
                column postion of object
            y (int):
                row position of object

        Returns:
            int:
                an element of the lab
        """
        return master_list[y][x]

    def put_in_lab(master_list: list, x: int, y: int, object_to_place):
        """
        Put an element in the lab.

        Store an element (a labyrinth row) of :list:`master_list`,
        which key is :int:`y`, as a list of elements.
        Then access this list at key :int:`x` (column number in lab)
        to replace its element by desired `object_to_place`.

        Args:
            master_list (list):
                list representing the lab
            x (int):
                abs postion of object
            y (int):
                ord position of object
            object_to_place (str):
                element to place in lab.

        Returns:
            master_list (list):
                list representing the lab with the new element in it.
        """
        master_list[y][x] = object_to_place
        return master_list

    def erase_from_lab(master_list: list, x: int, y: int):
        """
        Erase an element from the lab.

        Args:
            master_list (list):
                list representing the lab
            x (int):
                abs postion of object
            y (int):
                ord position of object

        Returns:
            master_list (list):
                list representing the lab with desired element removed
        """
        line = list(master_list[y])
        line[x-1] = ' '
        master_list[y] = line
        return master_list

class Positions():
    pos_x: int 
    pos_y: int

    def reference_position():
        
        reference_position method defines point of origin and assign position
        to each font item (empty path).
        
        pass

    def up(self):
        return self.pos_y + 1

    def down(self):
        return self.pos_y - 1

    def left(self):
        return self.pos_x - 1

    def right(self):
        return self.pos_x + 1


class Characters(Positions):
    pass


class SomeItems(Maze, Positions):

    items_type = ['needle', 'tube', 'ether', 'syringe']
    items_proprety = ['mac', 'gard', 'lab', None]
    items_state = ['to_find', 'found', 'used', 'made']
    pass
"""
