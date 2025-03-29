import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # initialize the circle shape
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # draw the circle shape
    def draw(self, screen):
        pass

    # update the circle shape
    def update(self, dt):
        pass

    # check if the circle shape is colliding with another object 
    def is_colliding(self, other):
        return self.position.distance_to(other.position) < self.radius + other.radius
