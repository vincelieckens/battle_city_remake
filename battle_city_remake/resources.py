# This module loads all the necessary resources for the game

import os.path
import os
import pygame
import constants as c
from pygame.locals import *

    
def load_tank_images_new(colors_folders):
    """ 
    The tank images are structured in a folder named tanks, which is
    further divided into folders that store tank images according to 
    color. This function accepts a list of names of these folders 
    and calls the load_images function for each color in this list.
    Returns a 2d dictionary of the tank images with the color and name
    of the image as keys, while the values are the images themselves.
    """
    tank_images =  {}
    
    for color in colors_folders:
        tank_folder = os.path.join('tanks', color)
        images = load_images(tank_folder)
        tank_images[color] = images
    
    return tank_images
        

def load_images(directory, colorkey=c.BLACK, size = 3, accept=('.png', '.jpg', '.bmp')):
    """
    This function loads all the images in a specified directory, 
    transforms these images according to the given colorkey, which
    is black by default. It returns a dictionary with the names of
    the images as keys, while the values are the images themselves.
    The size argument determines the size of the loaded images,
    """
    images = {}
    
    for img in os.listdir(os.path.join('data', directory)):
        name, ext = os.path.splitext(img)
        
        if ext.lower() in accept:
            image = pygame.image.load(os.path.join('data', directory, img))
            if image.get_alpha():
                image = image.convert_alpha()
            else:
                image = image.convert()
                image.set_colorkey(colorkey)
            expanded_image = pygame.transform.scale(image, (image.get_width() * size, image.get_height() * size))
            images[name] = expanded_image
    
    return images


SCREEN = pygame.display.set_mode(c.SCREEN_SIZE)
pygame.display.set_caption(c.TITLE)   
TANK_IMAGES = load_tank_images_new(c.COLORS)
TILE_IMAGES = load_images('tiles', size = 1)
BULLET_IMAGES = load_images('bullets')


# Debugging
if __name__ == '__main__':
    print TILE_IMAGES


