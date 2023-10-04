import pygame


class Brique:

    def __init__(self, x_pos, y_pos, height, width, color):
        self.x = x_pos
        self.y = y_pos
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(self.width,self.height, self.x, self.y,)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))