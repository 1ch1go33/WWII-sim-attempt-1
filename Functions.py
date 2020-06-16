import pygame
Click = False
MiddleClick = False
RightClick = False
def Mouse(Coord): #     Tells you where the mouse is
    CoordVal = 'n/a'
    if Coord == ('X'):
        CoordVal = pygame.mouse.get_pos()[0]
    if Coord == ('Y'):
        CoordVal = pygame.mouse.get_pos()[1]
    return CoordVal

def MouseDetect():
    global Click
    global MiddleClick
    global RightClick
    Click = False
    MiddleClick = False
    RightClick = False
    g=pygame.mouse.get_pressed()
    if g[0] == 1:
        Click = True
    if g[1] == 1:
        MiddleClick = True
    if g[2] == 1:
        RightClick = True

