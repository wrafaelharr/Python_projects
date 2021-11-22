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

#demensions
ground_height = 150
rect_width = 10
rect_height = 5

#start positions
ground_x = 0
ground_y = screen_height-ground_height
rect_x = screen_width/5
rect_y = ground_y-rect_height

#start phisics
rect_force = 0
rect_vel = 0

while True:
    
    pygame.display.set_caption('pong')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    while True:
        #reset screen
        display.fill(bak_color)
        
        #buttons
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            rect_force = rect_force+3
        elif keys[pygame.K_LEFT]:
            rect_force = rect_force-3
        else:
            rect_force = 0
        
        #acceleration
        rect_vel = rect_vel + 0.2*rect_force
        rect_x = rect_x+rect_vel
        print(rect_force,rect_vel,rect_x)
        
        #air friction
        rect_vel = rect_vel*np.e**(-np.absolute(rect_vel)*0.001)
        rect_force = rect_force*np.e**(-np.absolute(rect_vel)*0.01)
        
        #loop the walls
        if rect_x > screen_width+rect_width*4:
            rect_x = 0-rect_width*3
        elif rect_x < -rect_width*4:
            rect_x = screen_width+rect_width*4
        
        #draw proscribed shapes
        #pygame.draw.circle(display, fu_color, (ball_x, ball_y), ball_radius, ball_wall)
        pygame.draw.rect(display, ground_color, (ground_x, ground_y, screen_width, screen_height))
        pygame.draw.rect(display, jo_color, (rect_x, rect_y, rect_width, rect_height))
        
        #update screen
        pygame.display.update()
        
        #reset screen
        pygame.time.delay(30)
        display.fill(bak_color)
        
        #quit properly
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()