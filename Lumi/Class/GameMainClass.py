import pygame

import Lumi.Class.MapClass as MC
import Lumi.Class.PlayerClass as PC
import Lumi.Class.ProjectileClass as PCP
import Lumi.Class.BriqueClass as BC

pygame.init()



class Main:

    def __init__(self, width=1920, height=1080, name="Lumi", fps=60):
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.__name = name
        self.fps = fps
        self.speed_map = 3
        self.__screen = pygame.display.set_mode((self.width, self.height))
        self.__player = PC.Player(self.width / 2, height - 118)
        self.projectiles = []
        self.ulti = []
        self.items = []
        self.DrawMode = False
        self.MainMenu = True
        self.SettingsMenu = False
        self.map = MC.Map(self.__screen, 'Background_1')
        self.Menu = pygame.transform.scale(pygame.image.load(f'images/Gui/MainMenu/Background/img.png').convert_alpha(), (1920, 1080))
        self.sound = pygame.mixer.Sound(f'images/main.mp3')

        pygame.display.set_caption(self.__name)



    def DrawGui(self):

        play_button = BC.Brique(670, 590, 250, 90, self.__screen)
        quit_button = BC.Brique(805, 740, 320, 80, self.__screen)
        reglage_button = BC.Brique(1010, 590, 375, 90, self.__screen)


        if self.sound.get_num_channels() == 0:
            self.sound.set_volume(0.1)
            self.sound.play()


        blackanim = pygame.Rect(0, 0, 1920, 1080)
        rectsurf = pygame.Surface(blackanim.size, pygame.SRCALPHA)
        rectsurf.fill((255, 100, 0, 0))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if not self.SettingsMenu:
                        if play_button.collidepoint(x, y):
                            self.MainMenu = False
                            self.sound.stop()

                        elif quit_button.collidepoint(x, y):
                            pygame.quit()
                            exit()

                        elif reglage_button.collidepoint(x, y):
                            self.SettingsMenu = True

                    else:
                        pass



        self.__screen.blit(self.Menu, (0, 0))

        if not self.SettingsMenu:
            name_text = f"LUMI"
            play_text = f"JOUER - REGLAGE"
            quit_text = f"QUITTER"
            font = pygame.font.Font("images/font.ttf", 100)
            font2 = pygame.font.Font("images/font.ttf", 50)
            font3 = pygame.font.Font("images/font.ttf", 250)

            text0 = font3.render(name_text, True, (184, 7, 75))
            text1 = font.render(play_text, True, (184, 7, 75))
            text2 = font.render(quit_text, True, (184, 7, 75))



            self.__screen.blit(text0, (700, 0))
            self.__screen.blit(text1, (665, 550))
            self.__screen.blit(text2, (800, 700))
            self.__screen.blit(rectsurf, blackanim)
            #pygame.draw.rect(self.__screen, (255, 255, 255), play_button)
            #pygame.draw.rect(self.__screen, (255, 255, 255), quit_button)
            #pygame.draw.rect(self.__screen, (255, 255, 255), reglage_button)


        else:
            retour_text = f"RETOUR"
            font2 = pygame.font.Font("images/font.ttf", 50)
            text2 = font2.render(retour_text, True, (184, 7, 75))
            self.__screen.blit(text2, (700, 500))
            pygame.draw.rect(self.__screen, (255, 255, 255), text2.get_rect())

        pygame.display.update()


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
                            self.ulti.append(PCP.Projectile(self.__player.x, self.__player.y, angle, 7 - i))

                elif event.key == pygame.K_k:
                    if self.DrawMode == True:
                        self.DrawMode = False
                    else:
                        self.DrawMode = True

                elif event.key == pygame.K_j:
                    with open('Level/briques_list.txt', 'w') as file:
                        file.write(str(self.map.briques))


                elif event.key == pygame.K_x and self.DrawMode:
                    self.map.briques = []


                elif event.key == pygame.K_ESCAPE:
                    self.MainMenu = True



            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.DrawMode:
                        self.map.DrawRect(self.__screen)

                    elif len(self.projectiles) == 0 and len(self.ulti) == 0 and self.__player.main_attack > 0:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        angle = self.__player.get_angle(self.__player.x, self.__player.y, mouse_x, mouse_y)
                        self.projectiles.append(PCP.Projectile(self.__player.x, self.__player.y, angle))
                        self.__player.main_attack -= 1
                        self.__player.is_attack = True
                        self.__player.current_image = 0

                elif event.button == 3:
                    if self.DrawMode:
                        self.map.RemoveRect()

                elif event.button == 4:
                    if self.DrawMode:
                        self.map.scroll_tile(1)

                elif event.button == 5:
                    if self.DrawMode:
                        self.map.scroll_tile(-1)

        if len(self.items) != 0:
            for item in self.items:
                if item.check_collision(self.__player) and not item.collected:
                    item.collect(self.__player)

        cle = pygame.key.get_pressed()

        self.map.get_check_collision(self.__player.x, self.__player.y)

        self.__player.move(cle, self.map.active_briques)

    def update_display(self):
        self.__player.update(self.__screen, self.map.active_briques)

        for projectile in self.projectiles + self.ulti:
            projectile.move()
            projectile.update(self.__screen)
            projectile.DrawMainAttack(self.__screen)
            self.map.get_check_collision(projectile.x, projectile.y)
            if projectile.x < 0 or projectile.x > self.width or projectile.y < 0 or projectile.y > self.height:
                if projectile in self.projectiles:
                    self.projectiles.remove(projectile)
                else:
                    self.ulti.remove(projectile)

            else:
                for brique in self.map.active_briques:
                    if projectile.hitbox.colliderect(brique):
                        if projectile in self.projectiles:
                            self.projectiles.remove(projectile)
                            break
                        else:
                            self.ulti.remove(projectile)
                            break


        if self.__player.movement_vector != 0:
            for brique in self.map.briques:
                if self.__player.scroll > 0:
                    brique.relocate(brique.x_pos - self.speed_map * self.__player.movement_vector, brique.y_pos)

    def draw(self):
        if self.DrawMode:
            number_of_cells = self.map.background.loop * self.map.background.width_background // 64
            self.map.DrawMode(self.__screen, number_of_cells)
            self.map.DrawScrollText(self.__screen)

        self.map.update(self.__player.movement_vector, self.speed_map, self.__player.scroll)
        #pygame.draw.rect(self.__screen, (255, 255, 255), self.__player.hitbox)
        self.__player.draw(self.__screen)
        for item in self.items:
            item.draw(self.__screen)
        self.__player.draw_ammo(self.__screen)
        self.__player.debug_mode(self.__screen)

        pygame.display.flip()


    def run(self):
        while True:
            if self.MainMenu:
                self.DrawGui()
            else:
                self.main_events()
                self.update_display()
                self.draw()

            self.clock.tick(self.fps)