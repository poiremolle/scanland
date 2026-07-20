import pygame
from Creature import Creature
from CONSTANTS import SCREEN_WIDTH, SCREEN_HEIGHT

class LandWindow:
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.queue = Queue()
        self.all_sprites = pygame.sprite.Group()
        self.bg_img = pygame.image.load('assets/fixed/background.png')
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

    def add_creature_from_file(self, path):
        Creature.from_file(path, self.all_sprites)

