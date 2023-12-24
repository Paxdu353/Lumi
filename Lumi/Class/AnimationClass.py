import pygame

class AnimationSprite(pygame.sprite.Sprite):

    def __init__(self, target, movement):
        super().__init__()
        self.target = target
        self.movement = movement
        self.current_image = 0
        self.image = ''
        self.images = animations.get(target)

    def animate(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0

        self.image = self.images[self.current_image]



def load_animation(target, movement):
    images = []
    chemin = f"images/{target}/{movement}/"

    for img in range(1, 12):
        image = chemin + f"Idle_{img}.png"
        images.append(pygame.image.load(image))

    return images


animations = {
    'Player': load_animation('Player', 'Idle')
}