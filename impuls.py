
import parameters as par
# Реализуй расчет скорости, не забудь обновить скорость у объекта, с  которым столкнулся
# Пример реализации item.update({nomber:[item[x, y, speedX....]]})
#Формулы для упругого,
#U_x = (((weight - weight2) * Ux + 2 * weight2 * Ux2) / (weight + weight2))
#U_x2 =((2 * weight * Ux + (weight2 - weight) * Ux2) / (weight2 + weight))
def SpeedCalculate_x(x, Speed_x, nomber): #Позиция столкновения, скорость до столкновения, номер с которым столкнулся, тип столкновения(0-по оси x, 1-по оси y)

    if(par.ImpulsType==1):
        ...
    elif(par.ImpulsType==2):
        ...


    return Speed_x, x


def SpeedCalculate_y(y, Speed_y, nomber):

    if (par.ImpulsType == 1):
        ...
    elif (par.ImpulsType == 2):
        ...

    return Speed_y, y