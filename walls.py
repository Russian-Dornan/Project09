#Суорость должна меняться на противоположную, в стенках не должен объект застревать
def Reverse(speed, pos_x, pos_y):
    if (pos_x == 0) or (pos_y == 0) or (pos_x == 1050) or (pos_y == 700):
        speed == (-1) * speed
    return speed, pos_x, pos_y