#!/usr/bin/env python3

import os
import pygame
from pygame.locals import *


if __name__ == '__main__':

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption('Flo is Life,Quentin is Game')
    background = pygame.Surface(screen.get_size())

    if pygame.font:
        font = pygame.font.Font(None,36)
        text = font.render("F&Q's Game of Life",1,(10,10,10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text,textpos)


    grid = pygame.draw.rect(background,(255,255,255),(20,20,560,360),1)
    screen.blit(background,(0,0))
    pygame.display.flip()

    while 1:
        clock.tick(500)




    quit()
