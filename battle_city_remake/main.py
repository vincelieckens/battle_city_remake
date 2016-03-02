#!/usr/bin/env python2
# main file of the battle_city_remake


import pygame
import objects
from pygame.locals import *
import sys

def set_globals():
    global FPS, WINDOWWIDTH, WINDOWHEIGHT, TITLE, BLACK, WHITE
    global PLAYER1_COLOR, PLAYER2_COLOR, PLAYER1_START_POS, PLAYER2_START_POS
    
    FPS = 30
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    TITLE = 'Battle_city_remake'
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PLAYER_1_COLOR = 'green'
    PLAYER_2_COLOR = 'grey' 
    PLAYER1_START_POS = 'down'
    PLAYER2_START_POS = 'up'


def end_game():
    pygame.quit()
    sys.exit()

def main():
    global FPS, WINDOWWITH, WINDOWHEIGHT, BLACK, WHITE
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill(BLACK)
    
    player1 = game_objects.Tank(PLAYER_1_COLOR, PLAYER_1_START_POS)
    player2 = game_objects.Tank(PLAYER_2_COLOR, PLAYER_2_START_POS)
    # initialize cannonball_player1
    # initialize cannonball_player2
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
                    green_tank.move_up()
                elif event.key == K_s:
                    green_tank.move_down()
                elif event.key == K_q:
                    green_tank.move_left()
                elif event.key == K_d:
                    green_tank.move_right()
            # elif event.type = KEYDOWN:
                
        # Debugging
        print green_tank.moving    
                
        #allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    set_globals()
    main()
