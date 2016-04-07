import pygame
import constants as c
import resources as r


class Tank(pygame.sprite.Sprite):

    def __init__(self, color, start_pos, screen):
        pygame.sprite.Sprite.__init__(self)
        self.color = color # There are four different colors possible. Each color has it's own map in data/tanks which consists of eight sprites, two for every direction with a different position of the tank tread
        
        if start_pos == c.UP:
            self.image = r.TANK_IMAGES[color][c.DOWN]
            self.rect = self.image.get_rect()
            self.rect.center = [r.SCREEN.get_width() / 2 , r.SCREEN.get_height() - r.SCREEN.get_height() / 4]
            print self.rect.center
            self.direction = c.DOWN
        elif start_pos == c.DOWN:
            self.image = r.TANK_IMAGES[color][c.UP]
            self.rect = self.image.get_rect()
            self.rect.center = [r.SCREEN.get_width() / 2, r.SCREEN.get_height() / 4]
            print self.rect.center
            self.direction = c.UP
            
        self.moving = False
        self.area = screen.get_rect()
              
    def update(self):
        self.animate_tank()
        self.detect_wall_collision()
        while self.moving:
            print "X coordinate: {}".format(self.rect.center[0])
            print "Y coordinate: {}".format(self.rect.center[1])
            self.update_position()
            self.change_image()
    
    def change_image(self):
        """
        This function changes the image of the tank according to the 
        direction in which the tank will be moving. It also expands
        the default size of the image to three times it's size
        """
        self.image = r.TANK_IMAGES[self.color][self.direction]
    
    def animate_tank(self):
        """ Changes the image of the tank to create the illusion that the tank tread is moving """
        if self.image == r.TANK_IMAGES[self.color]["{}_{}".format(self.direction, "mov")]:
            self.image = r.TANK_IMAGES[self.color][self.direction]
        elif self.image == r.TANK_IMAGES[self.color][self.direction]:
            self.image = r.TANK_IMAGES[self.color]["{}_{}".format(self.direction, "mov")]

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
        x_coordinate = self.rect.x
        y_coordinate = self.rect.y
        
        if not self.area.contains(self.rect):
            if y_coordinate > self.area.height - self.rect.height and self.direction == c.DOWN:
                self.moving = False
            elif y_coordinate < self.rect.height and self.direction == c.UP:
                self.moving = False
            elif x_coordinate > self.area.width - self.rect.width and self.direction == c.RIGHT:
                self.moving = False
            elif x_coordinate < self.rect.width and self.direction == c.LEFT:
                self.moving = False

        
        
