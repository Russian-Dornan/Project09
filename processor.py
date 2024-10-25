import impuls
import walls
import parameters as par
import gravity
import mooving
import collision

# 1:[x, y, size, Speed_x, Speed_y, mass, Color, ]
# 1:[0, 1,   2 ,   3    ,    4   ,   5 ,   6    ]

def Item_Update(item, n):
    massive=item[n]
    if(par.GravityType!=2):
        massive[0],massive[1],massive[3],massive[4] = walls.Reverse(massive[0],massive[1],massive[2],massive[3],massive[4])

    result=collision.IsCollied(n, item)
    if result==0:
        None
    elif result>10: # Столкновение объектов верхом

        massive[4], massive[1] = impuls.SpeedCalculate_y(n, result//10, item);

    elif result<-10:

        massive[3], massive[0] = impuls.SpeedCalculate_x(n, result//(-10), item)

    if(par.GravityType==1):
        massive[4]=gravity.EarthGravity(massive[4]);
    elif(par.GravityType==2):
        massive[3], massive[4] = gravity.MultiGravity(n, item)

    massive[0], massive[1] = mooving.ChangePosition(massive[0], massive[1], massive[3], massive[4]);

    item[n]=massive
