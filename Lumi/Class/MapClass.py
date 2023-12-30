import pygame
import Lumi.Class.BackgroundClass as BAC
import Lumi.Class.BriqueClass as BRC
class Map:
    def __init__(self, screen, background_name):
        self.screen = screen
        self.briques = []
        self.background = BAC.Background(background_name)
        self.grid_offset_x = 0
        self.sroll_tile = {
            '0': (255, 0, 0),
            '1':  (255, 255, 0),
            '2': (255, 255, 255),
            '3': (0, 0, 255)
        }
        self.current_scroll = 0


    def add_brique(self, x_pos, y_pos, width, height, color=(255, 255, 255)):
        nouvelle_brique = BRC.Brique(x_pos, y_pos, width, height, self.screen, color)
        self.briques.append(nouvelle_brique)

    def update(self, player_velocity, player_movement_vector):
        self.grid_offset_x += player_velocity * -player_movement_vector

    def TiledMap(self, screen, size):
        for line in range(size):
            pygame.draw.line(screen, (255, 255, 255), (line * 64 + self.grid_offset_x, 0), (line * 64 + self.grid_offset_x, 1080))
            pygame.draw.line(screen, (255, 255, 255), (0, line * 64), (size * 64 + self.grid_offset_x, line * 64))


    def DrawModeText(self, screen):
        mode_text = f'Mode draw activé'
        font = pygame.font.SysFont(None, 24)
        text = font.render(mode_text, True, (255, 255, 255))
        screen.blit(text, (10, 25))

    def scroll_tile(self, next_index):
        if next_index == -1 and self.current_scroll == 0:
            return self.sroll_tile[0]
        else:
            return self.sroll_tile[self.current_scroll + next_index]



    def DrawMode(self, screen, size, mouvement_vector, velocity):
        self.TiledMap(screen, size)
        self.DrawModeText(screen)


    def DrawRect(self, screen):
        x, y = pygame.mouse.get_pos()
        x = (x-self.grid_offset_x)//64
        y = y//64
        brique = BRC.Brique(x*64 + self.grid_offset_x, y*64, 64, 64, screen)
        if brique not in self.briques:
            self.briques.append(brique)

    def RemoveRect(self):
        x, y = pygame.mouse.get_pos()
        for brique in self.briques:
            if brique.collidepoint(x, y):
                self.briques.remove(brique)


    def draw(self, scroll):
        self.background.draw_bg(self.screen, scroll)
        for brique in self.briques:
            brique.draw(self.screen)

