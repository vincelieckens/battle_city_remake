#!/usr/bin/env python2
# main file of the battle_city_remake


import pygame
import game_objects

def set_globals(player1_color, player1_pos, player2_color, player2_pos):
    FPS = 30
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    TITLE = 'Battle_city_remake'
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PLAYER_1_COLOR = ""
    PLAYER_2_COLOR = "" 
    PLAYER1_START_POS = 0
    PLAYER2_START_POS = 0
    global FPS, WINDOWWIDTH, WINDOWHEIGHT, TITLE, BLACK, WHITE
    global PLAYER1_COLOR, PLAYER2_COLOR, PLAYER1_START_POS, PLAYER2_START_POS

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
    
    green_tank = game_objects.Tank("green")
    allsprites = pygame.sprite.RenderPlain((green_tank))

    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                end_game()
            elif event.type = K_ESCAPE:
                end_game()
                
                
        #allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    main()
