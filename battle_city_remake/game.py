# This module holds the Game class that controls the game

import pygame
import sys
import constants as c
import level
from pygame.locals import *


class Game(object):
    # I still need to code a method to flip levels/states
    """
    This class controls the main loop of the game
    """
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.background = pygame.Surface(self.screen.get_size())
        self.background.convert()
        self.background.fill(c.BLACK)
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.current_level = level.Level(self.screen)
    
    def event_loop(self):
        # Some events are needed in every state of the game, such as quitting the
        # game by pressing escape or clickin on the window. Some events are specific
        # To a certain state where the game finds itself in, these are called by the
        # self.current_level.event_loop() method
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                self.current_level.event_loop(event)
                if event.key == K_ESCAPE:
                    self.terminate()
    
    def terminate(self):
        pygame.quit()
        sys.exit()
        
    def update(self):
        while True:
            self.clock.tick(self.fps)
            self.event_loop()
            
            if self.current_level.status == c.QUIT:
                self.terminate()
            
            self.screen.blit(self.background, (0, 0))
            self.current_level.update(self.screen)
            pygame.display.update()
            
            
        
