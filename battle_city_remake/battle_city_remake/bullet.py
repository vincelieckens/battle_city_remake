import pygame
import constants as c 
import resources as r


class Bullet(pygame.sprite.Sprite):

    def __init__(self, start_pos, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = r.BULLET_IMAGES[direction]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        

    
        
