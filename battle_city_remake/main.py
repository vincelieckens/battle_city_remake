#!/usr/bin/env python2
# main file of the battle_city_remake

import sys
import os
import pygame
from pygame.locals import *
import resources
import objects


global FPS, WINDOWWIDTH, WINDOWHEIGHT, TITLE, BLACK, WHITE, RIGHT, LEFT, UP, DOWN
global TANK_SIZE, PLAYER1_COLOR, PLAYER2_COLOR, PLAYER1_START_POS, PLAYER2_START_POS 
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
TITLE = 'Battle_city_remake'
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'
TANK_SIZE = (50, 50)
PLAYER_1_COLOR = 'green'
PLAYER_2_COLOR = 'grey' 
PLAYER1_START_POS = DOWN
PLAYER2_START_POS = UP

 
def end_game():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill(BLACK)
    
    resources.load_resources()
    
    player1 = objects.Tank('green', TANK_SIZE, UP, screen)
    player2 = objects.Tank('green', TANK_SIZE, DOWN, screen)
    # initialize cannonball_player1
    # initialize cannonball_player2
    # initialize stonetile
    # initialize map
    allsprites = pygame.sprite.RenderPlain((player1, player2))

    while True:
        clock.tick(FPS)
       
        for event in pygame.event.get():
            if event.type == QUIT:
                end_game()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    end_game()
                elif event.key == K_z:
                    player1.moving(UP)
                elif event.key == K_s:
                    player1.moving(DOWN)
                elif event.key == K_q:
                    player1.moving(LEFT)
                elif event.key == K_d:
                    player1.moving(RIGHT)
                elif event.key == K_UP:
                    player2.moving(UP)
                elif event.key == K_DOWN:
                    player2.moving(DOWN)
                elif event.key == K_LEFT:
                    player2.moving(LEFT)
                elif event.key == K_RIGHT:
                    player2.moving(RIGHT)
        
        allsprites.update()
        screen.blit(background,(0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    main()
        

