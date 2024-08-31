import pygame
class Button:

    def __init__(self, x: int, y: int, text: str, color: (int, int, int), size: int):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size
        self.rect = self.render().get_rect()
        self.rect.topleft = (self.x, self.y)


    def font(self):
        return pygame.font.Font("images/font.ttf", self.size)

    def render(self):
        return self.font().render(self.text, True, self.color)

    def change_text(self, new_text: str):
        self.text = new_text

    def check_colision(self, x, y):
        if self.rect.collidepoint(x, y):
            self.color = (105, 4, 43)


    def draw_text(self, screen):
        screen.blit(self.render(), (self.x, self.y))

    def draw_rect(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)







