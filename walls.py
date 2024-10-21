#Суорость должна меняться на противоположную, в стенках не должен объект застревать
from parameters import *
import processor as proc
def Reverse(x,y,size,speed_x,speed_y):
    if (x <= 0):
        x=0.3
        speed_x = (-1) * speed_x
    elif(x>=wide-size-otstup):
        x=wide-size-0.3-otstup
        speed_x = (-1) * speed_x
    if (y <= 0):
        y = 0.3
        speed_y = (-1) * speed_y
    elif (y >= hight - size):
        y = hight - size - 0.3
        speed_y = (-1) * speed_y
    return x,y,speed_x,speed_y
