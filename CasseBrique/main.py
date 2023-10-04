import pygame
import CasseBrique.BriqueClass as BC
import CasseBrique.PlayerClass as PC
pygame.init()
width, height = 600, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CasseBrique")

brique = BC.Brique(50,50 ,25,75 , (255, 255, 255))
map = [brique.rect]
objet_player = pygame.Rect(width//2, height -15, 50, 10)
player = PC.Player(objet_player, (255, 255, 255))
balle = balle = pygame.Rect(width//2-10,50,10,10)
velocity = [2, 3]

while True:
    mouse = (pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.aller(mouse)

    for i in map:
        if balle.colliderect(i):
            velocity[1] = -velocity[1]


    if balle.right > width or balle.left < 0:
        velocity[0] = -velocity[0]

    if balle.top < 0:
        velocity[1] = -velocity[1]

    if balle.colliderect(objet_player):
        velocity[1] = -velocity[1]

    balle.x += velocity[0]
    balle.y += velocity[1]


    brique.draw(screen)
    player.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), balle)
    pygame.display.flip()
    screen.fill((0, 0, 0))

    pygame.time.wait(10)
