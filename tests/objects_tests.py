from nose.tools import *
from battle_city_remake.objects import *
import pygame


def test_tank():
    grey_tank = Tank('grey', 'down')
    green_tank = Tank('green', 'up')
    assert_equal(grey_tnnk.rect.topleft, (400, 400))
    assert_equal(green_tank.rect.topleft, (200, 200))
    
def test_tank_move():
    grey_tank = Tank('grey', 'down')
    green_tank = Tank('green', 'up')
    grey_tank.move_up()
    assert_equal(grey_tank.moving, 'up')
    green_tank.move_down()
    assert_equal(green_tank.moving, 'down')
    grey_tank.move_left()
    assert_equal(grey_tank.moving, 'left')
    green_tank.move_right()
    assert_equal(green_tank.moving, 'right')
    
    
    
