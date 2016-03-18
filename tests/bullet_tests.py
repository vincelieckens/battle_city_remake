from nose.tools import *
from battle_city_remake.constants import *
from battle_city_remake.bullet import *
from battle_city_remake.resources import *

pygame.init()
pygame.display.set_mode((800, 600))
	
def test_bullet_spawn():
	position_one = (700, 300)
	position_two = (650, 420)
	position_three = (123, 321)
	bullet_one = Bullet(position_one, UP)
	bullet_two = Bullet(position_two, DOWN)
	bullet_three = Bullet(position_three, RIGHT)
	assert_equal(bullet_one.rect.center, position_one)
	assert_equal(bullet_two.rect.center, position_two)
	assert_equal(bullet_three.rect.center, position_three)
