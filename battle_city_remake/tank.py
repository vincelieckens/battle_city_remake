import pygame
import constants as c
import resources as r


class Tank(pygame.sprite.Sprite):

    def __init__(self, color, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        # There are four different colors possible. Each color has it's own map in data/tanks which consists of eight sprites, two for every direction with a different position of the tank tread
        self.image = r.TANK_IMAGES[color][start_pos] 
        self.expand_image()
        self.rect = self.image.get_rect()
        
        if start_pos == c.UP:
            self.rect.center = [r.SCREEN.get_width() / 2 , r.SCREEN.get_height() - r.SCREEN.get_height() / 4]
            self.direction = c.DOWN
        elif start_pos == c.DOWN:
            self.rect.center = [r.SCREEN.get_width() / 2, r.SCREEN.get_height() / 4]
            self.direction = c.UP
        self.moving = False
              
    def update(self):
        self.animate_tank()
        while self.moving:
            self.update_position()
            self.change_image()
    
    def change_image(self):
        """
        This function changes the image of the tank according to the 
        direction in which the tank will be moving. It also expands
        the default size of the image to three times it's size
        """
        self.image = r.TANK_IMAGES[self.color][self.direction]
        self.expand_image()
        
    def expand_image(self):
        """ This function expands the image to three times it's default size """
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
    
    def animate_tank(self):
        """ Changes the image of the tank to create the illusion that the tank tread is moving """
        if self.image == r.TANK_IMAGES[self.color]["{}_{}".format(self.direction, "mov")]:
            print "True!"
            self.image = r.TANK_IMAGES[self.color][self.direction]
            """ self.expand_image() """
        else:
            print "False!"
            self.image = r.TANK_IMAGES[self.color]["{}_{}".format(self.direction, "mov")]
            """ self.expand_image() """
        
    def move(self, direction):
        """
        This function gets called by the Level.event_loop() method.
        It sets the direction in which the tanks will move
        """
        self.moving = True
        self.direction = direction
    
    def update_position(self, speed = 5):
        """ Updates the position of the tank based on the direction attribute """
        if self.direction == c.RIGHT:
            self.rect = self.rect.move(speed, 0)
        elif self.direction == c.LEFT:
            self.rect = self.rect.move(-speed, 0)
        elif self.direction == c.UP:
            self.rect = self.rect.move(0, -speed)
        elif self.direction == c.DOWN:
            self.rect = self.rect.move(0, speed)
        self.moving = False
        
