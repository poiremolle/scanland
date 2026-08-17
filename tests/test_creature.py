import pytest
import pygame
from scanland.creature import Creature
from scanland.constants import SCREEN_WIDTH

all_sprites = pygame.sprite.Group()

@pytest.fixture
def creature():
    image = pygame.image.load("tests/test_assets/appleworm.jpg")
    return Creature(image, all_sprites)

def test_update_position(creature):
    creature.update_position(1000, 1000)
    assert creature.rect.x == 1000
    assert creature.rect.y == 1000

def test_off_screen_true(creature):
    creature.update_position(SCREEN_WIDTH + 10, 0)
    assert creature.off_screen() == True

def test_off_screen_false(creature):
    creature.update_position(0,0)
    assert creature.off_screen() == False

def test_flag_for_despawn(creature):
    creature.flag_for_despawn()
    assert creature.flagged_for_despawn == True

def test_remove_from_screen(creature):
    current_len = len(all_sprites)
    creature.remove_from_screen()
    assert len(all_sprites) == current_len - 1