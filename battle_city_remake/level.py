# This module holds the Map class

import pygame
from pygame.locals import *
import constants as c 
import tank
import bullet
import tile
# import explosion

class Level(object):
    
    def __init__(self, screen):
        self.status = c.PLAYING
        
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 80, 80))
        
        self.playerone = tank.Tank(c.GREEN, c.UP, screen)
        self.playertwo = tank.Tank(c.GREY, c.DOWN, screen)
        self.bullet = bullet.Bullet((180, 180), c.DOWN)
        self.initialize_map()
        
        self.tanks = pygame.sprite.RenderPlain((self.playerone, self.playertwo))
        self.map = pygame.sprite.RenderPlain((self.tile))

        
    def initialize_map(self):
        self.tile = tile.Tile((100, 100))
        
    def update(self, screen):
        # Gets called by the Game.update() method with the screen as argument
        
        if self.playerone.health < 0 or self.playertwo.health < 0:
            self.status = c.QUIT
        
        self.playerone.update(self.playertwo)
        self.playertwo.update(self.playerone)
        self.draw_everything(screen)
    
    def draw_everything(self, screen):
        screen.blit(self.background, (0, 0))
        self.tanks.draw(screen)
        self.map.draw(screen)
    
    def event_loop(self, event):
        if event.key == K_UP:
            self.playertwo.move(c.UP)
            print "Player two up"
        elif event.key == K_DOWN:
            self.playertwo.move(c.DOWN)
            print "Player two down"
        elif event.key == K_LEFT:
            self.playertwo.move(c.LEFT)
            print "Player two left"
        elif event.key == K_RIGHT:
            self.playertwo.move(c.RIGHT)
            print "Player two right"
        elif event.key == K_z:
            self.playerone.move(c.UP)
            print "Player one up"
        elif event.key == K_s:
            self.playerone.move(c.DOWN)
            print "Player one down"
        elif event.key == K_q:
            self.playerone.move(c.LEFT)
            print "Player one left"
        elif event.key == K_d:
            self.playerone.move(c.RIGHT)
            print "Player one right"
        
        
        
    
