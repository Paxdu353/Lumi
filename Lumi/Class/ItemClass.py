import pygame

class Item:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.type = item_type  # 'main' ou 'ultimate'
        self.width = 30
        self.height = 30
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            if self.type == "main":
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def check_collision(self, player):
        if (player.x < self.x + self.width and player.x + player.width > self.x and
            player.y < self.y + self.height and player.y + player.height > self.y):
            return True
        return False

    def collect(self, player):
        if self.type == 'main':
            player.main_attack += 1
        elif self.type == 'ultimate':
            player.ultime_attack += 1
        self.collected = True
