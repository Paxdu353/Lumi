import pygame
import Class.ProjectileClass as PCP
import math

class Player():

    def __init__(self, x_pos, y_pos,main_attack = 10, ultime_attack = 4, width = 32, height = 32, ):
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.main_attack = main_attack
        self.ultime_attack = ultime_attack
        self.__velocity = 3
        self.__velocity_y = 0
        self.__jump_height = 13
        self.__jumps_left = 2
        self.__is_jumping = False


    def move(self, cle, width_screen):
        if cle[pygame.K_q]:
            if self.x <= 0:
                self.x = 0
            else:
                self.x -= self.__velocity

        elif cle[pygame.K_d]:
            if self.x >= width_screen - self.width:
                self.x = width_screen - self.width
            else:
                self.x += self.__velocity

    def jump(self):
        if self.__jumps_left > 0:
            self.__is_jumping = True
            self.__velocity_y = - self.__jump_height
            self.__jumps_left -= 1


    def update(self):
        if self.__is_jumping:
            self.__velocity_y += 1
            self.y += self.__velocity_y

            if self.y >= 750:
                self.y = 750
                self.__is_jumping = False
                self.__velocity_y = 0
                self.__jumps_left = 2



    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))


    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)
