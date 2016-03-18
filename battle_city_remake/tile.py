import pygame
import constants as c
import resources as r


class Tile(pygame.sprite.Sprite):

	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = r.TILE_IMAGES['normal']
		self.rect = self.image.get_rect()
		self.rect.center = position
