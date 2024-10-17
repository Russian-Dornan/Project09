import draw
import pygame
from parameters import *

''''
main_menu_options=["Добавить бъект", "Импорт сценария",
                   "Настройки физики", "Настройки приложения",
                   "Экстра функции", "Выбрать объект",
                   "Следовать за объектом"]

k=0
x=base_x
y=base_y
print("[")
for i in main_menu_options:
        print("draw.GetButton("+str(x)+", "+str(y)+", "+
                        str(size_x)+", "+str(size_y)+", "+"'"+i+"'"+", win, font), ")
        if k%2==0:
                x+=size_x+step
                k+=1
        else:
                x=base_x
                y+=size_y+step
                k+=1
print("]")
'''
ObjectData = ['', '', '', '']
input_rects = [pygame.Rect(1010, 35, 80, 20), pygame.Rect(1035, 60, 80, 20), pygame.Rect(1035, 85, 80, 20), pygame.Rect(1010, 110, 80, 20)]
def MainMenu(win, font):
        Main_Menu_Buttons = [
                draw.GetButton(975, 10, 200, 50, 'Добавить объект', win, font),
                draw.GetButton(975, 70, 200, 50, 'Импорт сценария', win, font),
                draw.GetButton(975, 130, 200, 50, 'Настройки физики', win, font),
                draw.GetButton(975, 190, 200, 50, "Настройки приложения", win, font),
                draw.GetButton(975, 250, 200, 50, 'Экстра функции', win, font),
                draw.GetButton(975, 310, 200, 50, 'Выбрать объект', win, font),
                draw.GetButton(975, 370, 200, 50, 'Следовать', win, font),
                draw.GetButton(975, 430, 200, 50, 'Выход', win, font)
                ]

        return Main_Menu_Buttons
def CreateObj(win, font):
        GenerateText(win)
        CreateInputBox(win)
        Create_obj_Buttons = [
                draw.GetButton(975, 150, 200, 50, 'Создать объект', win, font),
                draw.GetButton(975, 210, 200, 50, 'Главное меню', win, font)
                ]
        return Create_obj_Buttons
def GenerateText(win):
       my_font = pygame.font.SysFont('Comic Sans MS', 15)
       par_font = pygame.font.SysFont('Comic Sans MS', 13)
       text_surface = my_font.render('Введите значения объекта: ', False, WHITE)
       win.blit(text_surface, (980, 10))
       size_surface = par_font.render('Size: ', False, WHITE)
       win.blit(size_surface, (975, 35))
       speedx_surface = par_font.render('Speed_x: ', False, WHITE)
       win.blit(speedx_surface, (975, 60))
       speedy_surface = par_font.render('Speed_x: ', False, WHITE)
       win.blit(speedy_surface, (975, 85))
       mass_surface = par_font.render('Mass: ', False, WHITE)
       win.blit(mass_surface, (975, 110))

active = 1
def CreateInputBox(win):
        my_font = pygame.font.SysFont('Comic Sans MS', 13)
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(len(input_rects)):
                                if input_rects[i].collidepoint(event.pos):
                                        global active
                                        active = i
                                        break
                user_text = ObjectData[active]
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                                user_text = user_text[:-1] 
                        else:
                                if len(user_text) <= 5 and event.unicode in '0123456789':
                                        user_text += event.unicode
                        ObjectData[active] = user_text

        for i in range(len(input_rects)):
                pygame.draw.rect(win, WHITE, input_rects[i])
                text_surface = my_font.render(ObjectData[i], True, BLACK)
                win.blit(text_surface, (input_rects[i].x+1, input_rects[i].y+1)) 
