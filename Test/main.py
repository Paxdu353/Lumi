import pygame
import PlayerClass as PC
from Constants import *
pygame.init()

screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Racasting")
player = PC.Player(250, 250)




Map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

map = []

for (i, line) in enumerate(Map):
    for (j, line) in enumerate(line):
        if line == 1:
            x, y = j * 50, i * 50
            brique = pygame.Rect(x, y, 50, 50)
            map.append(brique)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    player.moove()




    screen.fill(black)

    for i in map:
        pygame.draw.rect(screen, white, i)

    player.draw(screen)
    player.vision(screen)
    pygame.display.flip()
    pygame.time.wait(10)
