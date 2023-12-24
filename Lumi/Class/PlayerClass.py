import pygame
import math
import Lumi.Class.AnimationClass as AC

class Player(AC.AnimationSprite):

    def __init__(self, x_pos, y_pos, main_attack = 10, ultime_attack = 4 , width = 32 , height = 32):
        super().__init__("Player", "Idle")
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.main_attack = main_attack
        self.ultime_attack = ultime_attack
        self.scroll = 0
        self.is_attack = False
        self.attack_anim = AC.animations.get('Player', 'Attack')
        self.original_img = self.image
        self.__velocity = 3
        self.__movement_vector = 1
        self.__velocity_y = 0
        self.__jump_height = 13
        self.__jumps_left = 2
        self.__is_jumping = False

    def start_attack(self):
        self.is_attack = True
        self.current_image = 0
        self.images_list = self.attack_anim


    def update_animation_state(self):
        if self.__movement_vector != 0:
            self.images_list = AC.animations['Player']['Walk']

        elif self.is_attack:
            self.images_list = self.attack_anim
            self.current_image = 0
            self.is_attack = True


        else:
            self.images_list = AC.animations['Player']['Idle']



    def move(self, cle):
        moving = False
        if cle[pygame.K_q]:
            self.x -= self.__velocity
            moving = True
            self.__movement_vector = -1
            if self.scroll > 0: self.scroll -= 1

        elif cle[pygame.K_d]:
            self.x += self.__velocity
            moving = True
            self.__movement_vector = 1
            if self.scroll < 3000: self.scroll += 1

        else:
            self.__movement_vector = 0



    def jump(self):
        if self.__jumps_left > 0:
            self.__is_jumping = True
            self.__velocity_y = - self.__jump_height
            self.__jumps_left -= 1



    def update(self):

        self.update_animation_state()


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
        img_width = self.image.get_width()
        img_height = self.image.get_height()

        img_x = self.x - img_width // 2
        img_y = self.y - img_height // 2

        image_to_draw = pygame.transform.flip(self.image, True, False) if self.__movement_vector == -1 else self.image
        screen.blit(image_to_draw, (img_x, img_y))
        self.animate()


    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)
