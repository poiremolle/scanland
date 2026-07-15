import pygame
from imageprocessing import get_surface, remove_white_background
from Creature import Creature
from CONSTANTS import SCREEN_WIDTH, SCREEN_HEIGHT

class LandWindow:
    def __init__(self, width=600, height=500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, 500])
        self.all_sprites = pygame.sprite.Group()
        self.cooldown = 45

    def initialize_land(self):
        running = True
        test_sprite = Creature(
            pygame.image.load("grump-dood.jpg"), 
            self.all_sprites
            )
        
        last_update = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            current_time = pygame.time.get_ticks()

            if(current_time - last_update >= self.cooldown):
                last_update = current_time
                self.all_sprites.update()
                self.screen.fill((230, 215, 255))
                self.all_sprites.draw(self.screen)

                pygame.display.flip()


        pygame.quit()

    def show_img_on_screen(self, imgPath):
        img = remove_white_background(imgPath)
        img.thumbnail((SCREEN_WIDTH * 0.25, SCREEN_HEIGHT))
        surface = get_surface(img)

        Creature(surface, self.all_sprites)

