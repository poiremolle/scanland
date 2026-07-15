import pygame
import random
from CONSTANTS import SCREEN_WIDTH

class Creature(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # self.speed = random.choice(range(2,5))
        self.speed = 1

    def update(self):
        if(self.rect.x > SCREEN_WIDTH):
            self.rect.x = 0
            return
        self.rect.x += self.speed

        