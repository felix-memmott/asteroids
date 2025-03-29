import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

# Asteroid class
class Asteroid(CircleShape):
    # initialize the asteroid
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    # update the asteroid's position
    def update(self, dt):
        self.position += self.velocity * dt

    # split the asteroid into two smaller asteroids
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create first asteroid
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        
        # Create second asteroid
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
        