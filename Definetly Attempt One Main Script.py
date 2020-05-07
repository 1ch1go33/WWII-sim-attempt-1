import pygame
import random
import math
import os
X=0
Y=0
Width = 1000
Height = 600
Game = False
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('WWII Simulator')
Black = (0,0,0)
White = (255,255,255)

################           This is where important functions go

def Mouse(Coord): #     Tells you where the mouse is
    CoordVal = 'n/a'
    if Coord == ('X'):
        CoordVal = pygame.mouse.get_pos()[0]
    if Coord == ('Y'):
        CoordVal = pygame.mouse.get_pos()[1]
    return CoordVal
def MouseClick():
    g=pygame.mouse.get_pressed()
    print(g)


def Events():                          # Handles inputs from keyboard, mouse, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit
###############              This part is the game loop
def PlayGame():
    global Game
    Game = True
    while Game == True:
        Events()
        MouseClick()
PlayGame()