import math

import pygame


import pygame
import math

class Projectile:
    def __init__(self, x, y, angle, speed=7, image_path='images/Player/Attack.png'):
        self.x = x
        self.y = y
        self.damage = 10
        self.angle = angle
        self.speed = speed
        self.rotation_angle = 0
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image
        self.image = pygame.transform.scale(self.image, (50, 50))


    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        self.rotation_angle += 5
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)


    def DrawMainAttack(self, screen):
        rect = self.image.get_rect()
        rect.center = (self.x, self.y)
        screen.blit(self.image, rect)

