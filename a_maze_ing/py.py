class Maze():
    width = 15
    height = 15
    filename = 'a_maze_ing.txt'

    def lab_txt_to_list(self):
        """
        Convert text file which represents the the labyrinth layout into a list.

        The text file, which represents the labyrinth, is stored as a list of rows.
        The keys of this list represents the row number.
        An element of this list represents all the elements in a row

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

mazing = Maze()
x = mazing.lab_txt_to_list()
print(len(x))
print(x)
