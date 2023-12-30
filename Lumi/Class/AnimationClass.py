import pygame


class AnimationSprite(pygame.sprite.Sprite):

    def __init__(self, target, movement):
        super().__init__()
        self.target = target
        self.movement = movement
        self.current_image = 0
        self.animation_delay = 75
        self.last_update_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(pygame.image.load(f"images/Player/Idle/Idle_1.png"), (240, 190))
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

    for img in range(1, 13):
        image = chemin + f"{movement}_{img}.png"
        images.append(pygame.transform.scale(pygame.image.load(image), (250, 200)))

    return images


animations = {
    'Player': {
        'Idle': load_animation('Player', 'Idle'),
        'Walk': load_animation('Player', 'Walk'),
        'Attack': load_animation('Player', 'Attack')
    }
}
