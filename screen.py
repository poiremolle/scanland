import pygame
from imageprocessing import get_surface, remove_white_background

class LandWindow:
    def __init__(self, width=600, height=500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([500, 500])
        self.all_sprites = pygame.sprite.Group()

    def initialize_land(self):
        running = True
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()
            self.screen.fill((230, 215, 255))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()


        pygame.quit()

    def show_img_on_screen(self, imgPath):
        img = remove_white_background(imgPath)
        surface = get_surface(img)
        # Create sprite here 
        # self.screen.blit(surface, (0, 0))
        pygame.display.flip()

