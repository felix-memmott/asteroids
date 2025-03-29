import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

# Shot class
class Shot(CircleShape):
    # initialize the shot
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # update the shot
    def update(self, dt):
        self.position += self.velocity * dt

    # draw the shot
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
