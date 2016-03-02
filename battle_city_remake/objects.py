# Tank class and cannonball class 

from main import *
import pygame
from pygame.locals import *
import os


def load_image(name, color, colorkey=None):
    fullname = os.path.join('data', 'tanks', color, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, color, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('Sprite_1.png', color, -1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        if start_pos == 'down':
            self.rect.topleft = 400, 400
        elif start_pos == 'up':
            self.rect.topleft = 200, 200
        self.rect.topleft = 200, 200
        self.moving = 'still'
        self.shooting = False
        self.state = 'alive'
        self.health = 3
        
    def update():
        
        # Check moving state of tank, move according to this state
        if self.moving == 'right':
            pass
        elif self.moving == 'left':
            pass
        elif self.moving == 'up':
            pass
        elif self.moving == 'down':
            pass
            
        # Check for health, game over if health zero
        
        # if death:
        # self.respawn
        
        # if self.shooting:
            # shoot_cannon()
        
        
    
    # Every move function needs to check if the tank is hitting a wall or stone
    
    def move_left():
        self.moving = 'left'
    
    def move_righ():
        self.moving = 'right'
        
    def move_up():
        self.moving = 'up'
    
    def move_down():
        self.moving = 'down'
        
    def fire_cannon():
        pass
        
    def respawn():
        pass
        
    def check_health():
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
    
    

