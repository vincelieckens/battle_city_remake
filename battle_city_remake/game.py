# This module holds the Game class that controls the game

import pygame
import sys
import constants as c
import level
from pygame.locals import *


class Game(object):
    # I still need to code a method to flip levels/states
    def __init__(self):
        self.screen = pygame.display.set_mode(c.SCREEN_SIZE)
        pygame.display.set_caption(c.TITLE)
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.current_level = level.Level(self.screen)
        # self.next_level = level.Level(self.screen)
    
    def event_loop(self):
        # Events (quitting the game by pressing escape or clicking on the window to quit) 
        # which are common to every state are handled by this loop
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                self.current_level.event_loop(event)
                if event.key == K_ESCAPE:
                    self.terminate()
    
    def flip_states(self):
        pass
        
    def terminate(self):
        pygame.quit()
        sys.exit()
        
    def update(self):
        while True:
            self.clock.tick(self.fps)
            self.event_loop()
            
            if self.current_level.status == c.QUIT:
                self.terminate()
            
            self.current_level.update(self.screen)
            pygame.display.flip()
            
            
        
