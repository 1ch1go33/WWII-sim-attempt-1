import pygame
import random
import math
import os
<<<<<<< HEAD:DefinetlyAttemptOneMainScript.py
import TitleScreen as TS
import ObjectDefinitionsGame as OBJ
X=0
Y=0
Width = 1280
Height = 720
=======
import sys
import Functions as Fun
import Objects as Obj
import Images as Img
X=0
Y=0
Background = Img.sUSBackground
Width = 1000
Height = 600
>>>>>>> 8fb3a49e7f3d8b18ba5b9f257785c51a421310d7:Definetly Attempt One Main Script.py
Game = False
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('WWII Simulator')
Black = (0,0,0)
White = (255,255,255)
<<<<<<< HEAD:DefinetlyAttemptOneMainScript.py
Zoom = 1
Scroller = 0
#What is multiplyed to get the right size for different resolutions
ResCon = 1
OceanBackground = pygame.image.load(r'images\black.jpg')

=======
################           Big lists and variables
SpriteList = []
>>>>>>> 8fb3a49e7f3d8b18ba5b9f257785c51a421310d7:Definetly Attempt One Main Script.py
################           This is where important functions go


def Events():                          # Handles inputs from keyboard, mouse, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
<<<<<<< HEAD:DefinetlyAttemptOneMainScript.py
            pygame.quit
            sys.exit
def Display():
    pygame.event.pump()
    for i in OBJ.CurrentImages:
        Screen.blit(i.Img,(i.X + Scroller,i.Y + Scroller))
    pygame.display.update()    
        
def Adjust():
    for i in OBJ.Map:
        pygame.transform.rotozoom(i.Img, 0, Zoom)
=======
            pygame.quit()
            sys.exit()

>>>>>>> 8fb3a49e7f3d8b18ba5b9f257785c51a421310d7:Definetly Attempt One Main Script.py

###############              This part is the game loop
def PlayGame():
    global Screen
    global White
    global Black
    global Game
<<<<<<< HEAD:DefinetlyAttemptOneMainScript.py
    Map1 = OBJ.Region(0-Width,Height,OceanBackground)
    Map2 = OBJ.Region(0,Height,OceanBackground)
    Map3 = OBJ.Region(0+Width,Height,OceanBackground)
    print(OBJ.CurrentImages)
=======
    global Background
>>>>>>> 8fb3a49e7f3d8b18ba5b9f257785c51a421310d7:Definetly Attempt One Main Script.py
    Game = True

    while Game == True:
        
        Events()
<<<<<<< HEAD:DefinetlyAttemptOneMainScript.py
        #MouseClick()
        Display()
        #Adjust()
    
PlayGame()
=======
        Fun.MouseDetect()
        Screen.fill(Black)
        Screen.blit(Background, (0,0))

PlayGame() 
>>>>>>> 8fb3a49e7f3d8b18ba5b9f257785c51a421310d7:Definetly Attempt One Main Script.py
