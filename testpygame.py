import pygame 
  
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
#assign several in game variables
white = (255, 255, 255) 
black= (0,0,0)
wi = 400  #change these two to fit game
height = 400
war==True
allies=[]
enemies=[]
neutral=[]
#initiate the pygame window
screen = pygame.display.set_mode((width, height)) 
  
# set the pygame window name 
pygame.display.set_caption('World War II simulator') 

image = pygame.image.load(r'')#insert file path and image name
  
# conditional loop
while war==True : 
  
    # completely fill the surface object 
    display_surface.fill(white) 
  
    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    display_surface.blit(image, (0, 0)) 
  
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen.   
        pygame.display.update()  
             
