import pygame
import Lumi.Class.BackgroundClass as BAC
import Lumi.Class.BriqueClass as BRC
class Map:
    def __init__(self, screen, background_name):
        self.TMN = [
            [],
            [],
            []
        ]

        self.TMR = []
        self.screen = screen
        self.briques = []
        self.background = BAC.Background(background_name)


    def add_brique(self, x_pos, y_pos, width, height, color=(255, 255, 255)):
        nouvelle_brique = BRC.Brique(x_pos, y_pos, width, height, self.screen, color)
        self.briques.append(nouvelle_brique)

    def update(self):
        pass


    def TiledMap(self, screen, size):
        increment = 1
        for line in range(size):
            pygame.draw.line(screen, (255, 255, 255), (increment * 64, 0), (increment * 64, 1080))
            pygame.draw.line(screen, (255, 255, 255), (0, increment*64), (size*64, increment*64))
            increment += 1

    def draw(self, scroll):
        self.background.draw_bg(self.screen, scroll)
        for brique in self.briques:
            brique.draw(self.screen)

