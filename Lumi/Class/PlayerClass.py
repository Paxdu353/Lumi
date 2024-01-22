import math

import pygame

import Lumi.Class.AnimationClass as AC
import Lumi.Class.BriqueClass as BC


class Player(AC.AnimationSprite):

    def __init__(self, x_pos, y_pos, main_attack=10, ultime_attack=4, width=32, height=32):
        super().__init__("Player", "Idle")
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.main_attack = main_attack
        self.ultime_attack = ultime_attack
        self.scroll = 0
        self.is_attack = False
        self.original_img = self.image
        self.look = 'RIGHT'
        self.velocity = 0
        self.movement_vector = 0
        self.__velocity_y = 0
        self.__jump_height = 13
        self.__jumps_left = 2
        self.can_move = True
        self.__is_jumping = False
        self.images_list = AC.animations['Player']['Attack']
        self.rect = None



    def update_animation_state(self, screen):
        self.rect = BC.Brique(self.x-55, self.y-100, self.image.get_width()//2, self.image.get_height(), screen)
        if self.movement_vector != 0 and not self.is_attack:
            self.images_list = AC.animations['Player']['Walk']

        if self.is_attack:
            self.animation_delay = 20
            self.images_list = AC.animations['Player']['Attack']
            if self.current_image >= len(self.images_list) - 1:
                self.is_attack = False
                self.animation_delay = 75

        if not self.is_attack and self.movement_vector == 0:
            self.images_list = AC.animations['Player']['Idle']

    def move(self, cle):
        moving = False

        if cle[pygame.K_q] and cle[pygame.K_d]:
            self.movement_vector = 0

        elif cle[pygame.K_d]and self.can_move:
            if self.x < 960 or self.scroll >= 3000:
                moving = True
                self.movement_vector = 1
                self.look = 'RIGHT'
                self.x += 3
                self.last_vector = 1


            else:
                moving = True
                self.movement_vector = 1
                self.last_vector = 1
                self.look = 'RIGHT'
                self.scroll += 1


        elif cle[pygame.K_q]and self.can_move:
            if self.x > 960 or self.scroll <= 0:
                moving = True
                self.last_vector = -1
                self.movement_vector = -1
                self.look = 'LEFT'
                self.x -= 3


            else:
                moving = True
                self.movement_vector = -1
                self.look = 'LEFT'
                self.scroll -= 1

        else:
            self.movement_vector = 0

    def jump(self):
        if self.__jumps_left > 0:
            self.__is_jumping = True
            self.__velocity_y = - self.__jump_height
            self.__jumps_left -= 1

    def update(self, screen):
        self.update_animation_state(screen)

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
        img_width, img_height = self.image.get_width(), self.image.get_height()
        img_x, img_y = self.x - img_width // 2, self.y - img_height // 2

        image_to_draw = pygame.transform.flip(self.image, True, False) if self.look == 'LEFT' else self.image
        screen.blit(image_to_draw, (img_x, img_y))
        self.animate()

        check_colision = pygame.Rect(self.x- 150 , self.y- 150, 300, 300)
        rectsurf = pygame.Surface(check_colision.size, pygame.SRCALPHA)
        rectsurf.fill((255, 100, 0, 100))
        screen.blit(rectsurf, check_colision.topleft)

    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)
