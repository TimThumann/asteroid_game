import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)


    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_child_1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_child_2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_child_1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_child_2.velocity = self.velocity.rotate(-angle) * 1.2
