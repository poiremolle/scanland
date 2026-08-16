import pygame
from creature import Creature
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_SPRITE_COUNT
from queue import Queue

class DisplayWindow:
    def __init__(self, processed_images: Queue, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.creature_data = processed_images
        self.all_sprites = pygame.sprite.Group()
        self.deletion_schedule = Queue()
        self.bg_img = pygame.image.load('assets/fixed/background.jpg')
        self.cooldown = 45

    def initialize(self):
        running = True
        last_update = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.creature_data.empty():
                self.show_pending_creature()

            current_time = pygame.time.get_ticks()
            if(current_time - last_update >= self.cooldown):
                last_update = current_time
                self.all_sprites.update()
                self.screen.blit(self.bg_img, self.bg_img.get_rect())
                self.all_sprites.draw(self.screen)

                pygame.display.flip()

        pygame.quit()

    def show_pending_creature(self):
        surface = self.creature_data.get()
        self.create_creature_from_surface(surface)

    def create_surface_from_data(self):
        data = self.creature_data.get()
        return pygame.image.fromstring(
            data[0].tobytes(), data[1], data[2]
        ).convert_alpha()

    def create_creature_from_surface(self, surface):
        if self.deletion_schedule.qsize() > MAX_SPRITE_COUNT:
            self.deletion_schedule.get().flag_for_despawn()

        new = Creature.from_surface(surface, self.all_sprites)
        self.deletion_schedule.put(new)

