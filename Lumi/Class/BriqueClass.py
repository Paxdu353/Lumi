import pygame


class Brique:
    def __init__(self, x_pos, y_pos, width, height, screen, color=(255, 255, 255)):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.__screen = screen
        self.__is_visible = True
        self.color = color

    def resize(self, width, height):
        self.height = height
        self.width = width

    def relocate(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def change(self, x_pos, y_pos, width, height):
        self.relocate(x_pos, y_pos)
        self.resize(width, height)

    def change_color(self, r, g, b):
        self.color = (r, g, b)

    def show(self):
        self.__is_visible = True

    def hide(self):
        self.__is_visible = False

    def draw(self, screen):
        if self.__is_visible and (self.x_pos > 0 - self.width) and self.y_pos <= 1920:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))

    def collidepoint(self, x, y):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height).collidepoint(x, y)

    def colliderect(self, rect):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height).colliderect(rect)

    def list_info(self):
        return [self.x_pos, self.y_pos, self.width, self.height, self.color]

    def __repr__(self):
        return f"{self.x_pos}, {self.y_pos}, {self.width}, {self.height}, {self.color}"

