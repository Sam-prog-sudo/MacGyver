
class Maze():
    width = 15
    height = 15
    filename = 'a_maze_ing.txt'

    def draw_font_lab(self):      
        """
        draw_font method plots the font of the lab onto a text file:
        no walls, only empty paths.
        
        Returns:
            list: list of all case arranged in list of list of 
        """
        axe_x = axe_y = []
        with open(self.filename, 'w+') as f:
            for i in range(self.width):
                axe_x[i] = 0
            for j in range(self.height):
                axe_y[j] = axe_x
            for item in axe_y:
                f.write(f"{item}\n")
        return axe_y

    def display_lab(self):
        """
        display_lab method prints lab layout, from text file to console.
        """
        with open('a_maze_ing.txt', 'r') as f:
            print(f.read())

    def place_something_somwhere(self, content, pos_x, pos_y):
        with open('a_maze_ing.txt', 'r+') as f:
            lines = f.readlines()
            line = list(lines[pos_y])
            
            for line in f:
                pass

    def starting_position():
        random(pos(gard)
        g_w = (pos(gard) != pos(wall))
        g_m = (pos(gard) != pos(mac))
        g_o = (pos(gard) != pos(an_item))
        g_t
        if g_w and g_m and g_o:
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
    items_proprety = ['mac', 'gard', 'lab', None]
    items_state = ['to_find', 'found', 'used', 'made']
    pass
