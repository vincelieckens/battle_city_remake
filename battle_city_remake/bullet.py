import pygame
import constants as c 
import resources as r


class Bullet(pygame.sprite.Sprite):

	def __init__(self, start_pos, direction):
		pygame.sprite.Sprite.__init__(self)
		self.image = r.BULLET_IMAGES[direction]
		self.rect = self.image.get_rect()
		self.rect.center = start_pos
		

	
		
