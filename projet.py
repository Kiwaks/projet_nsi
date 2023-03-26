import pygame
from game import Game
from random import *
import button
import math
pygame.init()

width = 800
height = 600
running = True
FPS = 60
clock = pygame.time.Clock()
laps = 0

screen = pygame.display.set_mode([width, height])
background = pygame.image.load("../projet_nsi/assets/bg.png")
pygame.display.set_caption("Need More Speed")
pygame_icon = pygame.image.load('../projet_nsi/assets/icon.png')
pygame.display.set_icon(pygame_icon)
game = Game()
start_btn_img = pygame.image.load("../projet_nsi/assets/bouton_start.png").convert_alpha()
start_btn_img = pygame.transform.scale(start_btn_img, (290,120)).convert_alpha()
background_accueil_1 = pygame.image.load("../projet_nsi/assets/accueil_bg_1.png")
background_accueil_2 = pygame.image.load("../projet_nsi/assets/accueil_bg_2.png")
joueur_choix = pygame.image.load("../projet_nsi/assets/joueur_choix.png").convert_alpha()
joueur_choix = pygame.transform.scale(joueur_choix, (352,352)).convert_alpha()
bouton_entry = pygame.image.load("../projet_nsi/assets/entry.png").convert_alpha()
bouton_entry = pygame.transform.scale(bouton_entry, (65,65))
game_over_img = pygame.image.load("../projet_nsi/assets/game_over.png")
pause_img = pygame.image.load("../projet_nsi/assets/pause.png")
pause_quit = pygame.image.load("../projet_nsi/assets/quit_pause.png").convert_alpha()
pause_quit = pygame.transform.scale(pause_quit, (548,76)).convert_alpha()
pause_restart = pygame.image.load("../projet_nsi/assets/restart_pause.png").convert_alpha()
pause_restart = pygame.transform.scale(pause_restart, (548,76)).convert_alpha()
pause_resume = pygame.image.load("../projet_nsi/assets/resume_pause.png").convert_alpha()
pause_resume = pygame.transform.scale(pause_resume, (550,76)).convert_alpha()
score_best = pygame.image.load("../projet_nsi/assets/score_best.png")
score_moy = pygame.image.load("../projet_nsi/assets/score_moy.png")
score_der = pygame.image.load("../projet_nsi/assets/score_der.png")
score_min = pygame.image.load("../projet_nsi/assets/score_min.png")
score_list = []
font = pygame.font.SysFont('Calibri', 36)
y_background =  -80
speed = 4

def reset():
    """
    Fonction permettant de réinitialiser toutes les valeurs du jeu 
    """
    game.score = 0
    game.event_barrage.all_cars.remove(game.barrage)
    game.event_barrage2.all_cars.remove(game.barrage2)
    game.event_car.all_cars.remove(game.car_obstacle)
    game.car.rect.x = 340
    game.car.rect.y = 300
    game.car.hearts = 3
    game.event_car.percent = 0
    game.event_barrage.percent = 0
    game.event_barrage2.percent = 0
    game.barrage.is_active = False
    game.barrage2.is_active = False
    game.barrage.is_spawning = False
    game.car_obstacle.is_driving = False
    game.pause = False

