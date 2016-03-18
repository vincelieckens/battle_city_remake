from nose.tools import *
from battle_city_remake.constants import *
from battle_city_remake.tank import *
from battle_city_remake.resources import *

pygame.init()
pygame.display.set_mode((800, 600))

def test_tank_position():
	green_tank = Tank('green', 'up')
	grey_tank = Tank('grey', 'down')
	assert_equal(green_tank.rect.center, (r.SCREEN.get_width() / 2, r.SCREEN.get_height() - r.SCREEN.get_height() / 4))
	assert_equal(grey_tank.rect.center, (r.SCREEN.get_width() / 2, r.SCREEN.get_height() / 4))
