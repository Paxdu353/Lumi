import pygame
import RaquetteClass
import random

pygame.init()

width, height = 320, 240
black = (0, 0, 0)
white= (255, 255, 255)
red = (255, 0, 0)

starter = random.randint(0, 1)
Nbr = 0
Nbr2 = 0

balle = pygame.Rect(width//2-10,50,10,10)
r1 = RaquetteClass.Raquette(pygame.Rect(10,100,5,50), white, True)
r2 = RaquetteClass.Raquette(pygame.Rect(310, 100, 5, 50), white, False)

screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("Pong")
font = pygame.font.SysFont("None", 16)

if bool(starter) == r1.player:
    vitesse = [-2, 1]

else:
    vitesse = [2, 1]

start = 0




while True:
    text = font.render(f"{Nbr2} passes", True, white)
    text2 = font.render(f"Le joueur {starter+1} commence", True, white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    r1.move()
    r2.move()

    if r1.rect.colliderect(balle) or r2.rect.colliderect(balle):
        vitesse[0] = -vitesse[0]
        Nbr += 1
        Nbr2 += 1


    if balle.right > width or balle.left < 0:
        pygame.quit()
        exit()

    if balle.bottom > height or balle.top < 0:
        vitesse[1] = -vitesse[1]
    if pygame.key.get_pressed()[pygame.K_SPACE] or start == 1:
        balle.x += vitesse[0]
        balle.y += vitesse[1]
        start = 1

    if Nbr // 5 == 1:
        if vitesse[0] < 0:
            vitesse[0] -= 1

        else:
            vitesse[0] += 1

        Nbr = 0


    screen.fill(black)
    pygame.draw.rect(screen, red, balle)
    r1.draw(screen)
    r2.draw(screen)
    screen.blit(text, ((width//2)-30, 20))
    if start == 0: screen.blit(text2, (width // 2 - 60, 30))

    pygame.display.flip()

    pygame.time.wait(10)

