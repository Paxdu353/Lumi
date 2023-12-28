import pygame
import Lumi.Class.PlayerClass as PC
import Lumi.Class.ProjectileClass as PCP
import Lumi.Class.ItemClass as IC
import Lumi.Class.MapClass as MC


pygame.init()


class Main:

    def __init__(self, width=1920, height=1080, name="Lumi", fps=60):
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.__name = name
        self.fps = fps
        self.__screen = pygame.display.set_mode((self.width, self.height))
        self.__player = PC.Player(self.width/2, height - 118)
        self.projectiles = []
        self.ulti = []
        self.items = []
        self.map = MC.Map(self.__screen, 'Background_1')
        self.map.add_brique(800, 500, 100, 100, (255, 255, 0))
        pygame.display.set_caption(self.__name)

    def main_events(self):
        self.map.draw(self.__player.scroll)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__player.jump()

                elif event.key == pygame.K_s:
                    if len(self.ulti) == 0 and len(self.projectiles) == 0 and self.__player.ultime_attack > 0:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        angle = self.__player.get_angle(self.__player.x, self.__player.y, mouse_x, mouse_y)
                        self.__player.ultime_attack -= 1
                        self.__player.is_attack = True
                        self.__player.current_image = 0
                        for i in range(3):
                            self.ulti.append(PCP.Projectile(self.__player.x, self.__player.y, angle, 7-i))

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(self.projectiles) == 0 and len(self.ulti) == 0 and self.__player.main_attack > 0:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        angle = self.__player.get_angle(self.__player.x, self.__player.y, mouse_x, mouse_y)
                        self.projectiles.append(PCP.Projectile(self.__player.x, self.__player.y, angle))
                        self.__player.main_attack -= 1
                        self.__player.is_attack = True
                        self.__player.current_image = 0

        if len(self.items) != 0:
            for item in self.items:
                if item.check_collision(self.__player) and not item.collected:
                    item.collect(self.__player)

        cle = pygame.key.get_pressed()
        self.__player.move(cle)

    def update_display(self):

        self.__player.update()
        for projectile in self.projectiles + self.ulti:
            projectile.move()
            projectile.DrawMainAttack(self.__screen)
            if projectile.x < 0 or projectile.x > self.width or projectile.y < 0 or projectile.y > self.height:
                if projectile in self.projectiles:
                    self.projectiles.remove(projectile)
                else:
                    self.ulti.remove(projectile)

        if self.__player.movement_vector != 0:
            for brique in self.map.briques:
                brique.relocate(brique.x_pos + (self.__player.velocity * -self.__player.movement_vector), brique.y_pos)
                print(brique.x_pos, brique.y_pos)





    def draw(self):
        self.__player.draw(self.__screen)
        for item in self.items:
            item.draw(self.__screen)
        self.__player.draw_ammo(self.__screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.main_events()
            self.update_display()
            self.draw()
            self.clock.tick(self.fps)


