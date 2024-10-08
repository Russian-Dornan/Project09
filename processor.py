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

    massive[0],massive[1],massive[3],massive[4] = walls.Reverse(massive[0],massive[1],massive[3],massive[4])

    result=collision.IsCollied(massive, n)
    if result==0:
        None
    # elif result==1:#столкновение с верхней и нижней стенкой
    #     massive[4], massive[1]=walls.Reverse(massive[4], massive[1]);
    # elif result==2: # Столкновение с правой и левой стенкой
    #     massive[3], massive[0] = walls.Reverse(massive[3], massive[0])

    elif result>10: # Столкновение объектов верхом
        massive[4], massive[1] = impuls.SpeedCalculate_y(massive[4], massive[1], result//10);
    elif result<-10:
        massive[3], massive[0] = impuls.SpeedCalculate_x(massive[3], massive[0], result//(-10))

    if(par.GravityType==1):
        massive[4]=gravity.EarthGravity(massive[4]);
    elif(par.GravityType==2):
        massive[3], massive[4] = gravity.SpaceGravity(massive[0], massive[1], massive[3], massive[4], massive[5])

    massive[0], massive[1] = mooving.ChangePosition(massive[0], massive[1], massive[3], massive[4]);

    item[n]=massive