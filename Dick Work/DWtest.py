import pygame 
import numpy as np
import DWfuncs as fun
pygame.init()

#colors
bak_color = (100,200,0)
red=(200,0,0)
jo_color=(165,42,42)
blue = (100,100,200)
white = (220,220,220)
menu_color = (10,20,50)

#screen demensions
screen_height=600
screen_width=1200

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen_width,screen_height))

#main game
game = True
while game:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    #create points
    side1 = (screen_width/3,screen_height/3),(screen_width*2/3,screen_height/3),(screen_width*2/3,screen_height*2/3),(screen_width/3,screen_height*2/3)
    
    #draw shapes
    pygame.draw.polygon(display, jo_color, side1)
    
    #update screen
    pygame.display.update()
    
    #quite
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update()
