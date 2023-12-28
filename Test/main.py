import pygame
import PlayerClass as PC
from Constants import *

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE, pygame.FULLSCREEN)
pygame.display.set_caption("Racasting")




Map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

map = []

player = PC.Player(250, 250, screen, map)

clock = pygame.time.Clock()

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



    screen.fill(BLACK)

    for i in map:
        pygame.draw.rect(screen, WHITE, i)

    player.draw(screen)





    player.vision(screen)
    pygame.display.flip()
    pygame.time.wait(10)

    clock.tick(60)

    fps = clock.get_fps()
    pygame.display.set_caption(f"Racasting - FPS: {fps:.2f}")

