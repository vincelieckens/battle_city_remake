from nose.tools import *
from battle_city_remake.constants import *
from battle_city_remake.tile import *
from battle_city_remake.resources import *

pygame.init()
pygame.display.set_mode((800, 600))
	
def test_tile_spawn():
	position_one = (700, 300)
	position_two = (650, 420)
	position_three = (123, 321)
	tile_one = Tile(position_one)
	tile_two = Tile(position_two)
	tile_three = Tile(position_three)
	assert_equal(tile_one.rect.center, position_one)
	assert_equal(tile_two.rect.center, position_two)
	assert_equal(tile_three.rect.center, position_three)
