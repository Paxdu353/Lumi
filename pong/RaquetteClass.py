import pygame
class Raquette:

    def __init__(self, rect, color, player):
        self.color = color
        self.rect = rect
        self.player = player

    def move(self):
        if self.player == True:
            if pygame.key.get_pressed()[pygame.K_z]:
                if self.rect.top > 0:
                    self.rect.y -= 1

            if pygame.key.get_pressed()[pygame.K_s]:
                if self.rect.bottom < 240:
                    self.rect.y += 1
        else:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if self.rect.top > 0:
                    self.rect.y -= 1

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if self.rect.bottom < 240:
                    self.rect.y += 1

    def IA_Move(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)