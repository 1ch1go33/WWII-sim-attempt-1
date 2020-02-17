import pygame
import time
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
LoadGameB = pygame.image.load(r'LoadGame.png')
StartGameB = pygame.image.load(r'StartGame.png')
TitleScreenStalin = pygame.image.load(r'images\wwII_3.png')
TitleScreenHitler = pygame.image.load(r'images\wwII_1.png')
#TitleScreenFDR = pygame.image.load(r'')
#initiate the pygame window
Screen = pygame.display.set_mode((width, height))

# set the pygame window name
pygame.display.set_caption('World War II simulator')

image = pygame.image.load(r'images\BlackSquare.png')#insert file path and image name
SpriteList=[image, StartGameB, LoadGameB]
Background=TitleScreenStalin
#def LoadSprites():
    #for sprite in SpriteList:
      #  Screen.blit(sprite, (0,0))

def DrawSprites():
    global Background
    global SpriteList
    for sprite in SpriteList:
        Screen.blit(Background, (0,0))
        Screen.blit(sprite, (0, 0))
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
    pygame.event.pump()
    TimeDelay += 1
    if TimeDelay >= 5000:
        TimeDelay=0
    return TimeDelay
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
       # time.sleep(5)
        #Background=TitleScreenHitler
        #DrawSprites()
        #time.sleep(5)
        Events()
        
       # Screen.blit(TitleScreenThree, (0,0))
        #time.sleep(5)

def RunGame():
# conditional loop
    while war==True :

        # completely fill the surface object
        Screen.fill(white)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
        Screen.blit(image, (0, 0))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
        for event in pygame.event.get() :

        # if event object type is QUIT
        # then quitting the pyame
        # and program both.
            if event.type == pygame.QUIT :

            # deactivates the pygame library
                pygame.quit()

            # quit the program. /
                quit()

        # Draws the surface object to the screen.
        pygame.display.update()

StartGame()


