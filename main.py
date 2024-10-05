
import pygame
import test
import parameters as par

pygame.init() #Просто запуск pygame


win = pygame.display.set_mode((par.wide, par.hight))    # Создание окна !win! 1200*700
size_stand=24
font = pygame.font.SysFont("", size_stand, 'utf-8')     #Создание Шрифта

Work=True   #Рабочий цикл(не относится к pygame)
cloak=pygame.time.Clock()   #Создание функции контроля фпс
#Параметры программы
background_color=par.BLACK
fps=60

speed=10000

item={}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]

while Work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Выход из программы
            Work = False

    cloak.tick(fps*speed);  #Контроль фпс

    win.fill(background_color)
    #pygame.draw.rect(win, (255, 255, 255), (x, y, 20, 20))#Создание квадратика 20 на 20

    pygame.display.update();    #Обновление экрана