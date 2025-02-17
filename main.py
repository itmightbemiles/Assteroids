# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

AsteroidField.containers = (updatable,)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #draw frame
        screen.fill("black")
        dt= clock.tick(60) /1000
        updatable.update(dt)

        for sprite in asteroids:
            if player.collision(sprite):
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()
    


if __name__ == "__main__":
    main()





