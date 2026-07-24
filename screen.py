import pygame
from Creature import Creature
from CONSTANTS import SCREEN_WIDTH, SCREEN_HEIGHT
from queue import Queue

class LandWindow:
    def __init__(self, processed_images: Queue, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.creature_surfaces = processed_images
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

            self.show_pending_creature()

            current_time = pygame.time.get_ticks()
            if(current_time - last_update >= self.cooldown):
                last_update = current_time
                self.all_sprites.update()
                self.screen.blit(self.bg_img, self.bg_img.get_rect())
                self.all_sprites.draw(self.screen)

                pygame.display.flip()

        pygame.quit()

    def queue_creature(self, path):
        self.pending_creatures.put(path)

    def show_pending_creature(self):
        if not self.pending_creatures.empty():
            path = self.pending_creatures.get()
            self.add_creature_from_file(path)
    
    def add_creature_from_file(self, path):
        Creature.from_file(path, self.all_sprites)

