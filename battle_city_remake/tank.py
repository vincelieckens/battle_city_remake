import pygame
import constants as c
import resources as r


class Tank(pygame.sprite.Sprite):

	def __init__(self, color, start_pos):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = r.TANK_IMAGES[color][start_pos]
		self.rect = self.image.get_rect()
		
		if start_pos == c.UP:
			self.rect.center = [r.SCREEN.get_width() / 2 , r.SCREEN.get_height() - r.SCREEN.get_height() / 4]  
		elif start_pos == c.DOWN:
			self.rect.center = [r.SCREEN.get_width() / 2, r.SCREEN.get_height() / 4]
