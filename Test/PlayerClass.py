import pygame
import math

class Player:


    def __init__(self, x_pos, y_pos, screen, map):
        self.x = x_pos
        self.y = y_pos
        self.screen = screen
        self.map = map
        self.rect = pygame.Rect((5, 5), (self.x, self.y))

    def get_pos(self):
        return self.x // 50, self.y // 50

    def moove(self):
        if pygame.key.get_pressed()[pygame.K_z]:

            self.y -= 1

        if pygame.key.get_pressed()[pygame.K_s]:
            self.y += 1

        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += 1

        if pygame.key.get_pressed()[pygame.K_q]:
            self.x -= 1

        #print(pygame.mouse.get_rel())

    def vision(self, screen):
        mouse_x = pygame.mouse.get_pos()[0]/140
        xe, ye = self.x + math.cos(mouse_x)*100, self.y + math.sin(mouse_x)*100
        line = pygame.draw.line(screen, (0, 255, 255), (self.x, self.y), (xe, ye), 2)


    def draw(self, screen):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 5)

