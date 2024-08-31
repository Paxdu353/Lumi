import math
import pygame
import Class.AnimationClass as AC
import Class.BriqueClass as BC
import Class.ProjectileClass as PC
from settings import *


class Enemy(AC.AnimationSprite):
    def __init__(self, scroll_x=0, vec_player = 0, x_pos=6048, y_pos=610, attack_power=5, patrol_points=[[5696, 610], [6400, 610]], width=32,
                 height=32):
        super().__init__("Enemy", "Idle")
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.attack_power = attack_power
        self.patrol_points = patrol_points
        self.current_patrol_point = 0
        self.velocity = 2
        self.movement_vector = 0
        self.hp = 10
        self.scroll_x = scroll_x
        self.vector_player = vec_player
        self.original_img = self.image
        self.look = 'LEFT'
        self.hitbox = None
        self.dead = False
        self.already_dead = False
        self.last_shot_time = pygame.time.get_ticks()
        self.shot_interval = 1000
        self.point = None

    def patrol(self):
        target_x, target_y = self.patrol_points[self.current_patrol_point]
        if self.hp > 0:
            self.point = pygame.Rect(target_x, target_y, self.width, self.height)


            if self.x < target_x:
                self.x += self.velocity
                self.movement_vector = 1
                self.look = 'RIGHT'

            elif self.x > target_x:
                self.movement_vector = -1
                self.x -= self.velocity
                self.look = 'LEFT'

            if math.hypot(target_x - self.x, target_y - self.y) < 5:
                self.current_patrol_point = (self.current_patrol_point + 1) % len(self.patrol_points)
        else:
            self.movement_vector = 0

    def shoot(self, projectiles_list, player_x, player_y):
        if self.already_dead:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shot_interval:
            angle = self.get_angle(self.x, self.y, player_x, player_y)
            projectile = PC.Projectile(self.x + 50, self.y + 75, angle, image_path=f'images/Enemy/Attack.png')
            projectiles_list.append(projectile)
            self.last_shot_time = current_time

    def update(self, screen, player, projectiles_list, player_x, player_y):
        self.patrol()
        self.update_animation_state(screen)
        self.attack_if_close(player, projectiles_list, player_x, player_y)
        self.text(screen)

        if self.scroll_x > 0:
            self.x += 5 * -self.vector_player
            self.hitbox.x_pos -= 5 * -self.vector_player

            for co in self.patrol_points:
                co[0] += 5 * -self.vector_player

    def check_colision(self, hit2):
        if self.hitbox.colliderect(hit2.hitbox):
            self.hp -= hit2.damage
            return True
        else:
            return False

    def text(self, screen):
        mode_text = f'{self.scroll_x}'
        font = pygame.font.SysFont(None, 24)
        text = font.render(mode_text, True, (255, 255, 255))
        screen.blit(text, (950, 25))

    def update_animation_state(self, screen):
        if self.already_dead:
            return

        if self.movement_vector != 0:
            self.images_list = AC.animations['Enemy']['Walk']

        elif self.hp <= 0:
            self.images_list = AC.animations['Enemy']['Dying']
            if self.current_image >= len(self.images_list) - 1:
                self.already_dead = True

        self.hitbox = BC.Brique(self.x + 75, self.y, (self.image.get_width() // 2) - 30,
                                (self.image.get_height() // 2) + 50, screen,
                                pygame.image.load("images/Tiles/Tile_2.png"), 1, 0)

    def attack_if_close(self, player, projectiles_list, player_x, player_y):
        if self.already_dead:
            return

        if math.hypot(player.x - self.x, player.y - self.y) < 500:
            self.images_list = AC.animations['Enemy']['Attack']
            self.shoot(projectiles_list, player_x, player_y)


    def draw(self, screen):
        img_width, img_height = self.image.get_width(), self.image.get_height()
        image_to_draw = pygame.transform.flip(self.image, True, False) if self.look == 'LEFT' else self.image
        screen.blit(image_to_draw, (self.x, self.y))

        self.animate()

    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)
