import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x, self.position.y),self.radius, 2)
    def update(self, dt):
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split1 = self.velocity.rotate(split_angle)
            split2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid1.velocity = split1 *1.2
            asteroid2.velocity = split2 *1.2
            for group in self.groups():
                group.add(asteroid1)
                group.add(asteroid2)

            




