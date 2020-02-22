import pygame
import time
import math
import os
#from array import *
pygame.init()

white = (255, 255, 255)
black= (0,0,0)
width = 1000  #change these two to fit game
height = 600
war=False
allies=[]
enemies=[]
neutral=[]
TimeDelay = 0
WallpaperCycle = 0
#whenever you load an image, put a comment of the dimensions right next to it
LoadGameB = pygame.image.load(r'images\LoadGame.png') #(300, 100)
StartGameB = pygame.image.load(r'images\StartGame.png') #(300, 100)
TitleScreen = pygame.image.load(r'images\WorldWarIITitleScreen.png') #(600, 1000)
TitleScreenStalin = pygame.image.load(r'images\wwII_3.png') #(600, 1000)
TitleScreenHitler = pygame.image.load(r'images\wwII_1.png') #(600, 1000)
#TitleScreenFDR = pygame.image.load(r'')
#initiate the pygame window
Screen = pygame.display.set_mode((width, height))
# set up hitboxes
LoadGameR= LoadGameB.get_rect(topleft=(600, 420))
StartGameR= StartGameB.get_rect(topleft=(150,420))
# set the pygame window name
pygame.display.set_caption('World War II simulator')


SpriteList={StartGameB:StartGameR, LoadGameB:LoadGameR}

Background=TitleScreenStalin


def StartGame():
    global TitleScreenHitler
    global TitleScreenStalin
    global LoadGameB
    global StartGameB
    global Background
    global WallpaperCycle
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
        #cycles through the different title screens
        DrawSprites()
        Events()


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
#    LoadAndStart = True
    global Background
    global SpriteList
    #pygame.event.pump()
    Screen.blit(Background, (0,0))
    for item in SpriteList:
        rect=SpriteList.get(item)
        coords=(rect[0],rect[1])
        Screen.blit(item, coords)
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


