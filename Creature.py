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
        self.rect.x = -self.rect.w
        self.original_image = image
        self.speed = random.choice(range(1,8))
        self.bounce_offsets = [1, 3, 6, 12, -12, -6, -3, -1]
        self.bounce_frame = 0
        self.reset()  

    def from_surface(surface, creature_group):
        Creature(surface, creature_group)    

    def off_screen(self):
        return self.rect.x > SCREEN_WIDTH  
    
    def reset(self):
        new_y = self.generate_random_y()
        self.update_scale(new_y)
        self.update_position(new_y)

    def generate_random_y(self):
        return random.randrange(
            MIN_Y, SCREEN_HEIGHT * MAX_Y_SCALE, Y_STEP  
        )
        
    def update_scale(self, new_y):
        print(f"current w: {self.rect.w}")
        depth_scale = max(MIN_Y, new_y) / SCREEN_HEIGHT
        self.image = pygame.transform.scale_by(
            self.original_image, depth_scale
            )
        self.rect = self.image.get_rect()
      
        print(f"new y: {new_y}, scaled by: {depth_scale}, new w: {self.rect.w}")

    def update_position(self, new_y):
        self.rect.x = -self.rect.w
        print(f"new x: {self.rect.x}")
        self.rect.y = new_y

    def animate_bounce(self):
        self.rect.x += self.speed

        self.bounce_frame = (self.bounce_frame + 1) % len(self.bounce_offsets)
        self.rect.y += self.bounce_offsets[self.bounce_frame]

    def update(self):
        if self.off_screen():
            print(f"is off screen, x: {self.rect.x}")
            self.reset()
           
        self.animate_bounce()