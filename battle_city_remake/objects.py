#!/usr/bin/env python2
# Tank class and cannonball class 

import os
import pygame
from pygame.locals import *
import resources
import main


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, color, size, start_pos, screen):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = resources.tank_sprites['right']
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        if start_pos == 'down':
            self.rect.topleft = (400, 400)
        elif start_pos == 'up':
            self.rect.topleft = (200, 200)
        self.direction = 'still' # Tank can stand still, move right, left, up or down
        self.shooting = False
        self.hit = True
        self.health = 3
        self.area = screen.get_rect()
        
    def update(self):
        # Move the tank if it does not stand still
        if self.direction != 'still':
            self._change_image()
            self._move()
            self.direction = 'still'
    
    def _change_image(self):
        self.image = resources.tank_sprites[self.direction]
        self.image = pygame.transform.scale(self.image, self.size)
        
    def moving(self, direction):
        if direction == 'right':
            self.direction = 'right'
        elif direction == 'left':
            self.direction = 'left'
        elif direction == 'up':
            self.direction = 'up'
        elif direction == 'down':
            self.direction = 'down'     
        
    def _move(self, speed = 20):
        # Check for walls or stonetiles first, abort if there are
        self._scan_surroundings(self.direction)
        if self.direction == 'right':
            self.rect = self.rect.move(speed, 0)
        elif self.direction == 'left':
            self.rect = self.rect.move(-speed, 0)
        elif self.direction == 'up':
            self.rect = self.rect.move(0, -speed)
        elif self.direction == 'down':
            self.rect = self.rect.move(0, speed)
            
    def _scan_surroundings(self, direction):
        x_coordinate = self.rect[0]
        y_coordinate = self.rect[1]
        print x_coordinate
        print y_coordinate
        # This function checks the surroundings of the tank for walls or stonetiles
        # Need to change hardcoded numbers 
        if not self.area.contains(self.rect):
            print self.rect
            if x_coordinate > 590 and direction == 'right':
               self.direction = 'still'
            elif x_coordinate < 40 and direction == 'left':
                self.direction = 'still'
            elif y_coordinate > 430 and direction == 'down':
                self.direction = 'still'
            elif y_coordinate <  40 and direction == 'up':
                self.direction = 'still'
        
    def fire_cannon(self):
        self.shooting = True
        
    def _respawn(self):
        pass
        
    def _check_health(self):
        if self.health < 0:
            pass
    

class Cannonball(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass
        
    def update():
        pass
        
        
class Explosion(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass
        
    def update():
        pass
    
    

