import pygame
import math
class Player:

    def __init__(self, rect, color):
        self.color = color
        self.rect = rect

    def aller(self, mouse):
        if self.rect.x != mouse[0]:
            difference = mouse[0] - self.rect.x
            self.rect.x += min(difference//10, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)