from nose.tools import *
from battle_city_remake.objects import *
import pygame

pygame.init()
pygame.display.set_mode((800, 600))

def test_tank():
    grey_tank = Tank('grey', 'down')
    green_tank = Tank('green', 'up')
    assert_equal(grey_tank.rect.topleft, (400, 400))
    assert_equal(green_tank.rect.topleft, (200, 200))
    
def test_tank_move():
    grey_tank = Tank('grey', 'down')
    green_tank = Tank('green', 'up')
    grey_tank.moving('up')
    assert_equal(grey_tank.direction, 'up')
    green_tank.moving('down')
    assert_equal(green_tank.direction, 'down')
    grey_tank.moving('left')
    assert_equal(grey_tank.direction, 'left')
    green_tank.moving('right')
    assert_equal(green_tank.direction, 'right')
    
def test_tank_update():
    grey_tank = Tank('grey', 'down')
    green_tank = Tank('green', 'up')
    grey_tank.moving('up')
    grey_tank.update()
    assert_equal(grey_tank.rect.topleft, (400, 390))
    green_tank.moving('down')
    green_tank.update()
    assert_equal(green_tank.rect.topleft, (200, 210))
    
    
    
