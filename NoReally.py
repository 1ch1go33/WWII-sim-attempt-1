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
Classes = []
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

    def __init__(self, x, y, img, showing):
        self.x = x
        self.y = y
        self.img = img[0]
        self.showing = True
        Classes.append(self)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Actions:

    def __init__(self, x, y, width, height, img, showing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img[0]
        self.showing = False
        Classes.append(self)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class WorldMap:


    def __init__(self, x, y, img, showing):
        self.x = x
        self.y = y
        self.img = img[0]
        self.showing = False
        Classes.append(self)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Country:

    def __init__(self, population, money, working, armysize, landsize, food):
        self.population = population
        self.money = money
        self.working = working
        self.armysize = armysize
        self.landsize = landsize
        self.food = food

def Draw(self):
    for i in Classes:
        if (Classes[i].showing):
            pygame.event.pump()
            Screen.blit(Classes[i], ((Classes[i].x),(Classes[i].y))
            pygame.display.update()

def Main():
    pass