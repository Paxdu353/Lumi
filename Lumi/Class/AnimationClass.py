import pygame
import os


class AnimationSprite(pygame.sprite.Sprite):

    def __init__(self, target, movement):
        super().__init__()
        self.target = target
        self.movement = movement
        self.current_image = 0
        self.animation_delay = 75
        self.last_update_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(pygame.image.load(f"images/Player/Idle/Idle_1.png"), (240, 190))
        self.box_collision = self.image.get_rect()
        self.images_list = animations.get(target).get(movement)

    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_delay:
            self.current_image += 1
            if self.current_image >= len(self.images_list):
                self.current_image = 0

            self.image = self.images_list[self.current_image]
            self.last_update_time = current_time


def load_animation(target, movement):
    images = []
    chemin = f"images/{target}/{movement}/"
    nbr_fichier = 0

    for nom_fichier in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, nom_fichier)
        if os.path.isfile(chemin_complet):
            nbr_fichier += 1

    for img in range(1, nbr_fichier):
        image = chemin + f"{movement}_{img}.png"
        images.append(pygame.transform.scale(pygame.image.load(image), (250, 200)))

    return images


animations = {
    'Player': {
        'Idle': load_animation('Player', 'Idle'),
        'Walk': load_animation('Player', 'Walk'),
        'Attack': load_animation('Player', 'Attack'),
    },

    'Enemy': {
        'Idle': load_animation('Enemy', 'Idle'),
        'Walk': load_animation('Enemy', 'Walk'),
        'Attack': load_animation('Enemy', 'Attack'),
        'Dying': load_animation('Enemy', 'Dying'),
    }

}
