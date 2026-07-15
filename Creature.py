import pygame
import random

class Creature(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = random.choice(range(2,5))

    def update(self):
        self.rect.x += self.speed