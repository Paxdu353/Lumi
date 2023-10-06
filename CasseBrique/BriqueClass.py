import pygame


class Brique:

    def __init__(self, x_pos, y_pos, height, width, color, screen, type = 0):
        self.x = x_pos
        self.y = y_pos
        self.height = height
        self.width = width
        self.color = color
        self.type = type
        self.screen = screen
        self.rect = pygame.Rect(self.width,self.height, self.x, self.y,)





    def draw(self):
        if self.type != 0:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))