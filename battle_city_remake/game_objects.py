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
    
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('Sprite_1.png', 'green'	, -1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.topleft = 200, 200
        
    def update():
        pass
        
    def move_left():
        pass
    
    def move_righ():
        pass
        
    def move_up():
        pass
    
    def move_down():
        pass
    

class Cannonball(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self):
        
    def update():
        
        
        
class Explosion(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self):
        
    def update():
        pass
    
    

