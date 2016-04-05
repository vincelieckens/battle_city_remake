# This module holds the Map class

import pygame
from pygame.locals import *
import constants as c 
import tank
import bullet
import tile
# import explosion

class Level(object):
    
    def __init__(self):
        self.status = c.PLAYING
        self.playerone = tank.Tank(c.GREEN, c.UP)
        self.playertwo = tank.Tank(c.GREY, c.DOWN)
        self.bullet = bullet.Bullet((180, 180), c.DOWN)
        self.initialize_map()
        self.tanks = pygame.sprite.RenderPlain((self.playerone, self.playertwo))
        self.map = pygame.sprite.RenderPlain((self.tile))
        
    def initialize_map(self):
        self.tile = tile.Tile((100, 100))
        
    def update(self, screen):
        # Gets called by the Game.update() method with the screen as argument
        self.playerone.update()
        self.playertwo.update()
        self.draw_everything(screen)
    
    def draw_everything(self, screen):
        self.tanks.draw(screen)
        self.map.draw(screen)
    
    def event_loop(self, event):
        print "Test event loop"
        if event.key == K_UP:
            print "Player 2 up"
            self.playertwo.move(c.UP)
        elif event.key == K_DOWN:
            print "Player 2 down"
            self.playertwo.move(c.DOWN)
        elif event.key == K_LEFT:
            print "Player 2 left"
            self.playertwo.move(c.LEFT)
        elif event.key == K_RIGHT:
            print "Player 2 right"
            self.playertwo.move(c.RIGHT)
        elif event.key == K_z:
            print "Player 1 up"
            self.playerone.move(c.UP)
        elif event.key == K_s:
            print "Player 1 down"
            self.playerone.move(c.DOWN)
        elif event.key == K_q:
            print "Player 1 left"
            self.playerone.move(c.LEFT)
        elif event.key == K_d:
            print "Player 1 right"
            self.playerone.move(c.RIGHT)
        
        
        
    
