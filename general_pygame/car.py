import pygame
import numpy
pygame.init()

#funcs
def dist(ob1y,ob1x,ob2y,ob2x):
    ydif = ((ob1y-ob2y)**2)**0.5
    xdif = ((ob1x-ob2x)**2)**0.5
    dst = (ydif**2+xdif**2)**0.5
    if ob1y<ob2y:
        if ob1x<=ob2x:
            y = 1
            x = 1
        if ob1x>=ob2x:
            y = 1
            x = -1
    if ob1y>=ob2y:
        if ob1x<=ob2x:
            y = -1
            x = 1
        if ob1x>=ob2x:
            y = -1
            x = -1
    return dst,y,x
    

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
rect_width = 10
rect_height = 5
screen_height = 600
screen_width = 1200
ground_height = 150
ground_width = screen_width
ball_radius = 30
ball_wall = 30
ball_dist = 0

#start phis
rect_mass = 20
force = 0
vel = 0
ball_accel_y = 0
ball_accel_x = 0
ball_vel_y = 0
ball_vel_x = 0
ball_force_y = 0
ball_force_x = 0
ball_mass = 30

#start positions
ground_x = 0
ground_y = screen_height-ground_height
rect_y = ground_y-rect_height
rect_x = 200
ball_y = 200
ball_x = 800

#main game
run = True
while run:
    #create display
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    
    game = True
    while game:
        #dellay and screen reset
        pygame.time.delay(30)
        display.fill(bak_color)
        
        #controlls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            force = force+3
            print('run it')
        elif keys[pygame.K_LEFT]:
            force = force-3
            print('run nut')
        else:
            force = 0
        
        #air friction
        if vel>0:
            force = force - vel*0.1
        if vel<0:
            force = force + vel*0.1
        if ball_vel_x>0:
            ball_force_x = ball_force_x - ball_vel_x*0.6
        if ball_vel_x<0:
            ball_force_x = ball_force_x + ball_vel_x*0.6
            
        #set ground height for ball    
        d_ball_ground = ground_y - ball_y - ball_radius
        if d_ball_ground >= 0:
            ball_accel_y = 0.1 #gravity
        if d_ball_ground < 0:
            ball_vel_y = -ball_vel_y*0.5
            ball_vel_x = ball_vel_x*0.5
            
        #hit the ball
        ball_dist = dist(rect_y,rect_x+rect_width,ball_y,ball_x)
        ball_distR = dist(rect_y,rect_x,ball_y,ball_x)
        
        if ball_dist[0] <= ball_radius:
            ball_vel_y = -numpy.arcsin((rect_y-ball_y)/ball_dist[0])/(numpy.pi/2)*ball_vel_y
            ball_vel_x = float(ball_dist[2])*numpy.arccos((rect_x+rect_width-ball_x)/ball_dist[0])/(numpy.pi/2)*vel
        if ball_distR[0] <= ball_radius:
            ball_vel_y = -numpy.arcsin((rect_y-ball_y)/ball_distR[0])/(numpy.pi/2)*ball_vel_y
            ball_vel_x = float(ball_distR[2])*numpy.arccos((rect_x-ball_x)/ball_distR[0])/(numpy.pi/2)*vel
            
        #physics for rect
        accel = force/rect_mass
        vel = vel+accel
        
        #physics for ball
        ball_force_y = ball_mass*ball_accel_y
        ball_vel_y = ball_vel_y+ball_accel_y
        
        #averages force
        force_avg = list(accel_avg)
        force_avg.append(accel)
        if len(force_avg)>20:
            del force_avg[0]
        force_avg = numpy.array(force_avg)
        
        #averages acceleration
        accel_avg = list(accel_avg)
        accel_avg.append(accel)
        if len(accel_avg)>40:
            del accel_avg[0]
        accel_avg = numpy.array(accel_avg)
        
        #make the edges loop back to eachother
        if rect_x>screen_width+rect_width*3:
            rect_x = -rect_width*3
        if rect_x<-rect_width*3:
            rect_x = screen_width+rect_width*3
        if ball_x>screen_width+ball_radius*3:
            ball_x = -ball_radius*3
        if ball_x<-ball_radius*3:
            ball_x = screen_width+ball_radius*3
        
        #calc positions
        rect_x = rect_x+vel
        ball_y = int(ball_y+ball_vel_y)
        ball_x = int(numpy.round(ball_x+ball_vel_x))
        
        force = 0
        #print out data
        OUT = 'velocity:  '+str(numpy.absolute(numpy.round(vel,2)))+'m/s   force: '+str(numpy.round(numpy.mean(force_avg),2))+'N  acceleration: '+str(numpy.round(accel,2))+'m/s/s'
        font = pygame.font.Font('freesansbold.ttf', 12) 
        text = font.render(OUT, True, fu_color, bak_color)
        textRect = text.get_rect()
        textRect.center = (screen_width//2, screen_height//2)
        display.blit(text, textRect)
        
        #draw proscribed shapes
        pygame.draw.circle(display, fu_color, (ball_x, ball_y), ball_radius, ball_wall)
        pygame.draw.rect(display, ground_color, (ground_x, ground_y, screen_width, screen_height))
        pygame.draw.rect(display, jo_color, (rect_x, rect_y, rect_width, rect_height))
        
        #make the game quit properly
        pygame.display.update()
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()
                    
        
pygame.quit