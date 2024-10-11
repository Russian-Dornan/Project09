
import pygame
import test
import draw
import parameters as par
import processor as proc
from interface import *
pygame.init() #Просто запуск pygame


win = pygame.display.set_mode((par.wide, par.hight))    # Создание окна !win! 1200*700
size_stand=16
font = pygame.font.SysFont("", size_stand, '')     #Создание Шрифта

Work=True   #Рабочий цикл(не относится к pygame)
cloak=pygame.time.Clock()   #Создание функции контроля фпс
#Параметры программы
background_color=par.BLACK
fps=60

speed=10000

item={1: [100, 100, 20, 0.2, 0.1, 10, par.RED]}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]

menu=1#1-Главное меню, 2 - создание объекта, 3 - натсройки физики
#4 - настройки приложения, 5 - Экстра функции

tick=1
#Зона кнопок

buttons_main_menu=[]


while Work:
    if tick>10000:
        tick=0
    tick+=1
    cloak.tick(fps * speed);  # Контроль фпс
    win.fill(background_color)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Выход из программы
            Work = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #Обработчик событий для кнопок
        if menu==1:
            if buttons_main_menu[0]:
                print("Test")
            elif buttons_main_menu[1]:#Добавить
                None
            elif buttons_main_menu[2]:#Импорт
                None
            elif buttons_main_menu[3]:#Настройки физики
                None
            elif buttons_main_menu[4]:#Настройки приложения
                None
            elif buttons_main_menu[5]:#Экстра
                None
            elif buttons_main_menu[6]:#Выбрать
                None
            elif buttons_main_menu[7]:#Следовать
                None
            elif buttons_main_menu[8]:
                None
        elif menu==2:
            None

    for i in item:
        draw.DrawItem(item[i], win)
        proc.Item_Update(item, i)

    if (tick%20==0):
        if(menu==1):
            buttons_main_menu = MainMenu(win, font)
        pygame.display.update();    #Обновление экрана

pygame.quit()
