import pygame

touches_fr = {
    "space": "espace",
    "left": "gauche",
    "right": "droite",
    "up": "haut",
    "down": "bas",
}

ControlSettings = {
    "SAUTER": pygame.K_SPACE,
    "DROITE": pygame.K_d,
    "GAUCHE": pygame.K_q,
    "ULTIME": pygame.K_s

}


def valeur_control(cle):
    sup = pygame.key.name(ControlSettings[cle])
    if sup in touches_fr.keys():
        return touches_fr[sup].upper()
    else:
        return sup.upper()

