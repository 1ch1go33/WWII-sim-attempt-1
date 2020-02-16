import pygame
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
#assign several in game variables
white = (255, 255, 255)
black= (0,0,0)
width = 400  #change these two to fit game
height = 400
war=True
allies=[]
enemies=[]
neutral=[]
TitleScreenOne = pygame.image.load(r'')
TitleScreenTwo = pygame.image.load(r'')
TitleScreenThree = pygame.image.load(r'')
#initiate the pygame window
Screen = pygame.display.set_mode((width, height))

# set the pygame window name
pygame.display.set_caption('World War II simulator')

image = pygame.image.load(r'images\BlackSquare.png')#insert file path and image name
SpriteList=[image]
#def LoadSprites():
    #for sprite in SpriteList:
      #  Screen.blit(sprite, (0,0))
def StartGame():
    while war==False:
        #cycles through the different title screens
        Screen.blit(TitleScreenOne, (0,0))
        time.sleep(5)
        Screen.blit(TitleScreenTwo, (0,0))
        time.sleep(5)
        Screen.blit(TitleScreenThree, (0,0))
        time.sleep(5)

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
RunGame()
