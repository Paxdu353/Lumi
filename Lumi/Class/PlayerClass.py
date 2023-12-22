import pygame
import math

class Player():

    def __init__(self, x_pos, y_pos, main_attack = 10, ultime_attack = 4 , width = 32 , height = 32):
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.main_attack = main_attack
        self.ultime_attack = ultime_attack
        self.scroll = 0
        self.parallax_factor = 0.5
        self.__velocity = 3
        self.__velocity_y = 0
        self.__jump_height = 13
        self.__jumps_left = 2
        self.__is_jumping = False


    def adjust_scroll(self, scroll_amount, width_screen, world_width):
        self.scroll += scroll_amount * self.parallax_factor
        self.scroll = max(0, min(self.scroll, world_width - width_screen))


    def move(self, cle, width_screen, world_width):
        left_limit = width_screen / 4
        right_limit = width_screen * 3 / 4
        if cle[pygame.K_q]:
            if self.x > left_limit:
                self.x -= self.__velocity
            else:
                self.adjust_scroll(-self.__velocity, width_screen, world_width)
        elif cle[pygame.K_d]:
            if self.x < right_limit:
                self.x += self.__velocity
            else:
                self.adjust_scroll(self.__velocity, width_screen, world_width)

    def jump(self):
        if self.__jumps_left > 0:
            self.__is_jumping = True
            self.__velocity_y = - self.__jump_height
            self.__jumps_left -= 1


    def update(self):
        if self.__is_jumping:
            self.__velocity_y += 1
            self.y += self.__velocity_y

            if self.y >= 962:
                self.y = 962
                self.__is_jumping = False
                self.__velocity_y = 0
                self.__jumps_left = 2

    def draw_ammo(self, screen):
        ammo_text = f"Bullet: {self.main_attack}, Ultimate: {self.ultime_attack}"
        font = pygame.font.SysFont(None, 24)
        text = font.render(ammo_text, True, (255, 255, 255))
        screen.blit(text, (10, 10))



    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))


    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)
