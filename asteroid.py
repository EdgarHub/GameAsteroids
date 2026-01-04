import circleshape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import logger
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return 
        else:
            logger.log_event("asteroid_split")
            ran_an = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(ran_an)
            velocity2 = self.velocity.rotate(-ran_an)
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = velocity1*1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2.velocity = velocity2*1.2
            self.kill()
            return [asteroid1, asteroid2]