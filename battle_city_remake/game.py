# This module holds the Game class that controls the game

import pygame
import constants as c


class Game(object):
	"""
	This class controls the main loop of the game
	"""
	def __init__(self):
		self.screen = pygame.display.set_caption(c.TITLE)
		self.clock = pygame.time.Clock()
		self.fps = 60
		
