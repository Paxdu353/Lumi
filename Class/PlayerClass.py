import math
import pygame
import Class.AnimationClass as AC
import Class.BriqueClass as BC
from settings import *


class Player(AC.AnimationSprite):

    def __init__(self, x_pos = 100, y_pos = 962, main_attack=10, ultime_attack=4, width=32, height=32):
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
        self.hp = 6
        self.velocity = 5
        self.movement_vector = 0
        self.vec_sup = 0
        self.vec_last = 0
        self.velocity_y = 0
        self.gravity = 0.5
        self.jumps_left = 2
        self.jump_speed = -12
        self.can_move = True
        self.__is_jumping = False
        self.hitbox = None
        self.bottom_collide = False


    def update_animation_state(self, screen):
        self.hitbox = BC.Brique(self.x-50, self.y-95, (self.image.get_width()//2) - 30, (self.image.get_height()//2) + 50,screen , pygame.image.load("images/Tiles/Tile_2.png"), 1, 0)
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

    def apply_gravity(self):
        self.velocity_y += self.gravity
        if self.y + self.height + self.velocity_y > 975:
            self.velocity_y = 0
            self.y = 975 - self.height
            self.jumps_left = 2
        else:
            self.y += self.velocity_y



    def check_vertical_collision(self, briques):
        self.apply_gravity()
        for brique in briques:
            if brique.has_colision:
                if brique.y_pos < self.hitbox.y_pos:
                    if self.hitbox != None and self.hitbox.colliderect(brique):
                        self.velocity_y = 0
                        self.y = brique.bottom() + (self.image.get_height() // 2)
                        break

                elif brique.y_pos > self.hitbox.y_pos and self.velocity_y > 0:
                    self.hitbox.y_pos += 1
                    if self.hitbox != None and self.hitbox.colliderect(brique):
                        self.velocity_y = 0
                        self.y = brique.top() - ((self.image.get_height() // 2) - 45)
                        self.jumps_left = 2
                        self.hitbox.y_pos -= 1
                        break

                    self.hitbox.y_pos -= 1

    def check_colision(self, hit2):
        if self.hitbox.colliderect(hit2.hitbox):
            self.hp -= hit2.damage
            return True
        else:
            return False


    def jump(self):
        if self.jumps_left > 0:
            self.velocity_y = self.jump_speed
            self.jumps_left -= 1

    def move(self, cle, briques):

        if cle[pygame.K_q] and cle[pygame.K_d]:
            self.movement_vector = 0


        elif cle[ControlSettings["DROITE"]] and self.hitbox != None:
            self.x += self.velocity
            self.hitbox.x_pos += self.velocity
            if self.hitbox != None and self.hitbox.collide(briques):
                self.x -= self.velocity
                self.hitbox.x_pos -= self.velocity
                self.movement_vector = 0
            else:
                self.x -= self.velocity
                self.hitbox.x_pos -= self.velocity
                if self.x < 960 or self.scroll >= 3000:
                    self.movement_vector = 1
                    self.look = 'RIGHT'
                    self.x += self.velocity
                else:
                    self.look = 'RIGHT'
                    self.scroll += 1
                    self.movement_vector = 1


        elif cle[ControlSettings["GAUCHE"]] and self.hitbox != None:
            self.x -= self.velocity
            self.hitbox.x_pos -= self.velocity
            if self.hitbox != None and self.hitbox.collide(briques):
                self.x += self.velocity
                self.hitbox.x_pos += self.velocity
                self.movement_vector = 0
            else:
                self.x += self.velocity
                self.hitbox.x_pos += self.velocity
                if self.x > 960 or self.scroll <= 0:
                    self.movement_vector = -1
                    self.look = 'LEFT'
                    self.x -= self.velocity

                else:
                    self.look = 'LEFT'
                    self.scroll -= 1
                    self.movement_vector = -1

        else:
            self.movement_vector = 0

    def update(self, screen, briques):
        self.update_animation_state(screen)
        self.check_vertical_collision(briques)

    def draw_ammo(self, screen):
        ammo_text = f"Bullet: {self.main_attack}, Ultimate: {self.ultime_attack}"
        font = pygame.font.SysFont(None, 24)
        text = font.render(ammo_text, True, (255, 255, 255))
        screen.blit(text, (10, 10))


    def debug_mode(self, screen):
        x, y = pygame.mouse.get_pos()
        co_text = f"X: {self.x}, Y: {self.y}"
        vec_text = f"Vector X: {self.movement_vector}, Vector Y: {self.velocity_y}"
        scroll_text = f"Scroll: {self.scroll}"
        mouse_text = f"Souris X: {x}, Souris Y: {y}"
        jump_text = f"Jump: {self.jumps_left}"
        font = pygame.font.SysFont(None, 24)

        text_1 = font.render(co_text, True, (255, 255, 255))
        text_2 = font.render(vec_text, True, (255, 255, 255))
        text_3 = font.render(scroll_text, True, (255, 255, 255))
        text_4 = font.render(mouse_text, True, (255, 255, 255))
        text_5 = font.render(jump_text, True, (255, 255, 255))

        screen.blit(text_1, (10, 60))
        screen.blit(text_2, (10, 84))
        screen.blit(text_3, (10, 108))
        screen.blit(text_4, (10, 132))
        screen.blit(text_5, (10, 156))


    def draw(self, screen):
        img_width, img_height = self.image.get_width(), self.image.get_height()
        img_x, img_y = self.x - img_width // 2, self.y - img_height // 2

        image_to_draw = pygame.transform.flip(self.image, True, False) if self.look == 'LEFT' else self.image
        screen.blit(image_to_draw, (img_x, img_y))
        self.animate()

        '''check_colision = pygame.Rect(self.x- 150 , self.y- 150, 300, 300)
        rectsurf = pygame.Surface(check_colision.size, pygame.SRCALPHA)
        rectsurf.fill((255, 100, 0, 100))
        screen.blit(rectsurf, check_colision.topleft)'''

    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)


    def get_scroll(self):
        print(self.scroll)
        return self.scroll
