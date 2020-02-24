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
#whenever you load an image, put a comment of the dimensions right next to it
LoadGameB = [pygame.image.load(r'images\LoadGame.png')] #(300, 100)
StartGameB = [pygame.image.load(r'images\StartGame.png')] #(300, 100)
TitleScreen = [pygame.image.load(r'images\WorldWarIITitleScreen.png')] #(600, 1000)
TitleScreens = [pygame.image.load(r'images\wwII_3.png'), pygame.image.load(r'images\wwII_1.png')] #(600, 1000)

#TitleScreenFDR = pygame.image.load(r'')
#initiate the pygame window
Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('World War II simulator')


#SpriteDict={StartGameB:StartGameR, LoadGameB:LoadGameR}

Background=TitleScreens[0]

class Wallpaper:
    #time between each cycle
    BackgroundCycle = 5
    Showing = True

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img[0]

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Actions:

    Showing = False

    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img[0]

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class WorldMap:

    Showing = False

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img[0]

    def get_mask(self):
        return pygame.mask.from_surface(self.img)