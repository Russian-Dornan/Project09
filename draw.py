import pygame
import math
import parameters as par
def Vectors(x, y, wide, hight, Ux, Uy, win):
    U = math.sqrt(Ux ** 2 + Uy ** 2)
    try:
        alfa1=math.asin(Ux/U)
        alfa2 = math.acos(Uy / U)
        pygame.draw.line(win, (200, 0, 0), (x+wide//2, y+hight//2), ((x+wide//2+40*math.sin(alfa1), y+hight//2+40*math.cos(alfa2))), 3)
    except:
        None
def DrawItem(mass, win):

    if(par.FormType==1):

        pygame.draw.rect(win, mass[6], (mass[0], mass[1], mass[2], mass[2]))
    if(par.is_vectors==1):
        Vectors(mass[0], mass[1], mass[2], mass[2], mass[3], mass[4], win)
def GetButton(x, y, width, height, text, win, font):
    text = font.render(text, True, par.BLACK)
    button_surface = pygame.Surface((width, height))
    text_rect = text.get_rect(center=(button_surface.get_width() /2, button_surface.get_height()/2))
    button_rect = pygame.Rect(x, y, width, height)
    button_surface.fill(par.WHITE)
    #ChangeColor(button_rect, button_surface)
    button_surface.blit(text, text_rect)
    win.blit(button_surface, (button_rect.x, button_rect.y))
    return button_rect

def ChangeColor(button_rect, button_surface):
    pointer = pygame.mouse.get_pos()
    if button_rect.collidepoint(pointer):
        button_surface.fill(par.SKY_BLUE)
    else:
        button_surface.fill(par.WHITE)
