import pygame
import constants as c
import resources as r


class Tile(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = r.TILE_IMAGES['normal']
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = position
