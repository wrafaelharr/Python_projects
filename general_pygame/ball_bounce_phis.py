import pygame
import numpy
pygame.init()

#funcs
#def angle_refl(force_):
    

#colors
jo_color = (100,100,200)
fu_color = (200,100,100)
bak_color = (130,0,130)
ground_color = (80,0,0)
black = (0,0,0)

#averages
force_avg = []
accel_avg = []

#start demensions
screen_height = 600
screen_width = 1200
ground_height = 150
ground_width = screen_width
ball_radius = 30
ball_wall = 30
pionter_width = 10
pionter_height = 10
pionter_dist = 50
pionter_angle = numpy.pi/2

#start phis
ball_mass = 30
ball_force_y = 0
ball_force_x = 0
ball_accel_y = 0
ball_accel_x = 0
ball_vel_y = 0
ball_vel_x = 0
ball_force = 0


#start positions
ground_x = 0
ground_y = screen_height-ground_height
ball_y = 200
ball_x = 800
pionter_x = ball_x-pionter_width/2
pionter_y = ball_y
delta_pionter_y = 0
delta_pionter_x = 0

#main game
run = True
while run:
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    
    game = True
    while game:
        #dellay and screen reset
        pygame.time.delay(30)
        display.fill(bak_color)
        
        #pionter placement
        delta_pionter_y = numpy.sin(pionter_angle)*ball_radius
        delta_pionter_x = numpy.cos(pionter_angle)*ball_radius
        pionter_x = ball_x-int(numpy.round(delta_pionter_x))
        pionter_y = ball_y-int(numpy.round(delta_pionter_y))
        
        
        #controlls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            #if numpy.cos(pionter_angle)>0:
            pionter_angle = pionter_angle - numpy.pi/10
            #if numpy.cos(pionter_angle)<=0:
                #pionter_angle = pionter_angle + numpy.pi/10
        if keys[pygame.K_DOWN]:
            #if numpy.cos(pionter_angle)>0:
            pionter_angle = pionter_angle - numpy.pi/10
            #if numpy.cos(pionter_angle)<=0:
                #pionter_angle = pionter_angle + numpy.pi/10
        if keys[pygame.K_RIGHT]:
            if numpy.sin(pionter_angle)>0:
                pionter_angle = pionter_angle + numpy.pi/10
            if numpy.sin(pionter_angle)<=0:
                pionter_angle = pionter_angle - numpy.pi/10
        if keys[pygame.K_LEFT]:
            if numpy.sin(pionter_angle)>0:
                pionter_angle = pionter_angle - numpy.pi/10
            if numpy.sin(pionter_angle)<=0:
                pionter_angle = pionter_angle + numpy.pi/10
        if keys[pygame.K_SPACE]:
            ball_force = ball_force + 1
        
        print(ball_y)
        
        
        #set ground interactions
        if ball_y+ball_radius>ground_y+0.25*ball_radius:
            ball_vel_y = ball_vel_y-0.5
        elif ball_y+ball_radius>ground_y:
            ball_vel_y = -ball_vel_y*0.5
            ball_vel_x = ball_vel_x*0.3
            if ball_vel_x>0:
                ball_vel_x = ball_vel_x - 0.1
            if ball_vel_x<0:
                ball_vel_x = ball_vel_x + 0.1
            
        #gravity
        ball_vel_y = ball_vel_y + 0.2
        
        #make the ball bounce
        
        
        #physics for ball
        ball_force_y = int(numpy.round(numpy.sin(pionter_angle)*ball_force))
        ball_force_x = int(numpy.round(numpy.cos(pionter_angle)*ball_force))
        ball_accel_y = ball_force_y/ball_mass
        ball_accel_x = ball_force_x/ball_mass
        ball_vel_y = ball_vel_y+int(numpy.round(numpy.sin(pionter_angle)*ball_force))
        ball_vel_x = ball_vel_x+int(numpy.round(numpy.cos(pionter_angle)*ball_force))
        ball_y = ball_vel_y+ball_y
        ball_x = ball_vel_x+ball_x
        
        
        #calc positions
        ball_y = int(ball_y+ball_vel_y)
        ball_x = int(ball_x+ball_vel_x)
        
        #draw proscribed shapes
        pygame.draw.circle(display, jo_color, (pionter_x, pionter_y), pionter_width, pionter_width)
        pygame.draw.circle(display, fu_color, (ball_x, ball_y), ball_radius, ball_wall)
        pygame.draw.rect(display, ground_color, (ground_x, ground_y, screen_width, screen_height))
        
        #loop the walls
        if ball_x>screen_width+ball_radius*3:
            ball_x = -ball_radius*3
        if ball_x<-ball_radius*3:
            ball_x = screen_width+ball_radius*3
        
        #make the game quit properly
        pygame.display.update()
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()
        ball_force = 0
        
        #if ball_y+ball_radius>ground_y:
            #ball_vel_y = (ball_y+ball_radius)-ground_y
pygame.quit