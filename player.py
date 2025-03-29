import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

# Player class
class Player(CircleShape):
    # initialize the player
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    ### PLAYER ACTIONS ###

    # rotate the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # move the player
    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt

    # shoot a shot
    def shoot(self):
        if self.shot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    
    ### DRAWING + UPDATING ###

    # create player triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 

    # draw the player
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    # read input and update the player
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotate the player
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)

        # move the player
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # update the shot cooldown
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt