from parameters import *
import math
def EarthGravity(Speed_y):
    Speed_y += g/100000
    return Speed_y
def MultiGravity(nomber, item):

    Uy = item[nomber][4]
    Ux = item[nomber][3]
    x, y, wide, hight = item[nomber][0], item[nomber][1], item[nomber][2], item[nomber][2]
    x = (x + wide / 2)
    y = (y + hight / 2)
    g_x = 0
    g_y = 0
    for i in item:

        if i != nomber:
            weight2 = item[i][5]
            x2, y2, wide2, hight2 = item[i][0], item[i][1], item[i][2], item[i][2]
            x2 = (x2 + wide2 / 2)
            y2 = (y2 + hight2 / 2)
            g_y_now = 0
            g_x_now = 0
            if i == -100:
                if abs(x - x2) > 1:
                    g_x_now = G * weight2 / ((x - x2) * (x - x2))
                else:
                    g_x_now = 0
                if abs(y - y2) > 1:
                    g_y_now = G * weight2 / ((y - y2) * (x - x2))
                else:
                    g_y_now = 0
                g_x += g_x_now
                g_y = g_y_now
                if g_x_now > 1:
                    print(g_x_now)
            if i != -1000:
                b = (x2 - x)
                a = (y2 - y)
                c = math.hypot((x2 - x), (y2 - y))
                try:
                    an_x = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
                except:
                    an_x = 0
                try:
                    an_y = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
                except:
                    an_y = 0

                g = G * weight2 / (c ** 2)
                g_x_now = g * math.cos(an_x)
                g_y_now = g * math.cos(an_y)
                g_x += g_x_now
                g_y += g_y_now
    Ux += g_x
    Uy += g_y
    return Ux, Uy