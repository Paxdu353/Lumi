import pygame
import math

class Projectile:
    def __init__(self, x, y, angle, speed=7):
        self.x = x
        self.y = y
        self.damage = 10
        self.angle = angle
        self.speed = speed

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def DrawMainAttack(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 20, 20))



