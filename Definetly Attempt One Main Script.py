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
            pygame.quit
            sys.exit
            sys.just_kinda_stop # for some reason .exit isn't working, so i wrote a line that causes an error and closes the program. obviously a dumb solution but for now it works

###############              This part is the game loop
def PlayGame():
    global Game
    Game = True
    while Game == True:
        Events()
        Fun.MouseDetect()
PlayGame()