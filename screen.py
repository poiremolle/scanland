import pygame
from imageprocessing import get_surface, remove_white_background
from Creature import Creature
from CONSTANTS import SCREEN_WIDTH, SCREEN_HEIGHT

class LandWindow:
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.all_sprites = pygame.sprite.Group()
        self.bg_img = pygame.image.load('background.png')
        self.cooldown = 45

    def initialize_land(self):
        running = True
        last_update = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            current_time = pygame.time.get_ticks()

            if(current_time - last_update >= self.cooldown):
                last_update = current_time
                self.all_sprites.update()
                self.screen.blit(self.bg_img, self.bg_img.get_rect())
                self.all_sprites.draw(self.screen)

                pygame.display.flip()


        pygame.quit()

    def show_creature(self, scanned_img_path):
        pil_image = remove_white_background(scanned_img_path)
        # pil_image.thumbnail((SCREEN_WIDTH * 0.25, SCREEN_HEIGHT))

        surface = get_surface(pil_image)

        Creature(surface, self.all_sprites)

