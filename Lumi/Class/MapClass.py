import pygame

import Lumi.Class.BackgroundClass as BAC
import Lumi.Class.BriqueClass as BRC


class Map:
    def __init__(self, screen, background_name):
        self.screen = screen
        self.briques = []
        self.background = BAC.Background(background_name)
        self.grid_offset_x = 0
        self.tile_list = {
            1: (255, 0, 0),
            2: (255, 255, 0),
            3: (255, 255, 255),
            4: (0, 0, 255),
            5: (178, 227, 157)
        }
        self.spawn = False
        self.current_scroll = 1


        if len(self.briques) != 0:
            len_rect = 5
            load = self.briques
            self.briques = []
            liste = [load[i:i + len_rect] for i in range(0, len(load), len_rect)]
            for brique in liste:
                self.add_brique(brique[0], brique[1], brique[2], brique[3], brique[4])


    def DrawMode(self, screen, size):
        self.TiledMap(screen, size)
        self.DrawModeText(screen)




    def add_brique(self, x_pos, y_pos, width, height, color=(255, 255, 255)):
        nouvelle_brique = BRC.Brique(x_pos, y_pos, width, height, self.screen, color)
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

    def RemoveAllRect(self):
        self.briques = []



    def draw(self, scroll):
        self.background.draw_bg(self.screen, scroll)
        for brique in self.briques:
            brique.draw(self.screen)

    def DrawRect(self, screen):
        x, y = pygame.mouse.get_pos()
        x = (x - self.grid_offset_x) // 64
        y = y // 64

        brique = BRC.Brique(x * 64 + self.grid_offset_x, y * 64, 64, 64, screen, self.tile_list[self.current_scroll])
        if brique not in self.briques:
            self.briques.append(brique)

    def DrawModeText(self, screen):
        mode_text = f'Mode draw activé'
        font = pygame.font.SysFont(None, 24)
        text = font.render(mode_text, True, (255, 255, 255))
        screen.blit(text, (10, 25))

    def DrawScrollText(self, screen):
        scroll_text = f"COULEUR UTILISER"
        font = pygame.font.SysFont(None, 24)
        text = font.render(scroll_text, True, self.tile_list[self.current_scroll])
        screen.blit(text, (10, 40))
