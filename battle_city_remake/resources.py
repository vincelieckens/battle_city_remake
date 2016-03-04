# This module loads all the resources needed for the game to run
# such as the sprite images


import os.path
import pygame
from pygame.locals import *


def load_image(filename, color, colorkey=None):
    """ 
    Loads the sprite of a given name, and sets the colorkey
    for this sprite if wanted.
    Positional arguments:
    - name : filename of the sprite
    - color : specify the color of the tank
    """
    fullname = os.path.join(os.path.expanduser('~'), 'projecten', 'games', 'battle_city_remake', 'battle_city_remake', 'data', 'tanks', color, filename)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def load_resources():
    global tank_sprites
    tank_sprite_files = ('Sprite_1.png', 'Sprite_3.png', 'Sprite_5.png', 'Sprite_7.png')
    tank_sprites = [load_image(sprite_name, 'green') for sprite_name in tank_sprite_files]
    tank_directions = ('up', 'left', 'down', 'right')
    tank_sprites = dict(zip(tank_directions, tank_sprites))


