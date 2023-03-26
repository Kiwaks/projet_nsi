import pygame
from random import *

class Barrage(pygame.sprite.Sprite):
    def __init__(self, event_barrage):
        super().__init__()
        self.image = pygame.image.load('../projet_nsi/assets/voiture_barrage.png')
        self.image = pygame.transform.scale(self.image, (181,102))
        self.rect = self.image.get_rect()
        self.rect.x = choice([125,480])
        self.rect.y = -210
        self.velocity = 5
        self.is_active = True
        self.is_spawning = True
        self.event_barrage = event_barrage

    def out_screen(self):
        """
        Fonction permettant de faire avancer le barrage et vérifier si on peut le supprimer ainsi 
        que de le faire pivoter de 10 degrés sur la droite ou la gauche en focntion de sa position
        """
        if self.rect.x == 125 and self.is_spawning == True:
                self.image = pygame.transform.rotate(self.image, 10)
                self.is_spawning = False
        if self.rect.x == 480 and self.is_spawning == True:
                self.image = pygame.transform.rotate(self.image, -10)
                self.is_spawning = False
        self.rect.y += self.velocity
        if self.rect.y > 600 and self.is_active == True:
            self.event_barrage.all_cars.remove(self)
            self.is_active = False
            


             