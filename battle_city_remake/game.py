# This module holds the Game class that controls the game

import pygame
import sys
import constants as c
import level
from pygame.locals import *


class Game(object):
	"""
	This class controls the main loop of the game
	"""
	def __init__(self):
		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.fps = 60
		self.current_level = level.Level()
	
	def event_loop(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.terminate()
	
	def terminate(self):
		pygame.quit()
		sys.exit()
		
	def run_current_level(self):
		self.clock.tick(self.fps)
		# self.current_level.update()
		
	def update(self):
		while True:
			# self.clock.tick(self.fps)
			# self.event_loop()
			self.current_level.update(self.screen)
			
			# if self.current_level == c.QUIT:
				# self.terminate()
				
			# self.screen.fill(c.BLACK)
			# self.event_loop()
			self.event_loop()
			pygame.display.update()
			
			
		
