import pygame
class Background:


    def __init__(self, name):
        self.name = name
        self.background = [pygame.image.load(f'images/{name}/{img}.png').convert_alpha() for img in range(1, 8)]
        self.width_background = self.background[0].get_width()
        self.increment_speed = 0.4

    def draw_bg(self,screen,  scroll):
        for x in range(5):
            speed = 1
            for i in self.background:
                screen.blit(i, ((x*self.width_background) - scroll * speed, 0))
                speed += self.increment_speed
    def __repr__(self):
        return f"Background name: {self.name}"