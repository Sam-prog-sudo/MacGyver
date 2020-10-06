
class Maze():
    width = 15
    height = 15
    filename = 'lab/a_maze_ing.txt'

    def draw_font_lab(self):
        """
        draw_font method plots the font of the lab onto a text file:
        no walls, only empty paths.
        """
        with open(self.filename, 'w+') as f:
            for i in range(self.height):
                for j in range(self.width):
                    f.write("0")
                f.write('\n')

    def display_lab(self):
        """
        display_lab method prints lab layout, from text file to console.
        """
        with open('lab/a_maze_ing.txt', 'r') as f:
            print(f.read())

    def starting_position():
        random(pos(gard)
        g_w = pos(gard) != pos(wall)
        g_m = pos(gard) != pos(mac)
        g_o = pos(gard) != pos(an_item)
        g_t
        if g_w and g_m and g_o
            random(pos(gard))
        


class Positions():
    pos_x: int
    pos_y: int

    def reference_position():
        """
        reference_position method defines point of origin and assign position
        to each font item (empty path).
        """
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
    pass
