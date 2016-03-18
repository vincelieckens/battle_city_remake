# This module loads all the necessary resources for the game

import os.path
import os
import pygame
import tank
import constants as c
from pygame.locals import *

    
def load_tank_images_new(colors):
	tank_images =  {}
	
	for color in colors:
		tank_folder = os.path.join('tanks', color)
		images = load_images(tank_folder)
		tank_images[color] = images
	
	return tank_images
		

def load_images(directory, colorkey=(0, 0, 0), accept=('.png', '.jpg', '.bmp')):
	images = {}
	
	for img in os.listdir(os.path.join('battle_city_remake', 'data', directory)):
		name, ext = os.path.splitext(img)
		if ext.lower() in accept:
			image = pygame.image.load(os.path.join('battle_city_remake', 'data', directory, img))
			if image.get_alpha():
				image = image.convert_alpha()
			else:
				image = image.convert()
				image.set_colorkey(colorkey)
			images[name] = image
	return images


pygame.init()
pygame.display.set_caption(c.TITLE) 
SCREEN = pygame.display.set_mode(c.SCREEN_SIZE)   
TANK_IMAGES = load_tank_images_new(c.COLORS)
TILE_IMAGES = load_images('tiles')
BULLET_IMAGES = load_images('bullets')


# Debugging
if __name__ == '__main__':
	print TILE_IMAGES


