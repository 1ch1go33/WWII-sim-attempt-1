import pygame
import random
import math
import os
import sys
import Functions as Fun
import Objects as Obj
import Images as Img
X=0
Y=0
Background = Img.sUSBackground
Width = 1000
Height = 600
Game = False
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('WWII Simulator')
Black = (0,0,0)
White = (255,255,255)

################           This is where important functions go


def Events():                          # Handles inputs from keyboard, mouse, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


###############              This part is the game loop
def PlayGame():
    global Screen
    global White
    global Black
    global Game
    global Background
    Game = True

    while Game == True:
        Events()
        Fun.MouseDetect()
        Screen.fill(Black)
        Screen.blit(Background, (0,0))
PlayGame() 