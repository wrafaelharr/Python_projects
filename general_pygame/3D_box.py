import pygame
import numpy as np
pygame.init()

#screen demensions
screen_height = 600
screen_width = 1200

#colors
jo_color = (100,100,200)
fu_color = (200,100,100)
bak_color = (130,0,130)
ground_color = (80,0,0)
black = (0,0,0)

#start cube orientations
angle_x = 0
angle_y = 0

#cube demensions
cube_size = 100

#gimme
the_Nword = 'nuggut'
i = 0

#main game
cube = True
while cube:
    keys = pygame.key.get_pressed()
    #create display
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    #time
    i = i+0.05
    if i > 12:
        i = 0
      
    angle_x = np.pi*i/6
    angle_y = np.pi*i/6
    
    #rotate top
    corner_x = []
    corner_y = []
    cornerB_x = []
    cornerB_y = []
    for n in range(4):
        corner_x.append(np.cos(angle_x+np.pi*n/2)*cube_size+screen_width/2)
        corner_y.append(np.sin(angle_x+np.pi*n/2)*cube_size/2+screen_height/2-cube_size*3/4)
        cornerB_x.append(np.cos(angle_x+np.pi*n/2)*cube_size+screen_width/2)
        cornerB_y.append(np.sin(angle_x+np.pi*n/2)*cube_size/2+screen_height/2+cube_size*3/4)
    
    top = (corner_x[0],corner_y[0]),(corner_x[1],corner_y[1]),(corner_x[2],corner_y[2]),(corner_x[3],corner_y[3])
    side1 = (corner_x[3],corner_y[3]),(corner_x[2],corner_y[2]),(cornerB_x[2],cornerB_y[2]),(cornerB_x[3],cornerB_y[3])
    side2 = (corner_x[1],corner_y[1]),(corner_x[0],corner_y[0]),(cornerB_x[0],cornerB_y[0]),(corner_x[1],cornerB_y[1])
    bottom = (cornerB_x[0],cornerB_y[0]),(corner_x[1],cornerB_y[1]),(cornerB_x[2],cornerB_y[2]),(cornerB_x[3],cornerB_y[3])
    
    #draw shape
    pygame.draw.polygon(display, ground_color, bottom)
    if angle_x > 0 and angle_x < np.pi:
        pygame.draw.polygon(display, fu_color, side1)
        pygame.draw.polygon(display, jo_color, side2)
    else:
        pygame.draw.polygon(display, jo_color, side2)
        pygame.draw.polygon(display, fu_color, side1)
    pygame.draw.polygon(display, ground_color, top)
    
    #update screen
    pygame.display.update()
    
    #make the game quit properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update()
    