#Суорость должна меняться на противоположную, в стенках не должен объект застревать
from parameters import *
def Reverse(x,y,speed_x,speed_y):
    if (x == 0) or (x == (wide-massive[3])):
        speed_x = (-1) * speed_x
    elif (y == 0) or (y == (hight-massive[3])):
        speed_y = (-1) * speed_y
    return x,y,speed_x,speed_y
