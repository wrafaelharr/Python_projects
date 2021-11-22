import pygame
import numpy as np
pygame.init()

def rote_to_xy(start_y,start_x,start_z,size,angle1,angle2):
    point_x = start_y - size*np.sin(angle1)
    radius_xz = size*np.cos(angle1)
    point_y = radius_xz * np.cos(angle2)+start_x
    point_z = radius_xz * np.sin(angle2)+start_z
    return point_x, point_y

def rote_to_yx(start_x,start_y,start_z,size,angle1,angle2):
    point_y = start_y - size*np.sin(angle1)
    radius_xz = size*np.cos(angle1)
    point_x = radius_xz * np.cos(angle2)+start_x
    point_z = radius_xz * np.sin(angle2)+start_z
    return point_x, point_y

#screen demensions
screen_height = 600
screen_width = 1200

#colors
jo_color = (100,100,200)
fu_color = (200,100,100)
shrew_color = (100,200,100)
bak_color = (130,0,130)
ground_color = (80,0,0)
black = (0,0,0)

#start cube orientations and position
box_ang1 = 0
box_ang2 = np.pi*1.5
box_x = screen_width/2
box_y = screen_height/2
box_z = 0

#cube demensions
box_size = 100

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
    
    #change angles
    #box_ang1 = box_ang1 + 0.05
    box_ang2 = box_ang2 + 0.05
    
    #diognostics
    pygame.draw.circle(display, shrew_color, (int(screen_width/2), int(screen_height/2)),30, 30)
    
    #loop box angs
    if box_ang1 < 0:
        box_ang1 = 2*np.pi
    elif box_ang1 > 2*np.pi:
        box_ang1 = 0
    elif box_ang2 < 0:
        box_ang2 = 2*np.pi
    elif box_ang2 > 2*np.pi:
        box_ang2 = 0
    
    #make a cube
    points = []
    for i in range(8):
        if i <= 3:
            points.append(rote_to_yx(rote_to_xy(box_x,box_y,box_z,box_size,np.pi/4+box_ang1,np.pi*i/2+box_ang2)+(box_z,box_size,np.pi/4+box_ang1,np.pi*i/2+box_ang2)))
        else:
            points.append(rote_to_yx(rote_to_xy(box_x,box_y,box_z,box_size,-np.pi/4+box_ang1,np.pi*i/2+box_ang2))+(box_z,box_size,-np.pi/4+box_ang1,np.pi*i/2+box_ang2))
            
    
    print(box_ang2)
    top = points[:4]
    side1 = points[2],points[3],points[7],points[6]
    side2 = points[0],points[1],points[5],points[4]
    bottom = points[4:]
    
    #draw shape
    pygame.draw.polygon(display, ground_color, bottom)
    if box_ang2 < np.pi and box_ang2 > 0:
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
    