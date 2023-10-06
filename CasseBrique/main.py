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
balle = balle = pygame.Rect(width//2-10,50,10,10)
velocity = [2, 3]

Map = [
    [1, 1, 1],
    [1, 1, 1],
    [0, 1, 0]
]

map = []
for (i, line) in enumerate(Map):
    for (j, cell) in enumerate(line):
        x,y = j*(75+5), i*(25+5)
        brique = BC.Brique(x+10, y+10, 25, 75, white, screen, cell)
        map.append(brique)

while True:
    mouse = (pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.aller(mouse)

    for i in map:
        if balle.colliderect(i.rect):
            map.remove(i)


    if balle.right > width or balle.left < 0:
        velocity[0] = -velocity[0]

    if balle.top < 0:
        velocity[1] = -velocity[1]

    if balle.colliderect(objet_player):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = get_angle(mouse_x, mouse_y,balle.x, balle.y)
        print(math.sin(angle))
        velocity[1] = -velocity[1] * math.sin(angle)
        velocity[0] *= math.cos(angle)

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
