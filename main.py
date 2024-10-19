
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
lawText = 'Закон тяжести'
impulsText = 'Упругие столкновения'
speed=10000

item={-1: [100, 100, 20, 0.1, 0, 10, par.RED], -2: [500, 100, 20, 0, 0, 10, par.WHITE]}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]

menu=1#1-Главное меню, 2 - создание объекта, 3 - натсройки физики
#4 - настройки приложения, 5 - Экстра функции

#Количество предметов
nomber=3

tick=1
#Зона кнопок
buttons_main_menu=[]
buttons_create_obj=[]
buttons_physics_law = []

def CreateObject(x, y): #Метод для создания объекта(ObjectData - массив с со значениями объекта)
    global nomber
    item.update({nomber:[x,y,float(ObjectData[0]), float(ObjectData[1]), float(ObjectData[2]), float(ObjectData[3]), par.WHITE]})
    nomber+=1
       
k = 0       
objects = []
while Work:
    if tick>10000:
        tick=0
    tick+=1
    cloak.tick(fps * speed);  # Контроль фпс
    win.fill(background_color)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Выход из программы
            Work = False
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #Это нужно, чтобы обработчки событий для кнопки срабатывал только при клике, а не при удерживании
        k = 0
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and k != 1:  #Обработчик событий для кнопок
        k = 1
        if menu==1:
            if buttons_main_menu[0].collidepoint(event.pos):
                menu = 2
                pygame.time.delay(200)
            elif buttons_main_menu[1].collidepoint(event.pos):#Добавить
                None
            elif buttons_main_menu[2].collidepoint(event.pos):#Импорт
                menu = 3
                pygame.time.delay(200)
            elif buttons_main_menu[3].collidepoint(event.pos):#Настройки физики
                None
            elif buttons_main_menu[4].collidepoint(event.pos):#Настройки приложения
                None
            elif buttons_main_menu[5].collidepoint(event.pos):#Экстра
                None
            elif buttons_main_menu[6].collidepoint(event.pos):#Выбрать
                None
            elif buttons_main_menu[7].collidepoint(event.pos):#Выбрать
                Work = False
        elif menu==2:
            if buttons_create_obj[1].collidepoint(event.pos):
                menu = 1
            elif event.pos[0]<wide-otstup and event.pos[0]>0 and event.pos[1]>0 and event.pos[1]<hight:
                CreateObject(event.pos[0], event.pos[1])
        elif menu == 3:
            if buttons_physics_law[0].collidepoint(event.pos):
                if par.GravityType == 1:
                    lawText = 'Закон всемирного тяготения'
                    par.GravityType = 2
                else:
                    lawText = 'Закон тяжести'
                    par.GravityType = 1           
            elif buttons_physics_law[1].collidepoint(event.pos):
               if par.ImpulsType == 1:
                    impulsText = 'Неупругие столкновения'
                    par.ImpulsType = 2
               else:
                    impulsText = 'Упругие столкновения'
                    par.ImpulsType = 1 
            elif buttons_physics_law[2].collidepoint(event.pos):
               if ParametersData[0] != '' and ParametersData[1] != '':
                   par.g = float(ParametersData[0])
                   par.G = float(ParametersData[1])*10**(-11)
                   menu = 1

    for i in item:
        draw.DrawItem(item[i], win)
        if(menu==1):
            proc.Item_Update(item, i)

    #UpdateObjects()
    if (tick%10==0 or menu != 1):
        if(menu==1):
            buttons_main_menu = MainMenu(win, font)
        elif(menu == 2):
            buttons_create_obj, menu = CreateObj(win, font)
        elif(menu==3):
            buttons_physics_law, menu = PhysicsOption(lawText,impulsText, win, font)
        pygame.display.update();    #Обновление экрана
        

pygame.quit()

