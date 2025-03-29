import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
# main function
def main():
    # initialize pygame
    pygame.init()

    # set up the clock
    clock = pygame.time.Clock()
    dt = 0

    # set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # set containers for Player class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    # create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create the asteroid field
    asteroid_field = AsteroidField()

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update the game state
        dt = clock.tick(60) / 1000

        # clear the screen
        screen.fill((0, 0, 0))
        
        # update the player
        updatable.update(dt)

        # draw the player
        for sprite in drawable:
            sprite.draw(screen)

        # update the display
        pygame.display.flip()
 
    # clean up
    pygame.quit()

if __name__ == "__main__":
    main()