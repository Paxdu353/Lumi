import pygame


class Background:

    def __init__(self, name):
        self.name = name
        self.background = [pygame.image.load(f'images/{name}/{img}.png').convert_alpha() for img in range(1, 8)]
        self.width_background = self.background[0].get_width()
        self.loop = 5
        self.increment_speed = 0.4

    def draw_bg(self, screen, scroll):
        for x in range(self.loop):
            speed = 1.3
            for i in self.background:
                if scroll > 0:
                    screen.blit(i, ((x * self.width_background) - scroll * speed, 0))
                else:
                    screen.blit(i, ((x * self.width_background) * speed, 0))
                speed += self.increment_speed


