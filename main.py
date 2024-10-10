
import pygame
import test
import draw
import parameters as par
import processor as proc

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

item={1: [100, 100, 20, 0.2, 0.1, 10, par.RED]}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]
menu=1
while Work:
    cloak.tick(fps * speed);  # Контроль фпс
    win.fill(background_color)
    if(menu==1):
        buttons =[
        draw.GetButton(20, 10, 100, 40,'Добавить объект', win), #Массив с кнопками
        draw.GetButton(20, 60, 90, 40,'Выйти', win)
        ]
    elif(menu==2):
        buttons = [

            draw.GetButton(20, 60, 90, 40, 'Выйти', win)
        ]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Выход из программы
            Work = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #Обработчик событий для кнопок
        if buttons[0].collidepoint(event.pos) and menu==1:
            menu=2
            pygame.time.delay(200)
        elif buttons[0].collidepoint(event.pos) and menu==2:
            menu=1
            pygame.time.delay(200)
        elif buttons[1].collidepoint(event.pos):
            Work=False

    for i in item:
        draw.DrawItem(item[i], win)
        proc.Item_Update(item, i)
    pygame.display.update();    #Обновление экрана

pygame.quit()
