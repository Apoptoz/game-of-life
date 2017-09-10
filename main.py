#!/usr/bin/env python3

import os
import pygame
from pygame.locals import *

import population

NB_LIGNE = 18
NB_COLONNE = 28

NB_WHITE = 10
NB_BLUE = 11
NB_BLACK = 12
NB_RED = 13
NB_GREEN = 14

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



    grid = pygame.draw.rect(background,(255,255,255),(20,20,560,360),1)
    for i in range (NB_LIGNE-1):
        ligne = colonne = pygame.draw.line(background, (255,255,255),(20,40+20*i),(579,40+20*i),1)
    for i in range (NB_COLONNE-1):
        colonne = pygame.draw.line(background, (255,255,255),(40+20*i,20),(40+20*i,379),1)


    white_cell = pygame.image.load("data/white_cell.png")
    blue_cell = pygame.image.load("data/blue_cell.png")
    black_cell = pygame.image.load("data/black_cell.png")
    red_cell = pygame.image.load("data/red_cell.png")
    green_cell = pygame.image.load("data/green_cell.png")


    pop = population.Population([NB_WHITE,NB_BLUE,NB_BLACK,NB_RED,NB_GREEN])
    for cellule in pop:
        print(cellule)
        x = cellule.coord_x * 20 + 20
        y = cellule.coord_y * 20 + 20
        map_to_colour = { "W":white_cell,
        "B":blue_cell,
        "N":black_cell,
        "R":red_cell,
        "G":green_cell}
        background.blit(map_to_colour[cellule.colour], (x,y))




    screen.blit(background,(0,0))
    pygame.display.flip()



    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT: #Si un de ces événements est de type QUIT
                continuer = 0

    quit()
