import pygame
from imageprocessing import get_surface_image

class LandWindow:
    def __init__(self, width=600, height=500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([500, 500])

    def initialize_land(self):
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((230, 215, 255))

            surfaceImage = get_surface_image('apple.jpg')

            self.screen.blit(surfaceImage, (0, 0))

            pygame.display.flip()

        pygame.quit()

