import pygame
import math
from Constants import *


def cross_product(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2


def is_brick_between_lines(px, py, x1, y1, x2, y2, brick):
    # Disons que la brique est un rectangle avec des coins top-left (bx1, by1) et bottom-right (bx2, by2)
    bx1, by1, bx2, by2 = brick.topleft[0], brick.topleft[1], brick.bottomright[0], brick.bottomright[1]

    corners = [(bx1, by1), (bx2, by1), (bx2, by2), (bx1, by2)]

    # Calculer les produits vectoriels pour chaque coin par rapport aux deux lignes.
    sides_line1 = [cross_product(x1 - px, y1 - py, cx - px, cy - py) for cx, cy in corners]
    sides_line2 = [cross_product(x2 - px, y2 - py, cx - px, cy - py) for cx, cy in corners]

    # Si tous les coins sont du même côté de l'une des lignes, alors la brique est en dehors du FOV.
    # Autrement dit, si tous les produits vectoriels ont le même signe pour une ligne, alors tous les coins
    # sont du même côté de cette ligne.
    if all(side >= 0 for side in sides_line1) or all(side <= 0 for side in sides_line1):
        return False
    if all(side >= 0 for side in sides_line2) or all(side <= 0 for side in sides_line2):
        return False

    return True


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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x /= 140

        start_angle = mouse_x - (FOV * 0.5)
        angle_increment = RAYS_ANGLE / FOV

        cos_values = [math.cos(start_angle + i * angle_increment) for i in range(RAYS_DRAW)]
        sin_values = [math.sin(start_angle + i * angle_increment) for i in range(RAYS_DRAW)]

        for i in range(RAYS_DRAW):
            xe, ye = self.x, self.y

            for j in range(RAYS_MAX_DIST):
                xe += cos_values[i]
                ye += sin_values[i]

                brique = [brick.collidepoint(xe, ye) for brick in self.map]
                if any(brique):
                    break
            pygame.draw.line(screen, RED, (self.x, self.y), (xe, ye), 1)

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

