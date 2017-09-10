#!/usr/bin/env python3

import os
import pygame
from pygame.locals import *


if __name__ == '__main__':

    pygame.init()

    #clock = pygame.time.Clock()
    continuer = 1

    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption('Flo is Life,Quentin is Game')
    background = pygame.Surface(screen.get_size())

    if pygame.font:
        font = pygame.font.Font(None,36)
        text = font.render("F&Q's Game of Life",1,(10,10,10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text,textpos)

    #HAUTEUR_GRILLE
    #LARGEUR_GRILLE

    grid = pygame.draw.rect(background,(255,255,255),(20,20,560,360),1)
    for i in range (17): #LARGEUR_GRILLE 18
        ligne = colonne = pygame.draw.line(background, (255,255,255),(20,40+20*i),(579,40+20*i),1)
    for i in range (27): #HAUTEUR_GRILLE 28
        colonne = pygame.draw.line(background, (255,255,255),(40+20*i,20),(40+20*i,379),1)

    screen.blit(background,(0,0))
    pygame.display.flip()





    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT: #Si un de ces événements est de type QUIT
                continuer = 0

    quit()
