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
        self.bounce_height = [1, 3, 6, 12, -12, -6, -3, -1]
        self.frame = 0

    def update(self):
        if(self.rect.x > SCREEN_WIDTH):
            self.rect.x = -self.rect.w
            return
        
        self.rect.x += self.speed

        if(self.frame >= len(self.bounce_height)):
            self.frame = 0

        self.rect.y += self.bounce_height[self.frame]
        self.frame += 1

        