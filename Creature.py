import pygame
import random
from CONSTANTS import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    MAX_Y_SCALE, 
    Y_STEP, 
    MIN_Y
)

class Creature(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.original_image = image
        self.speed = random.choice(range(1,8))
        self.bounce_offsets = [1, 3, 6, 12, -12, -6, -3, -1]
        self.bounce_frame = 0
        self.update_scale()
        self.reset_position()
        

    def off_screen(self):
        return self.rect.x > SCREEN_WIDTH  

    def reset_position(self):
        self.rect.x = -self.rect.w
        self.rect.y = random.randrange(
                MIN_Y, SCREEN_HEIGHT * MAX_Y_SCALE, Y_STEP  
            )
        print(f"y: {self.rect.y}")
        
    def update_scale(self):
        depth_scale = max(MIN_Y, self.rect.y) / SCREEN_HEIGHT
        print(f"depth scale: {depth_scale}")
        self.image = pygame.transform.scale_by(self.original_image, depth_scale)

    def animate_bounce(self):
        self.rect.x += self.speed

        self.bounce_frame = (self.bounce_frame + 1) % len(self.bounce_offsets)
        self.rect.y += self.bounce_offsets[self.bounce_frame]

    def update(self):
        if self.off_screen():
            self.update_scale()
            self.reset_position()
           
        self.animate_bounce()