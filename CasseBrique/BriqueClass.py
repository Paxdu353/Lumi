import random
import pygame


class Brique:

    def __init__(self, x_pos, y_pos, width, height, screen, type = 0):
        self.x = x_pos
        self.y = y_pos
        self.height = height
        self.width = width
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.type = type
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def PU(self):
        pass
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def __repr__(self):
        return str((self.x, self.y))