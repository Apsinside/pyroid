import pygame
import sys
from constants import *
from player import Player
from player import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():  
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable , drawable )
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable , drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers= (updatable)
    AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game over")
                sys.exit()
            for shot in shots:
                if shot.collides(asteroid):
                    asteroid.split()
                    shot.kill()
        #update before
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        #draw before
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()