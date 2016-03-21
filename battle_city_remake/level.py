# This module holds the Map class

import pygame
import constants as c 
import tank
import bullet
import tile
# import explosion

class Level(object):
	
	def __init__(self):
		self.playerone = tank.Tank(c.GREEN, c.UP)
		self.playertwo = tank.Tank(c.GREY, c.DOWN)
		self.initialize_map()
		self.sprites = pygame.sprite.RenderPlain((self.playerone, self.playertwo, self.tile))
		
	def initialize_map(self):
		self.tile = tile.Tile((100, 100))
		
	def update(self, screen):
		self.sprites.draw(screen)
		
		
	
