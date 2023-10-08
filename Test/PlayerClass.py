import pygame


class Player:


    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


    def moove(self):
        if pygame.key.get_pressed()[pygame.K_z]:
            self.y -= 1

        if pygame.key.get_pressed()[pygame.K_s]:
            self.y += 1

        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += 1

        if pygame.key.get_pressed()[pygame.K_q]:
            self.x -= 1

        print(pygame.mouse.get_rel())

    def vision(self, screen):
        mouse_x = pygame.mouse.get_rel()[0]
        pygame.draw.line(screen, (0, 255, 255), (self.x, self.y), (self.x , self.y+100))

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 5)

