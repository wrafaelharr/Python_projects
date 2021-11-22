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

#start positions
dick_x=int(screen_width /2)
dick_y=int(screen_height /2)
ball_x=int(screen_width*np.random.rand())
ball_y=int(screen_height*np.random.rand())
bady_x = int(screen_width*np.random.rand())
bady_y = int(screen_height*np.random.rand())
bady_ang = 2*np.pi*np.random.rand()
nut_x = []
nut_y = []
nut_ang = []


#start demensions
ball_radius=7
ball_wall=7
balls_radius=3
dick_length = 14 
dick_gerth = 6
nut_radius = 5
bady_radius = 10

#stats
move=10
bady_speed = 3
nut_speed = 3

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen_width,screen_height))
        
#fun.menu_func()

#main game
game = True
while game:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    #create points
    side1 = (dick_x-dick_gerth/2,dick_y),(screen_width*2/3,screen_height/3),(screen_width*2/3,screen_height*2/3),(screen_width/3,screen_height*2/3)
    
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
