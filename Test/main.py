import pygame
from Constants import *
pygame.init()

screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Racasting")




Map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
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



    screen.fill(black)

    for i in map:
        pygame.draw.rect(screen, white, i)
    pygame.display.flip()

    pygame.time.wait(10)
