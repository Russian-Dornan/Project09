
import pygame
import test
import draw
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

item={1: [100, 100, 20, 0, 0, 10, par.RED]}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]

while Work:
    cloak.tick(fps * speed);  # Контроль фпс
    win.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Выход из программы
            Work = False

    for i in item:
        draw.DrawItem(item[i], win)

    pygame.display.update();    #Обновление экрана