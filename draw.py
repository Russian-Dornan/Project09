import pygame

import parameters as par

def DrawItem(mass, win):

    if(par.FormType==1):

        pygame.draw.rect(win, mass[6], (mass[0], mass[1], mass[2], mass[2]))
