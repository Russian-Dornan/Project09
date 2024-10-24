
import parameters as par
# Реализуй расчет скорости, не забудь обновить скорость у объекта, с  которым столкнулся
# Пример реализации item.update({nomber:[item[x, y, speedX....]]})
#Формулы для упругого
#U_x - скорость объекта который врезался, U_x2 - вес объекта в которого врезались
#weight - вес объекта который врезался, weight2- вес объекта в которого врезались
#Ux - изначальная скорость объекта который врезался, Ux2 - изначальная скорость объекта в которого врезались

#U_x = (((weight - weight2) * Ux + 2 * weight2 * Ux2) / (weight + weight2))
#U_x2 =((2 * weight * Ux + (weight2 - weight) * Ux2) / (weight2 + weight))

#item={nomber: [положение по x, положение по y, длина стороны, скорость по x,  скорость по  y, масса, цвет(в формате RGB)
def SpeedCalculate_x(nomber, nomber2, item):

    weight1 = item[nomber][5]
    weight2 = item[nomber2][5]
    Ux1 = item[nomber][3]
    Ux2 = item[nomber2][3]
    Ux=0
    if par.ImpulsType == 1:  # Упругий удар
        Ux1f = (((weight1 - weight2) * Ux1 + 2 * weight2 * Ux2) / (weight1 + weight2))
        Ux2f = ((2 * weight1 * Ux1 + (weight2 - weight1) * Ux2) / (weight1 + weight2))

        #item[nomber][3] = Ux1
        item[nomber2][3] = Ux2f
        return Ux1f, item[nomber][0]
    elif par.ImpulsType == 2:  # Неупругий удар
        Ux = (weight1 * Ux1 + weight2 * Ux2) / (weight1 + weight2)

        #item[nomber][3] = Ux
        item[nomber2][3] = Ux/100

    #return item[nomber][0], item[nomber2][0], item[nomber][3], item[nomber2][3]
        return Ux/100, item[nomber][0]

def SpeedCalculate_y(nomber, nomber2, item):
    weight1 = item[nomber][5]
    weight2 = item[nomber2][5]

    Uy1 = 100*item[nomber][4]
    Uy2 = 100*item[nomber2][4]

    if par.ImpulsType == 1:  # Упругий удар
        Uy1f = (((weight1 - weight2) * Uy1 + 2 * weight2 * Uy2) / (weight1 + weight2))
        Uy2f = ((2 * weight1 * Uy1 + (weight2 - weight1) * Uy2) / (weight1 + weight2))

        #item[nomber][4] = Uy1

        item[nomber2][4] = Uy2f/100


        return Uy1f/100, item[nomber][1]

    elif par.ImpulsType == 2: # Неупругий удар
        Uy = (weight1 * Uy1 + weight2 * Uy2) / (weight1 + weight2)

        #item[nomber][4] = Uy
        item[nomber2][4] = Uy/100

        return Uy/100, item[nomber][1]

