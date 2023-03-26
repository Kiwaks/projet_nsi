import pygame
from random import *

class Car(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 7
        self.image = pygame.image.load('../projet_nsi/assets/voiture.png')
        self.hearts_image = pygame.image.load('../projet_nsi/assets/vie.png')
        self.hearts_image = pygame.transform.scale(self.hearts_image, (100,100))
        self.hearts = 3
        self.hearts_max = 5
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 300
        self.game = game

    def collisions_with_obstacles(self):
        """
        Fonction permettant de vérifier s'il ya collisions entre la voiture et la voiture de police/barrage
        """
        if (self.game.check_collision(self, self.game.all_cars) or self.game.check_collision(self, self.game.all_barrages)) or self.game.check_collision(self, self.game.all_barrages2):
            self.game.car.rect.x = 340
            self.game.car.rect.y = 300
            self.game.car.hearts -= 1
            self.game.barrage.is_active = False
            self.game.car.is_driving = False
            self.game.event_car.all_cars.remove(self.game.all_cars)
            self.game.event_barrage.all_cars.remove(self.game.all_barrages)
            self.game.event_barrage2.all_cars.remove(self.game.all_barrages2)
            self.game.event_barrage.percent = 40
            self.game.event_barrage2.percent = 40
            self.game.event_car.percent = 25

    def move_right(self):
        """
        Fonction permettant de faire avancer la voiture vers la droite
        """
        if not (self.game.check_collision(self, self.game.all_cars) or self.game.check_collision(self, self.game.all_barrages) or self.game.check_collision(self, self.game.all_barrages2)):
            self.rect.x += self.velocity

    def move_left(self):
        """
        Fonction permettant de faire avancer la voiture vers la gauche
        """
        if not (self.game.check_collision(self, self.game.all_cars) or self.game.check_collision(self, self.game.all_barrages) or self.game.check_collision(self, self.game.all_barrages2)):
            self.rect.x -= self.velocity        

    def move_up(self):
        """
        Fonction permettant de faire avancer la voiture vers le haut
        """
        if not (self.game.check_collision(self, self.game.all_cars) or self.game.check_collision(self, self.game.all_barrages) or self.game.check_collision(self, self.game.all_barrages2)):
            self.rect.y -= self.velocity

    def move_down(self):
        """
        Fonction permettant de faire avancer la voiture vers le bas
        """
        if not (self.game.check_collision(self, self.game.all_cars) or self.game.check_collision(self, self.game.all_barrages) or self.game.check_collision(self, self.game.all_barrages2)):
            self.rect.y += self.velocity

        