while running:
    clock.tick(FPS)
    y_background += 4
    if y_background < 600:
        screen.blit(background, (0, y_background))
        screen.blit(background, (0,y_background-600))
        speed += 1
    else :
        y_background = 0
        screen.blit(background, (0, y_background))
        speed += 2  

    if game.is_starting == 10:
        if game.pause == False:
            screen.blit(game_over_img, (0,0))
            game_over_text = game.game_over_font.render("{0}".format(int(game.score)), 1, (255,255,255))
            if game.score < 10:
                screen.blit(game_over_text, (382, 335))
            if game.score >= 10 and game.score < 100:
                screen.blit(game_over_text, (357, 335))
            if game.score >= 100 and game.score < 1000:
                screen.blit(game_over_text, (327, 335))
            if game.score >= 1000 and game.score < 10000:
                screen.blit(game_over_text, (297, 335))
            if game.score >= 10000 and game.score < 100000:
                screen.blit(game_over_text, (272, 335))
            if game.score >= 100000 and game.score < 1000000:
                screen.blit(game_over_text, (237, 335))
            if game.score >= 1000000:
                screen.blit(game_over_text, (207, 335))
            score_list.append(game.score)
            if game.pressed.get(pygame.K_SPACE):
                game.pause = True
        elif game.pause == True:
            screen.blit(pause_img, (0,0))
            button_quit_pause = button.Button(135, 400, pause_quit, 1)
            if button_quit_pause.draw(screen):
                game.is_starting = 1
                score_list.append(game.score)
                reset()
            button_resume_pause = button.Button(132, 202, pause_resume, 1)
            if button_resume_pause.draw(screen):
                game.pause = False
    if game.is_starting == 0:
        screen.blit(background_accueil_1, (0,0))
        button_start = button.Button(245, 240, start_btn_img, 1)
        if button_start.draw(screen) or game.pressed.get(pygame.K_SPACE):
            game.is_starting = 1
            suite = False
    if game.is_starting == 1:
        screen.blit(background_accueil_2, (0,0))
        button_entry_1 = button.Button(760, 495, bouton_entry, 0.5)
        screen.blit(joueur_choix, (224, 124))
        if game.pressed.get(pygame.K_j):
            game.is_starting = 2
        if button_entry_1.draw(screen) or game.pressed.get(pygame.K_s):
            game.is_starting = 5
    if game.is_starting == 5:
        if game.pressed.get(pygame.K_SPACE):
            game.pause = True
        if game.pause == False:
            with open("scores.txt", "r") as c:
                scores = [float(score) for score in c.readlines()]
                meilleur_score = max(scores)
                dernier_score = scores[-1]
                moyenne_scores = sum(scores) / len(scores)
                pire_score = min(scores)
            c.close()
            screen.blit(score_best, (100, 350))
            score_meilleur = font.render("{0}".format(round(meilleur_score, 2)), 1, (255,255,255))
            largeur_text_1, hauteur_text_1 = font.size(str(score_meilleur))
            screen.blit(score_meilleur, ((350-(largeur_text_1/2)), 425))
            screen.blit(score_der, (100, 100))
            score_dernier = font.render("{0}".format(round(dernier_score, 2)), 1, (255,255,255))
            largeur_text_2, hauteur_text_2 = font.size(str(score_dernier))
            screen.blit(score_dernier, (350-(largeur_text_2/2), 175))
            screen.blit(score_moy, (450, 100))
            score_moyenne = font.render("{0}".format(round(moyenne_scores, 2)), 1, (255,255,255))
            largeur_text_3, hauteur_text_3 = font.size(str(score_moyenne))
            screen.blit(score_moyenne, (700-(largeur_text_3/2), 175))
            screen.blit(score_min, (450, 350))
            score_pire = font.render("{0}".format(round(pire_score, 2)), 1, (255,255,255))
            largeur_text_4, hauteur_text_4 = font.size(str(score_pire))
            screen.blit(score_pire, (700-(largeur_text_3/2), 425))
        elif game.pause == True:
            screen.blit(pause_img, (0,0))
            button_quit_pause = button.Button(135, 400, pause_quit, 1)
            if button_quit_pause.draw(screen):
                game.is_starting = 1
                game.pause = False
            button_resume_pause = button.Button(132, 202, pause_resume, 1)
            if button_resume_pause.draw(screen):
                game.pause = False
    if game.is_starting == 2:
        if game.pause == False:
            game.update(screen)
            if game.pressed.get(pygame.K_SPACE):
                game.pause = True
        elif game.pause == True:
            screen.blit(pause_img, (0,0))
            button_quit_pause = button.Button(135, 400, pause_quit, 1) 
            if button_quit_pause.draw(screen):
                game.is_starting = 1
                score_list.append(game.score)
                reset()
            button_resume_pause = button.Button(132, 202, pause_resume, 1)
            if button_resume_pause.draw(screen):
                game.pause = False
            button_restart_pause = button.Button(134, 303, pause_restart, 1)
            if button_restart_pause.draw(screen):
                score_list.append(game.score)
                reset()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if game.score != 0:
                score_list.append(game.score)
            score_list = list(set(score_list))
            with open("scores.txt", "a") as file:
                for s in score_list:
                    file.write(str(s) + "\n")
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        