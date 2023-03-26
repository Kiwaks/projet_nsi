import pygame
from random import *

class Car_obstacle(pygame.sprite.Sprite):
    def __init__(self, event_car):
        super().__init__()
        self.velocity = 7 
        self.image = pygame.image.load('../projet_nsi/assets/voiture_pc_p.png')
        self.rect = self.image.get_rect()
        self.rect.x = choice([160,340,520])
        self.rect.y = 1000
        self.is_driving = True
        self.event_car = event_car

    def out_screen(self):
        """
        Fonction permettant de faire avancer la voiture de police et vérifier si on peut la supprimer
        """
        self.rect.y -= self.velocity
        if self.rect.y < -100:
            self.event_car.all_cars.remove(self)
            self.is_driving = False
            
