import pygame

touches_fr = {
    "space": "espace",
    "left": "gauche",
    "right": "droite",
    "up": "haut",
    "down": "bas",
    "left alt": "alt gauche",
    "return": "entrer",
    "left ctrl": "ctrl gauche",
    "right ctrl": "ctrl droit",
    "right alt": "alt droit",
    "backspace": "effacer",
    "caps lock": "ver maj",
    "left shift": "maj gauche",
    "right shift": "maj droit",
    "enter": "entrer",
    "delete": "suppr",
    "left meta": "win",

}

ControlSettings = {
    "SAUTER": pygame.K_SPACE,
    "DROITE": pygame.K_d,
    "GAUCHE": pygame.K_q,
    "ULTIME": pygame.K_s

}


def valeur_control(cle):
    sup = pygame.key.name(ControlSettings[cle]) if cle in ControlSettings.keys() else ''

    if sup in touches_fr.keys():
        return touches_fr[sup].upper()
    else:
        return sup.upper()

