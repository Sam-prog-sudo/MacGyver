# encoding: utf-8
from assets import display as d


class Interaction:
    """
    Class for managing characters and items interactions.
    """
    def __init__(self, maze):
        self.lab = maze

    def still_awake(self):
        """
        still_awake verify if a character is still awake.

        Returns:
        - bool: if one of the characters is asleep.
        """
        if self.lab.macgyver.sleeping is True:
            print(d.defeat)
            return False
        elif self.lab.gard.sleeping is True:
            print(d.victory)
            return False
        else:
            return True

    def check_chars_pos(self):
        """
        Returns:
            bool: if Macgyver and the gard are in the same room.
        """
        return self.lab.macgyver.position_tuple == self.lab.gard.position_tuple

    def item_picking_process(self):
        """
        _item_picking_process.

        Iterates through the list of items.
        if Macgyver and an item have the same position:
        - Macgyver pick the item up
        - the list of items is updated
        - the list of empty paths to be displayed is updated.
        """
        for an_item in self.lab.list_items:
            if self.lab.macgyver.position_tuple == an_item.position_tuple:
                self.lab.macgyver.pick_up_item(an_item)
                self.lab.update_list_items(an_item)
                self.lab.update_list_empty_path(an_item)
                print(d.item, an_item.name)
                d.display_backpack(self.lab)
                if len(self.lab.macgyver.backpack) == 3:
                    print(d.yahoo)
