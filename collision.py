import pygame

def IsCollied(n, item):
    global regim

    x, y, wide, hight, Ux, Uy, weight = item[n][0], item[n][1], item[n][2], item[n][2], \
    item[n][2], item[n][5], item[n][6]
    # ITEM_X = pygame.Rect(x + wide // 2 - 3, y, wide // 2, hight)
    # ITEM_Y = pygame.Rect(x, y + hight // 2 - 3, wide, hight // 2)
    ITEM_X = pygame.Rect(x + wide * 0.1, y, wide - wide * 0.2, hight)
    ITEM_Y = pygame.Rect(x, y + hight * 0.1, wide, hight - hight * 0.2)

    for i in item:
        if i != n:

            reht = pygame.Rect(item[i][0], item[i][1], item[i][2], item[i][2])
            if ITEM_Y.colliderect(reht) == True:

                return i*(-10)
            if ITEM_X.colliderect(reht) == True:

                return i*10

    return 0