import pygame
from imageprocessing import get_surface_image

def initialize_land():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((230, 215, 255))

        surfaceImage = get_surface_image('apple.JPG')

        screen.blit(surfaceImage, (0, 0))

        pygame.display.flip()

    pygame.quit()

