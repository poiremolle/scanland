import pygame
import random

from scanland.constants import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    MAX_IMAGE_HEIGHT,
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
        self.rect.y = MAX_IMAGE_HEIGHT
        self.original_image = image
        self.speed = random.choice(range(1,8))
        self.bounce_offsets = [1, 3, 6, 12, -12, -6, -3, -1]
        self.bounce_frame = 0
        self.flagged_for_despawn = False

    def from_surface(surface, creature_group):
        return Creature(surface, creature_group)
    
    def flag_for_despawn(self):
        self.flagged_for_despawn = True

    def update(self):
        if self.off_screen():
            if self.flagged_for_despawn:
                self.remove_from_screen()
                return
  
            self.reset()
           
        self.animate_bounce()
    
    def off_screen(self):
        return self.rect.x > SCREEN_WIDTH  

    def remove_from_screen(self):
        self.kill()
    
    def reset(self):
        new_y = self.generate_random_y()
        scale = self.calculate_scale_from_y(new_y)

        self.update_scale_from_original(scale)
        self.update_position(-self.rect.w, new_y)

    def generate_random_y(self):
        return random.randrange(
            0, int(SCREEN_HEIGHT * MAX_Y_SCALE), Y_STEP  
        )

    def calculate_scale_from_y(self, y):
        return self.map_range(y, 0, SCREEN_HEIGHT, 0.2, 1)
    
    def map_range(self, value, input_min, input_max, output_min, output_max):
        return (value - input_min) * (output_max - output_min) / (input_max - input_min) + output_min

    def update_scale_from_original(self, scale):
        self.image = pygame.transform.scale_by(
            self.original_image, scale
        )
        self.rect = self.image.get_rect()

    def update_position(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y
        
    def animate_bounce(self):
        self.rect.x += self.speed

        self.bounce_frame = (self.bounce_frame + 1) % len(self.bounce_offsets)
        self.rect.y += self.bounce_offsets[self.bounce_frame]    