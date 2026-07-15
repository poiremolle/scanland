import pygame
import random
from CONSTANTS import SCREEN_WIDTH, SCREEN_HEIGHT

class Creature(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.w
        self.rect.y = random.choice(
            range(0, SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.2))
            )
        self.speed = random.choice(range(1,5))

    def update(self):
        if(self.rect.x > SCREEN_WIDTH):
            self.rect.x = 0
            return
        self.rect.x += self.speed

        