
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

item={1: [100, 100, 20, 0.1, 0, 10, par.RED], 21: [500, 100, 20, 0, 0, 10, par.WHITE]}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]

menu=1#1-Главное меню, 2 - создание объекта, 3 - натсройки физики
#4 - настройки приложения, 5 - Экстра функции

tick=1
#Зона кнопок

buttons_main_menu=[]
buttons_create_obj=[]
def CreateObject(): #Метод для создания объекта(ObjectData - массив с со значениями объекта)
    None

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
            if buttons_main_menu[0].collidepoint(event.pos):
                menu = 2
                pygame.time.delay(200)
            elif buttons_main_menu[1].collidepoint(event.pos):#Добавить
                None
            elif buttons_main_menu[2].collidepoint(event.pos):#Импорт
                None
            elif buttons_main_menu[3].collidepoint(event.pos):#Настройки физики
                None
            elif buttons_main_menu[4].collidepoint(event.pos):#Настройки приложения
                menu=3
            elif buttons_main_menu[5].collidepoint(event.pos):#Экстра
                None
            elif buttons_main_menu[6].collidepoint(event.pos):#Выбрать
                None
            elif buttons_main_menu[7].collidepoint(event.pos):#Выбрать
                Work = False
        elif menu==2:
            if buttons_create_obj[0].collidepoint(event.pos):
                CreateObject()
                pygame.time.delay(200)
            elif buttons_create_obj[1].collidepoint(event.pos):
                menu = 1
                pygame.time.delay(200)
                
    for i in item:
        draw.DrawItem(item[i], win)
        proc.Item_Update(item, i)
    if (tick%10==0):
        if(menu==1):
            buttons_main_menu = MainMenu(win, font)
        elif(menu == 2):
            buttons_create_obj = CreateObj(win, font) 
        elif(menu==3):
            None
        pygame.display.update();    #Обновление экрана
        

pygame.quit()
