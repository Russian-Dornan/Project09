
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
font_speed=pygame.font.SysFont("", 30, '')
Work=True   #Рабочий цикл(не относится к pygame)
cloak=pygame.time.Clock()   #Создание функции контроля фпс
#Параметры программы
background_color=par.BLACK
fps=60
lawText = 'Закон тяжести'
impulsText = 'Упругие столкновения'
speed=10000

#item={1: [300, 500, 20, 0.05, 0, 2000000000, par.RED], 2: [500, 300, 20, 0.05, 0, 11, par.WHITE], 3: [600, 600, 20, 0, 0, 20000000000, par.RED]}# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]
item={}
menu=1#1-Главное меню, 2 - создание объекта, 3 - натсройки физики
#4 - настройки приложения, 5 - Экстра функции

#Количество предметов
nomber=3
chosen_one=-10
follow_one=-1


tick=1
#Зона кнопок
buttons_main_menu=[]
buttons_create_obj=[]
buttons_physics_law = []

def CreateObject(x, y): #Метод для создания объекта(ObjectData - массив с со значениями объекта)
    global nomber
    try:
        item.update({nomber:[x,y,float(ObjectData[0]), float(ObjectData[1]), float(ObjectData[2]), float(ObjectData[3]), par.WHITE]})
    except:
        #Пользователь косяк
        None
    nomber+=1
def Following(x, y):


    delta_x = x - par.wide // 2
    delta_y = y - par.hight // 2
    if delta_x!=0 or delta_y!=0:
        for i in item:
            item[i][0]-=delta_x
            item[i][1]-=delta_y

k = 0       
objects = []
while Work:
    if tick>10000:
        tick=0
    tick+=1
    cloak.tick(fps * speed);  # Контроль фпс
    win.fill(background_color)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        for i in item:
            item[i][0]+=1
    if keys[pygame.K_RIGHT]:
        for i in item:
            item[i][0]-=1
    if keys[pygame.K_UP]:
        for i in item:
            item[i][1]+=1
    if keys[pygame.K_DOWN]:
        for i in item:
            item[i][1]-=1
    events = pygame.event.get();
    for event in events:

        if event.type == pygame.QUIT:   #Выход из программы
            Work = False
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #Это нужно, чтобы обработчки событий для кнопки срабатывал только при клике, а не при удерживании
        k = 0
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and k != 1:  #Обработчик событий для кнопок
        k = 1
        mouse_pos = event.pos
        if menu==1:

            if buttons_main_menu[0].collidepoint(event.pos):
                menu = 2
            elif buttons_main_menu[1].collidepoint(event.pos):#Добавить
                try:
                    f = open('input.txt')
                    for line in f:
                        etem = line.split()
    
                        item.update({nomber: [eval(etem[0]), eval(etem[1]), eval(etem[2]), eval(etem[3])/10,
                                               eval(etem[4]) , eval(etem[5]) , par.STANDART]})
                        nomber += 1
                    f.close()
                except: 
                    f = open('input.txt', 'x')
                    f.close()

            elif buttons_main_menu[2].collidepoint(event.pos):#Импорт
                menu = 3
            elif buttons_main_menu[3].collidepoint(event.pos):#Настройки физики
                while item!={}:
                        follow_one=-1
                        try:
                            for i in item:
                                item.pop(i)
                        except:
                            None
            elif buttons_main_menu[4].collidepoint(event.pos):#Векторы
                par.is_vectors*=-1
            elif buttons_main_menu[5].collidepoint(event.pos):#Экстра
                par.pause*=-1
            elif buttons_main_menu[6].collidepoint(event.pos):#Выбрать
                if is_follow==1:
                    follow_one=-1
                is_follow*=-1
            elif buttons_main_menu[7].collidepoint(event.pos):#Выбрать
                Work = False
        elif menu==2:
            if buttons_create_obj[0].collidepoint(event.pos):
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
        if pygame.Rect(item[i][0], item[i][1], item[i][2], item[i][2]).collidepoint(mouse_pos):
            chosen_one=i
            if(is_follow==1):
                follow_one=i
                is_follow=-1

        if(menu==1 and par.pause==-1):
            proc.Item_Update(item, i)
    if(follow_one!=-1):
          Following(item[follow_one][0], item[follow_one][1])

    #UpdateObjects()
    if (tick%10==0 or menu != 1):

        if(chosen_one!=-10):
            win.blit((font.render(("Index "+str(chosen_one)), True, GREEN)), (10, 10))
            try:
                win.blit((font_speed.render(("Ux = "+str(item[chosen_one][3])), True, GREEN)), (10, 20))
                win.blit((font_speed.render(("Uy = " + str((item[chosen_one][4]))), True, GREEN)), (10, 40))
            except:
                chosen_one=-10
        if(menu==1):
            buttons_main_menu = MainMenu(win, font)
        elif(menu == 2):
            buttons_create_obj, menu = CreateObj(win, font, events)
        elif(menu==3):
            buttons_physics_law, menu = PhysicsOption(lawText,impulsText, win, font, events)
        pygame.display.update();    #Обновление экрана


pygame.quit()

