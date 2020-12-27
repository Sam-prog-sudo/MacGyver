# encoding: utf-8
import pygame
from assets import constants as C


class Decor(pygame.sprite.Sprite):
    def __init__(self, name, pos_tuple):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(
            self.full_path(C.IMAGES[name])
            ).convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos_tuple[1] * C.A_MOVE
        self.rect.y = pos_tuple[0] * C.A_MOVE

    @staticmethod
    def full_path(image: str):
        return ''.join([C.IMAGE_FOLDER, image])


class Elements(Decor):
    def __init__(self, elt):
        super().__init__(elt.name, (elt.position_Y, elt.position_X))
        self.rect.centerx = elt.position_X * C.A_MOVE + 20
        self.rect.centery = elt.position_Y * C.A_MOVE + 20


class Player(Elements):
    def __init__(self, maze, macgyver):
        super().__init__(macgyver)
        self.maze = maze
        self.macgyver = macgyver

    def right(self):
        self.rect.x += C.A_MOVE

    def left(self):
        self.rect.x -= C.A_MOVE

    def up(self):
        self.rect.y -= C.A_MOVE

    def down(self):
        self.rect.y += C.A_MOVE

    def update_pos(self, event, inter):
        """
        Manage character movements in lab.

        Args:
            event : event in pygame.event.get()
            inter : Instance of class Interaction
        """
        keys = pygame.key.get_pressed()
        mov_keys = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        if (any(mov_keys) in keys) and event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if self.macgyver.move_char(key, self.maze.list_paths):
                if inter.check_chars_pos():
                    self.maze.chars_meet_up()
                elif self.maze.list_items:
                    inter.item_picking_process()
                getattr(self, key)()
