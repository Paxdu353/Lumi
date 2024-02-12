import pygame

import Lumi.Class.MapClass as MC
import Lumi.Class.PlayerClass as PC
import Lumi.Class.ProjectileClass as PCP
import Lumi.Class.BriqueClass as BC
import Lumi.Class.ButtonClass as BUC
from Lumi.settings import *

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
        self.AudioMenu = False
        self.VideoMenu = False
        self.ControlerMenu = False
        self.enter = False
        self.map = MC.Map(self.__screen, 'Background_1')
        self.Menu = pygame.transform.scale(pygame.image.load(f'images/Gui/MainMenu/Background/img.png').convert_alpha(), (1920, 1080))
        self.sound = pygame.mixer.Sound(f'images/main.mp3')

        pygame.display.set_caption(self.__name)



    def DrawGui(self):


        name = BUC.Button(710, 0, 'LUMI', (184, 7, 75), 250)
        jouer = BUC.Button(650, 500, 'JOUER', (184, 7, 75), 100)
        reglage = BUC.Button(1000, 500, 'REGLAGE', (184, 7, 75), 100)
        quitter = BUC.Button(810, 700, 'QUITTER', (184, 7, 75), 100)

        retour = BUC.Button(25, 0, 'RETOUR', (184, 7, 75), 75)
        audio = BUC.Button(500, 0, 'AUDIO', (184, 7, 75), 75)
        controle = BUC.Button(825, 0, 'CONTROLE', (184, 7, 75), 75)
        video = BUC.Button(1275, 0, 'VIDEO', (184, 7, 75), 75)

        jouabilite = BUC.Button(250, 200, 'JOUABILITE:', (184, 7, 75), 100)
        droite = BUC.Button(350, 350, f'DROITE: {valeur_control("DROITE")}', (184, 7, 75), 50)
        gauche = BUC.Button(350, 450, f'GAUCHE: {valeur_control("GAUCHE")}', (184, 7, 75), 50)
        sauter = BUC.Button(350, 550, f'SAUTER: {valeur_control("SAUTER")}', (184, 7, 75), 50)
        special = BUC.Button(350, 650, f'ULTIME: {valeur_control("ULTIME")}', (184, 7, 75), 50)

        construction = BUC.Button(1000, 200, 'CONSTRUCTION:', (184, 7, 75), 100)
        vider= BUC.Button(1150, 350, f'VIDER: {valeur_control("VIDER")}', (184, 7, 75), 50)
        sauvegarder = BUC.Button(1150, 450, f'SAUVEGARDER: {valeur_control("SAUVEGARDER")}', (184, 7, 75), 50)
        mod_contru = BUC.Button(1150, 550, f'CONSTRUCTEUR: {valeur_control("CONSTRUCTEUR")}', (184, 7, 75), 50)

        controle_list = [droite, gauche, sauter, special, vider, sauvegarder, mod_contru]





        if self.sound.get_num_channels() == 0:
            self.sound.set_volume(0.3)
            self.sound.play()


        blackanim = pygame.Rect(0, 0, 1920, 1080)
        rectsurf = pygame.Surface(blackanim.size, pygame.SRCALPHA)

        x, y = pygame.mouse.get_pos()
        jouer.check_colision(x, y)
        reglage.check_colision(x, y)
        quitter.check_colision(x, y)
        retour.check_colision(x, y)
        audio.check_colision(x, y)
        controle.check_colision(x, y)
        video.check_colision(x, y)





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if not self.SettingsMenu:
                        if jouer.rect.collidepoint(x, y):
                            self.MainMenu = False
                            self.enter = True
                            self.sound.stop()
                        elif quitter.rect.collidepoint(x, y):
                            for i in range(0, 255, 2):
                                rectsurf.fill((0, 0, 0, i))
                                self.__screen.blit(rectsurf, (0,0))
                                pygame.time.wait(6)
                                pygame.display.update()
                            pygame.quit()
                            exit()

                        elif reglage.rect.collidepoint(x, y):
                            self.SettingsMenu = True

                    else:
                        if retour.rect.collidepoint(x, y):
                            self.SettingsMenu = False
                            self.ControlerMenu = False
                        elif audio.rect.collidepoint(x, y):
                            self.ControlerMenu = False
                            self.AudioMenu = True
                            self.VideoMenu = False
                        elif controle.rect.collidepoint(x, y):
                            self.ControlerMenu = True
                            self.AudioMenu = False
                            self.VideoMenu = False
                        elif video.rect.collidepoint(x, y):
                            self.ControlerMenu = False
                            self.AudioMenu = False
                            self.VideoMenu = True

                        if self.ControlerMenu:
                            for elem in controle_list:
                                if elem.rect.collidepoint(x, y):
                                    elem.color = (255, 84, 150)
                                    elem.draw_text(self.__screen)
                                    pygame.display.update()
                                    waiting_for_key = True
                                    while waiting_for_key:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                waiting_for_key = False

                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_ESCAPE:
                                                    waiting_for_key = False
                                                    break

                                                elif not event.key in ControlSettings.values():
                                                    control_name = elem.text.split(':')[0].strip()
                                                    ControlSettings[control_name] = event.key
                                                    elem.text = f"{control_name}: {pygame.key.name(event.key)}"
                                                    waiting_for_key = False
                                                    break

        self.__screen.blit(self.Menu, (0, 0))

        if not self.SettingsMenu:
            name.draw_text(self.__screen)
            jouer.draw_text(self.__screen)
            reglage.draw_text(self.__screen)
            quitter.draw_text(self.__screen)

        else:
            audio.draw_text(self.__screen)
            retour.draw_text(self.__screen)
            controle.draw_text(self.__screen)
            video.draw_text(self.__screen)

        if self.enter:
            for i in range(0, 255, 2):
                rectsurf.fill((0, 0, 0, i))
                self.__screen.blit(rectsurf, (0, 0))
                pygame.time.wait(6)
                pygame.display.update()
            self.enter = False

        if self.ControlerMenu:
            gauche.draw_text(self.__screen)
            droite.draw_text(self.__screen)
            sauter.draw_text(self.__screen)
            special.draw_text(self.__screen)
            jouabilite.draw_text(self.__screen)

            construction.draw_text(self.__screen)
            sauvegarder.draw_text(self.__screen)
            vider.draw_text(self.__screen)
            mod_contru.draw_text(self.__screen)



        pygame.display.update()


    def main_events(self):
        self.map.draw(self.__player.scroll)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == ControlSettings['SAUTER']:
                    self.__player.jump()

                elif event.key == ControlSettings['ULTIME']:
                    if len(self.ulti) == 0 and len(self.projectiles) == 0 and self.__player.ultime_attack > 0:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        angle = self.__player.get_angle(self.__player.x, self.__player.y, mouse_x, mouse_y)
                        self.__player.ultime_attack -= 1
                        self.__player.is_attack = True
                        self.__player.current_image = 0
                        for i in range(3):
                            self.ulti.append(PCP.Projectile(self.__player.x, self.__player.y, angle, 7 - i))

                elif event.key == ControlSettings['CONSTRUCTEUR']:
                    if self.DrawMode == True:
                        self.DrawMode = False
                    else:
                        self.DrawMode = True

                elif event.key == ControlSettings['SAUVEGARDER']:
                    with open('Level/briques_list.txt', 'w') as file:
                        file.write(str(self.map.briques))


                elif event.key == ControlSettings['VIDER'] and self.DrawMode:
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