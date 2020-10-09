def generate_lab():
    with open('a_maze_ing.txt', 'w') as f:
        for j in range(15):
            for i in range(15):
                f.write("1")
            f.write('\n')


def lab_to_list():
    with open('a_maze_ing.txt', 'r') as f:
        list_of_lines = f.readlines()
        list_of_lines = [line[:-1] for line in list_of_lines]
    return list_of_lines


def put_in_lab(master_list: list, x: int, y: int, object_to_place):
    """
    Put an element in the lab.

    Args:
        master_list (list): list representing the lab
        x (int): abs postion of object
        y (int): ord position of object
        object_to_place (str): element to place in lab.

    Returns:
        master_list (list): list representing the lab with the new element in it
    """
    line = list(master_list[y])
    line[x-1] = object_to_place
    master_list[y] = line
    return master_list

def del_from_lab(master_list: list, x: int, y: int):
    """
    Del an element from the lab

    Args:
        master_list (list): list representing the lab
        x (int): abs postion of object
        y (int): ord position of object

    Returns:
        master_list (list): list representing the lab with desired element removed
    """
    line = list(master_list[y])
    line[x-1] = ' '
    master_list[y] = line
    return master_list
