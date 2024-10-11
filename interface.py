import draw
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
def MainMenu(win, font):
        Main_Menu_Buttons = [
                [
                        [
                                draw.GetButton(975, 10, 107.5, 107.5, 'Добавить бъект', win, font),
                                draw.GetButton(1092.5, 10, 107.5, 107.5, 'Импорт сценария', win, font),
                                draw.GetButton(975, 127.5, 107.5, 107.5, 'Настройки физики', win, font),
                                draw.GetButton(1092.5, 127.5, 107.5, 107.5, 'Настройки приложения', win, font),
                                draw.GetButton(975, 245.0, 107.5, 107.5, 'Экстра функции', win, font),
                                draw.GetButton(1092.5, 245.0, 107.5, 107.5, 'Выбрать объект', win, font),
                                draw.GetButton(975, 362.5, 107.5, 107.5, 'Следовать', win, font)
                        ]
                ]
        ]

        return Main_Menu_Buttons