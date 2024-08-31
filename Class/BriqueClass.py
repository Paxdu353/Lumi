import pygame
class Brique:
    def __init__(self, x_pos, y_pos, width, height, screen, img, index, scroll, colision = True):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.__screen = screen
        self.__is_visible = True
        self.img = img
        self.scroll = scroll
        self.index = index
        self.rect = self.rect_info()
        self.check_col = False
        self.has_colision = colision
        self.abs_x = x_pos + (abs(scroll))

    def resize(self, width, height):
        self.height = height
        self.width = width

    def relocate(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect.x = x_pos

    def change(self, x_pos, y_pos, width, height):
        self.relocate(x_pos, y_pos)
        self.resize(width, height)

    def show(self):
        self.__is_visible = True

    def hide(self):
        self.__is_visible = False

    def draw(self, screen):
        if self.__is_visible and (self.x_pos > 0 - self.width) and self.y_pos <= 1920:
            screen.blit(pygame.transform.scale(self.img, (64, 64)), self.rect_info())

    def rect_info(self):
        return pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def collidepoint(self, x, y):
        return self.rect_info().collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect_info().colliderect(rect)

    def collide(self, rects):
        return self.rect_info().collidelist(rects) != -1

    def list_info(self):
        return [self.x_pos, self.y_pos, self.width, self.height]

    def copy(self):
        return self.rect_info().copy()

    def bottom(self):
        return self.rect_info().bottom

    def top(self):
        return self.rect_info().top

    def __repr__(self):
        return f"{self.abs_x}, {self.y_pos}, {self.width}, {self.height}, {self.index}, {int(self.has_colision)}"

