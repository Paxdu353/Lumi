import pygame
import CasseBrique.BriqueClass as BC
import CasseBrique.PlayerClass as PC
import math


pygame.init()

width, height = 600, 600
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CasseBrique")


def get_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)


objet_player = pygame.Rect(width//2, height -15, 100, 10)
player = PC.Player(objet_player, (255, 255, 255))
balle = pygame.Rect(width//2-10,200,10,10)
velocity = [2, 3]

Map = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0]
]

map = []
for (i, line) in enumerate(Map):
    for (j, cell) in enumerate(line):
        x, y = j * (width // len(line)), i * 30
        brique = BC.Brique(x, y, width // len(line) - 5, 25, screen, cell)
        if brique.type == 1:
            map.append(brique)

while True:
    mouse = (pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.aller(mouse)

    for (i, rect) in enumerate(map):
        if balle.colliderect(rect.rect):
            velocity[1] = -velocity[1]
            map.pop(i)


    if balle.right > width or balle.left < 0:
        velocity[0] = -velocity[0]

    if balle.top < 0:
        velocity[1] = -velocity[1]

    if balle.bottom > height:
        exit()

    if balle.colliderect(objet_player):
        velocity[1] = -velocity[1]
        if balle.centerx < objet_player.centerx - 20:
            velocity[0] = -abs(velocity[0])
        elif balle.centerx > objet_player.centerx + 20:
            velocity[0] = abs(velocity[0])


    balle.x += velocity[0]
    balle.y += velocity[1]

    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), balle)
    for i in map:
        if i.type == 1:
            i.draw()
    pygame.display.flip()

    pygame.time.wait(10)
