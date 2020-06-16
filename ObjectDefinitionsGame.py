import pygame

Width = 1280
Height = 720

CurrentImages = []
Map = []

class Button:
    def DetectMouse(self):
        #if (X == self.X) and (Y == self.Y):   this isn't done yet
            print('mouse is yes')

class Region:

    def __init__(self,X,Y,Img):
        self.X = X
        self.Y = Y
        self.Img = Img
        CurrentImages.append(self)
        Map.append(self)

LeftScroll = pygame.Rect(0,0,250,Height)
RightScroll = pygame.Rect(Width-250,0,250,Height)
