import pygame
from random import *

class Barrage2(pygame.sprite.Sprite):
    def __init__(self, event_barrage2):
        super().__init__()
        self.image = pygame.image.load('../projet_nsi/assets/voiture_barrage.png')
        self.image = pygame.transform.scale(self.image, (181,102))
        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = -210
        self.velocity = 5
        self.is_active = True
        self.event_barrage2 = event_barrage2

    def out_screen(self):
        """
        Fonction permettant de faire avancer le barrage et vérifier si on peut le supprimer
        """
        self.rect.y += self.velocity
        if self.rect.y > 810 and self.is_active == True:
            self.event_barrage2.all_cars.remove(self)
            self.is_active = False
            