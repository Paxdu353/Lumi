import pygame


class Brique:

    def __init__(self, x_pos, y_pos, width, height, screen, color=(255, 255, 255)):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__width = width
        self.__height = height

        self.__screen = screen
        self.__is_visible = True
        self.__init = pygame.Rect(x_pos, y_pos, width, height)
        self.__color = color


    def resize(self, width, height):
        self.__init = pygame.Rect(self.__x_pos, self.__y_pos, width, height)

    def relocate(self, x_pos, y_pos):
        self.__init = pygame.Rect(x_pos, y_pos, self.__width, self.__height)

    def change(self, x_pos, y_pos, width, height):
        self.__init = pygame.Rect(x_pos, y_pos, width, height)

    def change_color(self, r, g, b):
        self.__color = (r, g, b)

    def show(self):
        self.__is_visible = True

    def hide(self):
        self.__is_visible = False

    def draw(self, screen):
        if self.__is_visible:
            pygame.draw.rect(screen, self.color, self.__init)