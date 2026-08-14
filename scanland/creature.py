import pygame
import random

from constants import (
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
        self.flagged_for_despawn = False
        self.reset()  

    def from_surface(surface, creature_group):
        return Creature(surface, creature_group)    

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
        depth_scale = max(MIN_Y, new_y) / SCREEN_HEIGHT
        self.image = pygame.transform.scale_by(
            self.original_image, depth_scale
            )
        self.rect = self.image.get_rect()

    def update_position(self, new_y):
        self.rect.x = -self.rect.w
        self.rect.y = new_y

    def animate_bounce(self):
        self.rect.x += self.speed

        self.bounce_frame = (self.bounce_frame + 1) % len(self.bounce_offsets)
        self.rect.y += self.bounce_offsets[self.bounce_frame]

    def update(self):
        if self.off_screen():
            if self.flagged_for_despawn:
                self.remove_from_screen()
                return
  
            self.reset()
           
        self.animate_bounce()

    def flag_for_despawn(self):
        self.flagged_for_despawn = True

    def remove_from_screen(self):
        self.kill()