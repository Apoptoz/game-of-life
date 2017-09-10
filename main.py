#!/usr/bin/env python3

import os
import pygame
from pygame.locals import *

HAUTEUR_GRILLE = 20
LARGEUR_GRILLE = 30


if __name__ == '__main__:
    
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


    grid = pygame.draw.rect(background,(255,255,255),(20,20,560,360),1)
    #for i in range (18): #ligne
    for j in range (28): #colonne
        case = pygame.draw.rect(background,(255,255,255),(20+20*j,20,40+20*j,40),1)


    screen.blit(background,(0,0))
    pygame.display.flip()





    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT: #Si un de ces événements est de type QUIT
                continuer = 0

    quit()
