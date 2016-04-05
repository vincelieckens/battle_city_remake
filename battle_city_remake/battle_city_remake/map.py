# This module holds the Map class

import pygame
import constants as c 
import tank
import bullet
import tile
# import explosion

class Map(object):
    
    def __init__(self):
        self.playerone = Tank(c.GREEN, c.UP)
        self.playertwo = Tank(c.GREY, c.DOWN)
        
        # Function that needs to load a specific amount of tiles
