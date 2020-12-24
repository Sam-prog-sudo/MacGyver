# encoding: utf-8
import pygame
from assets import constants as C
from .sprites_light import Decor, Elements, Player
from ..interact import Interaction


class Game:
    def __init__(self, maze):
        pygame.init()
        self.maze = maze
        self.screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
        pygame.display.set_caption("a_maze_ing")
        self.clock = pygame.time.Clock()
        self.running = True
        self.build_structures()
        self.build_items()
        self.build_pers()

    def build_structures(self):
        self.structure = pygame.sprite.Group()
        decor_sprites = [Decor('wall', pos_tuple) for pos_tuple in self.maze.list_walls] # noqa
        path_sprites = [Decor('path', pos_tuple) for pos_tuple in self.maze.list_paths] # noqa

        self.structure.add(decor_sprites+path_sprites)

    def build_items(self):
        self.items = pygame.sprite.Group()
        items_sprites = [Elements(elt) for elt in self.maze.list_items]

        self.items.add(items_sprites)

    def build_pers(self):
        self.pers = pygame.sprite.Group()
        self.player = Player(self.maze, self.maze.macgyver)
        gard = Elements(self.maze.gard)
        self.pers.add([self.player, gard])

    def update_pick_item(self):
        a_sprite = pygame.sprite.spritecollideany(self.player, self.items)
        if a_sprite:
            self.items.remove(a_sprite)
            self.structure.add(
                [Decor('path', (a_sprite.rect.y, a_sprite.rect.x))]
            )

    def run(self):
        inter = Interaction(self.maze)
        while self.running and inter.still_awake():
            # keep loop running at the right speed
            self.clock.tick(C.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    # Update
                    self.player.update_pos(event, inter)
                    self.update_pick_item()
                    # Draw / render
                    self.screen.fill(C.BLACK)
                    self.structure.draw(self.screen)
                    self.items.draw(self.screen)
                    self.pers.draw(self.screen)
                    # after drawing everything, flip the display
                    pygame.display.flip()
        pygame.quit()
