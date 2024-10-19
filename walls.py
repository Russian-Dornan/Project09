#Суорость должна меняться на противоположную, в стенках не должен объект застревать
from parameters import *
import processor as proc
def Reverse(x,y,size,speed_x,speed_y):
    if (x == 0) or (x == (wide-size-otstup)):
        speed_x = (-1) * speed_x
    elif (y == 0) or (y == (hight-size)):
        speed_y = (-1) * speed_y
    return x,y,speed_x,speed_y
