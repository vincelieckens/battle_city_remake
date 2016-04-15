import pygame
import constants as c
import resources as r


class Tank(pygame.sprite.Sprite):

    def __init__(self, color, start_pos, screen):
        pygame.sprite.Sprite.__init__(self)
        self.color = color # There are four different colors possible. Each color has it's own map in data/tanks which consists of eight sprites.
        
        self.TANK_IMAGES = r.load_tank_images_new(c.COLORS)
        
        if start_pos == c.DOWN:
            self.image = self.TANK_IMAGES[color][c.UP]
            self.rect = self.image.get_rect()
            self.rect.midtop = [screen.get_width() / 2 , screen.get_height() - screen.get_height() / 4]
            self.direction = c.UP
        elif start_pos == c.UP:
            self.image = self.TANK_IMAGES[color][c.DOWN]
            self.rect = self.image.get_rect()
            self.rect.midtop = [screen.get_width() / 2, screen.get_height() / 4]
            self.direction = c.DOWN
            
        self.moving = False
        self.area = screen.get_rect()
        
        self.health = 3
              
    def update(self, other_player):
        self.animate_tank()
        self.detect_wall_collision()
        self.detect_tank_collision(other_player)
        while self.moving:
            self.update_position()
            self.change_image()
    
    def change_image(self):
        """
        This function changes the image of the tank according to the 
        direction in which the tank will be moving. It also expands
        the default size of the image to three times it's size
        """
        self.image = self.TANK_IMAGES[self.color][self.direction]
    
    def animate_tank(self):
        """ Changes the image of the tank to create the illusion that the tank tread is moving """
        if self.image == self.TANK_IMAGES[self.color]["{}_{}".format(self.direction, "mov")]:
            self.image = self.TANK_IMAGES[self.color][self.direction]
        elif self.image == self.TANK_IMAGES[self.color][self.direction]:
            self.image = self.TANK_IMAGES[self.color]["{}_{}".format(self.direction, "mov")]

    def move(self, direction):
        """
        This function gets called by the Level.event_loop() method.
        It sets the direction in which the tanks will move
        """
        self.moving = True
        self.direction = direction
    
    def update_position(self):
        """ Updates the position of the tank based on the direction attribute """
        if self.direction == c.RIGHT:
            self.rect = self.rect.move(8, 0)
        elif self.direction == c.LEFT:
            self.rect = self.rect.move(-8, 0)
        elif self.direction == c.UP:
            self.rect = self.rect.move(0, -8)
        elif self.direction == c.DOWN:
            self.rect = self.rect.move(0, 8)
        self.moving = False
        
    def detect_wall_collision(self):
        if self.direction == c.UP and self.rect.midtop[1] <= 0:
            self.moving = False
        elif self.direction == c.DOWN and self.rect.midbottom[1] >= 624:
            self.moving = False
        elif self.direction == c.LEFT and self.rect.midleft[0] <= 0:
            self.moving = False
        elif self.direction == c.RIGHT and self.rect.midright[0] >= 864:
            self.moving = False

    def detect_tank_collision(self, other_player):
        if self.rect.colliderect(other_player):
            self.health = -1
            other_player.health = -1

