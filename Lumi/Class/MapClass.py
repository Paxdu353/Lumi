import pygame
import pickle

import Lumi.Class.BackgroundClass as BAC
import Lumi.Class.BriqueClass as BRC
import Lumi.Class.AnimationClass as AC




class Map():
    def __init__(self, screen, background_name):
        self.screen = screen
        self.briques = []
        self.liste_briques = []
        with open("Level/briques_list.txt", "r") as f1:
            for line in f1.readlines():
                self.liste_briques.append([int(c) for c in line.split(",")])


        self.active_briques = []
        self.background = BAC.Background(background_name)
        self.grid_offset_x = 0
        self.tile_list = {x: pygame.image.load(f"images/Tiles/Tile_{x}.png").convert_alpha() for x in range(1, 37)}
        self.spawn = False
        self.current_scroll = 1
        self.scroll_player = 0
        self.colision = True



        for brique in self.liste_briques:
            self.add_brique(brique[0], brique[1], brique[2], brique[3], self.tile_list[brique[4]], brique[4], 0, brique[5])
        print(self.briques)


    def DrawMode(self, screen, size):
        self.TiledMap(screen, size)
        self.DrawModeText(screen)

    def add_brique(self, x_pos, y_pos, width, height, img, index, scroll, colision):
        nouvelle_brique = BRC.Brique(x_pos, y_pos, width, height, self.screen, img, index, scroll, colision)

        self.briques.append(nouvelle_brique)

    def update(self, player_velocity, player_movement_vector, bg_scroll):

        if bg_scroll > 0:
            self.grid_offset_x += player_velocity * -player_movement_vector

    def TiledMap(self, screen, size):
        for line in range(size):
            pygame.draw.line(screen, (255, 255, 255), (line * 64 + self.grid_offset_x, 0),
                             (line * 64 + self.grid_offset_x, 1080))
            pygame.draw.line(screen, (255, 255, 255), (0, line * 64), (size * 64 + self.grid_offset_x, line * 64))



    def scroll_tile(self, next_index):
        if next_index == -1 and self.current_scroll == 1:
            self.current_scroll = len(self.tile_list)

        elif self.current_scroll == len(self.tile_list) and next_index == 1:
            self.current_scroll = 1

        else:
            self.current_scroll = self.current_scroll + next_index

    def RemoveRect(self):
        x, y = pygame.mouse.get_pos()
        for brique in self.briques:
            if brique.collidepoint(x, y):
                self.briques.remove(brique)

    def update_anim(self):
        self.animation_delay = 10
        self.animate()

    def RemoveAllRect(self):
        self.briques = []

    def draw_bg(self, scroll):
        self.background.draw_bg(self.screen, scroll)

    def draw_rect(self):
        for brique in self.briques:
            brique.draw(self.screen)

    def get_check_collision(self, x_pos, y_pos):
        liste = []
        for brique in self.briques:
            if brique.has_colision:
                if x_pos - 215 <= brique.x_pos <= x_pos + 150 and y_pos - 215 <= brique.y_pos <= y_pos + 150:
                    liste.append(brique)
                    brique.check_col = True
        self.active_briques = liste

    def DrawRect(self, screen):
        x, y = pygame.mouse.get_pos()
        x = (x - self.grid_offset_x) // 64
        y = y // 64
        brique = BRC.Brique(x * 64 + self.grid_offset_x, y * 64, 64, 64, screen, self.tile_list[self.current_scroll], self.current_scroll, self.grid_offset_x)
        if brique not in self.briques:
            if not self.colision:
                brique.has_colision = False
            self.briques.append(brique)

    def DrawModeText(self, screen):
        mode_text = f'Mode draw activé'
        scroll_souris = f"{self.current_scroll}:"
        colision = f"Colision: {self.colision}"
        font = pygame.font.SysFont(None, 24)
        text = font.render(mode_text, True, (255, 255, 255))
        text2 = font.render(scroll_souris, True, (255, 255, 255))
        text3 = font.render(colision, True, (255, 255, 255))
        screen.blit(text, (1700, 25))
        screen.blit(text3, (1700, 45))
        screen.blit(text2, (1700, 85))

    def DrawScrollText(self, screen):
        screen.blit(pygame.transform.scale(pygame.image.load(f"images/Tiles/Tile_{self.current_scroll}.png"), (50, 50)), (1725, 70))


