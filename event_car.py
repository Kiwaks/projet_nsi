import pygame
from random import *
from car_obstacle import Car_obstacle

class Event_car(pygame.sprite.Sprite):
    def __init__(self, game):
        self.percent = 0
        self.all_cars = pygame.sprite.Group()
        self.game = game

    def add_percent(self):
        """
        Ajouter 0.009 * 12 * 2 à la variable percent
        """
        self.percent += 0.025 * 12 * 2

    def is_full_loaded(self):
        """
        Fonction permettant de renvoyer self.percent >= 100
        """
        return self.percent >= 100

    def generations_cars(self):
        """
        Fonction permettant d'ajouter un sprite (Car_obstacle) dans le group de sprite all_cars
        """
        self.all_cars.add(Car_obstacle(self))

    def attempt_generations_cars(self):
        """
        Fonction permettant de vérifier si on peut faire apparaitre la voiture si la fonction is_full_loaded() renvoit self.percent >= 100
        """
        if self.is_full_loaded() and len(self.game.event_barrage2.all_cars) == 0:
            self.generations_cars()
            self.percent = 0

    def update_bar(self, screen):
        self.add_percent()
        self.attempt_generations_cars()
