
import pygame
import math

import Lumi.Class.BriqueClass as BC

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
        self.hitbox = None


    def move(self):

        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        self.rotation_angle += 5
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)

    def update(self, screen):
        self.hitbox = BC.Brique(self.x - (self.image.get_width() // 2) + 5, self.y - (self.image.get_height() // 2) + 10, self.image.get_width() - 10, self.image.get_height() - 10, screen, pygame.image.load("images/Tiles/Tile_2.png"), 0, 0)


    def DrawMainAttack(self, screen):
        rect = self.image.get_rect()
        # pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
        rect.center = (self.x, self.y)
        screen.blit(self.image, rect)

        '''check_colision = pygame.Rect(self.x - 150, self.y - 150, 300, 300)
        rectsurf = pygame.Surface(check_colision.size, pygame.SRCALPHA)
        rectsurf.fill((255, 100, 0, 100))
        screen.blit(rectsurf, check_colision.topleft)'''

