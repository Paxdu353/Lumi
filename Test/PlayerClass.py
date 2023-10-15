import pygame
import math
from Constants import *

class Player:


    def __init__(self, x_pos, y_pos, screen, map):
        self.x = x_pos
        self.y = y_pos
        self.screen = screen
        self.map = map
        self.rect = pygame.Rect(self.x-5, self.y-5, 10, 10)

    def get_pos(self):
        return self.x // 50, self.y // 50

    def get_angle(self, x, y):
        return math.atan2(y-self.y, x-self.x)

    def check_collision(self, x_move, y_move):
        new_rect = self.rect.move(x_move, y_move)
        for brick in self.map:
            if new_rect.colliderect(brick):
                return True

        return False

    def vision(self, screen):
        mouse_x = pygame.mouse.get_pos()[0] / 140

        for i in range(RAYS_DRAW):
            xe = self.x + math.cos(mouse_x ) * RAYS_MAX_DIST
            ye = self.y + math.sin(mouse_x ) * RAYS_MAX_DIST
            line = pygame.draw.line(screen, RED, (self.x, self.y), (xe, ye), 2)

    def moove(self):
        if pygame.key.get_pressed()[pygame.K_z]:
            if not self.check_collision(0, -1):
                self.y -= 1
        if pygame.key.get_pressed()[pygame.K_s]:
            if not self.check_collision(0, 1):
                self.y += 1
        if pygame.key.get_pressed()[pygame.K_d]:
            if not self.check_collision(1, 0):
                self.x += 1
        if pygame.key.get_pressed()[pygame.K_q]:
            if not self.check_collision(-1, 0):
                self.x -= 1

        self.rect.x, self.rect.y = (self.x-5, self.y-5)



    def draw(self, screen):
        #pygame.draw.rect(self.screen, WHITE, self.rect)
        pygame.draw.circle(self.screen, WHITE, (self.x, self.y), 5)

