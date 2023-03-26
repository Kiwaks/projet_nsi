import pygame
import button
from random import *
from car import Car
from car_obstacle import Car_obstacle
from event_car import Event_car
from barrage import Barrage
from event_barrage import Event_barrage
from event_barrage2 import Event_barrage2
from barrage_2 import Barrage2

class Game:
    def __init__(self):
        self.car = Car(self)
        self.car_obstacle = Car_obstacle(self)
        self.event_car = Event_car(self)
        self.event_barrage = Event_barrage(self)
        self.event_barrage2 = Event_barrage2(self)
        self.all_cars = self.event_car.all_cars
        self.all_barrages = self.event_barrage.all_cars
        self.all_barrages2 = self.event_barrage2.all_cars
        self.barrage = Barrage(self)
        self.barrage2 = Barrage2(self)
        self.pressed = {}
        self.score = 0
        self.percent = 0
        self.is_starting = 0
        self.font = pygame.font.SysFont('Calibri', 36)
        self.game_over_font = pygame.font.Font('Pixolletta8px.ttf', 100)
        self.white = (255,255,255)
        self.rouge = (255,0,0)
        self.pause = False
        self.aleatoire = choice([1,2])
        self.can_spawning_bar = False
        self.can_spawning_bar2 = False
        self.btn1 = pygame.image.load('../projet_nsi/assets/plus.png').convert_alpha()
        self.btn2 = pygame.image.load('../projet_nsi/assets/plus2.png').convert_alpha()

    def update(self, screen):
        """
        screen : variale pour l'écran du jeu
        Fonction "boucle du jeu" 
        """
        if self.pause == False:
            barrage_changement_bizzare = True      

            if barrage_changement_bizzare == True:
                self.barrage.is_active = False
                barrage_changement_bizzare = False

            screen.blit(self.car.image, self.car.rect)
            self.car.collisions_with_obstacles()

            if self.car.hearts >= 3:
                screen.blit(self.car.hearts_image, (8, 8))
                screen.blit(self.car.hearts_image, (8, 116))
                screen.blit(self.car.hearts_image, (8, 224))
            if self.car.hearts == 2:
                screen.blit(self.car.hearts_image, (8, 8))
                screen.blit(self.car.hearts_image, (8, 116))
            if self.car.hearts == 1:
                screen.blit(self.car.hearts_image, (8, 8))

            if self.car.hearts <= 0:
                self.is_starting = 10
                
            if (self.pressed.get(pygame.K_d) or self.pressed.get(pygame.K_RIGHT)) and self.car.rect.x + self.car.rect.width < screen.get_width() - 116:
                self.car.move_right()
            elif (self.pressed.get(pygame.K_q) or self.pressed.get(pygame.K_LEFT)) and self.car.rect.x > 0.0 + 116:
                self.car.move_left()
            elif (self.pressed.get(pygame.K_z) or self.pressed.get(pygame.K_UP)) and self.car.rect.y > 0.0:
                self.car.move_up()
            elif (self.pressed.get(pygame.K_s) or self.pressed.get(pygame.K_DOWN)) and self.car.rect.y  + self.car.rect.height < 600.0:
                self.car.move_down()

            self.event_car.update_bar(screen)
            self.event_barrage.update_bar(screen)
            self.event_barrage2.update_bar(screen)

            for self.car_obstacle in self.event_car.all_cars:
                self.car_obstacle.out_screen()
            self.event_car.all_cars.draw(screen)

            for self.barrage in self.all_barrages:
                self.barrage.out_screen()
            self.all_barrages.draw(screen)

            for self.barrage2 in self.all_barrages2:
                self.barrage2.out_screen()
            self.all_barrages2.draw(screen)
            
            score_text_1 = self.font.render("Score", 1, (0,0,0))
            pygame.draw.line(screen, (0,0,0), (702,50), (775,50), 2)
            score_text_2 = self.font.render("{0}".format(int(self.score)), 1, (0,0,0))
            screen.blit(score_text_1, (700, 10))
            if self.score < 10:
                screen.blit(score_text_2, (730, 65))
            if self.score >= 10 and self.score < 100:
                screen.blit(score_text_2, (720, 65))
            if self.score >= 100 and self.score < 1000:
                screen.blit(score_text_2, (712, 65))
            if self.score >= 1000 and self.score < 10000:
                screen.blit(score_text_2, (704, 65))
            if self.score >= 10000:
                screen.blit(score_text_2, (694, 65))
            if self.score < 10:
                self.score += 0.005 * 6
            if self.score >= 10 and self.score < 100:
                self.score += 0.01 * 6
            if self.score >= 100 and self.score < 1000:
                self.score += 0.01 * 6
            if self.score >= 1000 and self.score < 10000:
                self.score += 0.05 * 6
            if self.score >= 10000 and self.score < 100000:
                self.score += 0.1 * 6
            if self.score >= 100000 and self.score < 1000000:
                self.score += 0.5 * 6
            if self.score >= 1000000:
                self.score += 1 * 6 

    def check_collision(self, sprite, group):
        """
        Fonction vérifiant les collisions entre un sprite et un group de sprite retournant True
        """
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
