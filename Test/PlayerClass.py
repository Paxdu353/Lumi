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

    def draw_rays(self, screen):
        mouse_x = pygame.mouse.get_pos()[0] / 140
        start_angle = mouse_x - (FOV * 0.5) / 140

        for _ in range(RAYS_DRAW):
            xe, ye = self.x, self.y
            for j in range(RAYS_MAX_DIST):
                xe += math.cos(start_angle)
                ye += math.sin(start_angle)

                if any(brick.collidepoint(xe, ye) for brick in self.map):
                    break

            pygame.draw.line(screen, RED, (self.x, self.y), (xe, ye), 1)
            start_angle += (RAYS_ANGLE / 140.0)


    def check_collision(self, x_move, y_move):
        """Colision avec map et player\n
            param x_move (int)\n
            param y_move (int)\n
            :return True si collision detect - return False si collision detect
            """
        new_rect = self.rect.move(x_move, y_move)
        for brick in self.map:
            if new_rect.colliderect(brick):
                return True

        return False


    def moove(self):
        """Mouvement du joueur \n
                Z = 0, -1 \n
                S = 0, 1 \n
                D = 1, 0 \n
                Q = -1, 0 \n
                : return None"""
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

    """def vision(self, screen):
        mouse_x = pygame.mouse.get_pos()[0]/140
        xe, ye = self.x + math.cos(mouse_x)*150, self.y + math.sin(mouse_x)*150
        line = pygame.draw.line(screen, RED, (self.x, self.y), (xe, ye), 2)"""


    def draw(self, screen):
        """Dessine player"""
        #pygame.draw.rect(self.screen, WHITE, self.rect)
        pygame.draw.circle(self.screen, WHITE, (self.x, self.y), 5)

