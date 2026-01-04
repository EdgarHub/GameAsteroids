from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame
import shot
from player import Player
from asteroid import Asteroid
import asteroidfield
from logger import log_event
import sys

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    play_obj = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield.AsteroidField.containers = (updatable)
    asteroidfield_obj = asteroidfield.AsteroidField()
    asteroidfield.AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if play_obj.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                #pygame.quit()
                sys.exit()

        for asteroid in asteroids:
            for shot_obj in shots:
                if asteroid.collides_with(shot_obj):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot_obj.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
