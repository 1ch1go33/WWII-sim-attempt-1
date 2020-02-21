import pygame
import time
import math
import os
from array import *
pygame.init()

white = (255, 255, 255)
black= (0,0,0)
width = 1000  #change these two to fit game
height = 600
war=False
allies=[]
enemies=[]
neutral=[]
#Objects = array('i', [1, 2, 3,]) this needs further testing
Objects = []#inside of each object, have an x, y, width, and height
#example = Objects = [[600, 420, 300, 100], [150, 420, 300, 100]]
#use for loop to find out where mouse is and where clickable box is
TimeDelay = 0
WallpaperCycle = 0
#whenever you load an image, put a comment of the dimensions right next to it
LoadGameB = pygame.image.load(r'images\LoadGame.png') #(300, 100)
StartGameB = pygame.image.load(r'images\StartGame.png') #(300, 100)
TitleScreen = pygame.image.load(r'images\WorldWarIITitleScreen.png') #(600, 1000)
TitleScreenStalin = pygame.image.load(r'images\wwII_3.png') #(600, 1000)
TitleScreenHitler = pygame.image.load(r'images\wwII_1.png') #(600, 1000)
LoadGameR= LoadGameB.get_rect(topleft=(600, 420))
#TitleScreenFDR = pygame.image.load(r'')
#initiate the pygame window
Screen = pygame.display.set_mode((width, height))

# set the pygame window name
pygame.display.set_caption('World War II simulator')


SpriteList={StartGameB:(150, 420), LoadGameB:(600, 420), TitleScreen:(280, 100)}
Background=TitleScreenStalin
#def LoadSprites():
    #for sprite in SpriteList:
      #  Screen.blit(sprite, (0,0))

def StartGame():
    global Objects
    global TitleScreenHitler
    global TitleScreenStalin
    global LoadGameB
    global StartGameB
    global Background
    global WallpaperCycle
    Objects.append([150, 420, 300, 100])
    Objects.append([600, 420, 300, 100])
    while war==False:
        pygame.time.delay(1)
        if Tick()==0:
            if WallpaperCycle < 3:
                WallpaperCycle += 1 
            else:
                WallpaperCycle = 1
            if WallpaperCycle == 1:
                Background = TitleScreenHitler
            elif WallpaperCycle == 2:
                Background = TitleScreenStalin
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for j in Objects:
                    print("no")
        #cycles through the different title screens
        DrawSprites()
        Events()
        
       # Screen.blit(TitleScreenThree, (0,0))
        #time.sleep(5)
def MousePos(coord):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if coord == 'x':
                ret = pygame.mouse.get_pos()[0]
                return ret
            elif coord =='y':
                ret = pygame.mouse.get_pos()[1]
                return ret
def DrawSprites():
    LoadAndStart = True
    global Background
    global SpriteList
    pygame.event.pump()
    Screen.blit(Background, (0,0))
    Screen.blit(LoadGameB, SpriteList.get(LoadGameB))
    Screen.blit(StartGameB, SpriteList.get(StartGameB))
    Screen.blit(TitleScreen, SpriteList.get(TitleScreen))
    pygame.display.update()
def Events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            hx=6
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hx=6
        elif event.type == pygame.MOUSEMOTION:
            hx=6
def Tick():
    global TimeDelay
    TimeDelay += 1
    if TimeDelay >= 1000:
        TimeDelay=0
    return TimeDelay

def RectangleHitBox(x, y, w, h):
    
    return [x, y, w, h]

StartGame()


