import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    # set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update the display
        screen.fill((0, 0, 0))
        pygame.display.flip()
 
    # clean up
    pygame.quit()

if __name__ == "__main__":
    main()