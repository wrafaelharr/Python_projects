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
rect_x=int(screen_width /2)
rect_y=int(screen_height /2)
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

#counters
points = 0
delete = False
badys = True


#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen_width,screen_height))

menu = True
#menu
while menu:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(menu_color)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        menu = False
    
    #count the barries
    OUT = 'DICK WORK'
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(OUT, True, red, menu_color)
    textRect = text.get_rect()
    textRect.center = (screen_width/2, screen_height/4)
    display.blit(text, textRect) 
    
    #count the barries
    OUT = 'start'
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(OUT, True, red, menu_color)
    textRect = text.get_rect()
    textRect.center = (screen_width/2, screen_height/3)
    display.blit(text, textRect) 
    
    #count the barries
    OUT = 'dificulty'
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(OUT, True, red, menu_color)
    textRect = text.get_rect()
    textRect.center = (screen_width/2, screen_height/2)
    display.blit(text, textRect) 
    
    #difficulty scale
    #pygame.draw.rect(display, jo_color, (rect_x, screen_height*3/4), dick_gerth, dick_length))
        
    #quite
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update()

    
#main game
game = True
while game:
   
    
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    #loop screen player
    if rect_x > screen_width:
        rect_x = 0
    elif rect_x < 0:
        rect_x = screen_width     
    elif rect_y >screen_height:
        rect_y =0
    elif rect_y < 0:
        rect_y =screen_height 
    
    #loop screen badys
    if bady_x > screen_width:
        bady_x = 0
    elif bady_x < 0:
        bady_x = screen_width     
    elif bady_y >screen_height:
        bady_y =0
    elif bady_y < 0:
        bady_y =screen_height 
   
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect_x = rect_x + move
    elif keys[pygame.K_LEFT]:
        rect_x = rect_x - move
    
    if keys[pygame.K_UP]:
        rect_y = rect_y - move
    elif keys[pygame.K_DOWN]:
        rect_y = rect_y + move

    #collision ditection
    dist = ((rect_x+dick_gerth/2-ball_x)**2+(rect_y+dick_gerth/2-ball_y)**2)**0.5
    
    #if center of the cube crosses the barry
    if dist < ball_radius+dick_gerth/2:
        #randomly reset barry placement
        ball_x=int(screen_width*np.random.rand())
        ball_y=int(screen_height*np.random.rand())
        
        #grow character
        dick_gerth = dick_gerth + 1
        dick_length = dick_length + 3
        balls_radius = balls_radius + 1
        
        #count up points
        points = points+1
        
        nut_x.append(rect_x+dick_gerth/2)
        nut_y.append(rect_y)
        nut_ang.append(1.5*np.pi)
        
    #nut
    for i in range(len(nut_ang)):
        nut_ang[i] = nut_ang[i] + np.random.rand()-0.5
        nut_x[i] = nut_x[i] + int(np.cos(nut_ang[i])*nut_speed)
        nut_y[i] = nut_y[i] + int(np.sin(nut_ang[i])*nut_speed)
        if nut_y[i] <= 0:
            nut_ang[i] = np.pi/2
        elif nut_y[i] >= screen_height:
            nut_ang[i] = 1.5*np.pi
        
        #not bad boy collision
        nut_dist = ((nut_x[i]-bady_x)**2+(nut_y[i]-bady_y)**2)**0.5
            
        if nut_dist < bady_radius+nut_radius:
            delete = True
            n = i
            bady_radius = bady_radius + 2
            print('yes')
        else:   
            pygame.draw.circle(display, white, (int(nut_x[i]), int(nut_y[i])), nut_radius, nut_radius)
            delete = False
    
    #delete eatin nut
    if delete:       
        del nut_ang[n],nut_x[n],nut_y[n]
        
    #find distance from bad guy to Left and Right balls   
    ball_distL = ((bady_x-rect_x)**2+(bady_y-rect_y+dick_length)**2)**0.5
    ball_distR = ((bady_x-int(rect_x+dick_gerth))**2+(bady_y-rect_y+dick_length)**2)**0.5
    
    #eat the balls
    if ball_distL < bady_radius+balls_radius or ball_distR < bady_radius+balls_radius:
        if balls_radius < bady_radius:
            #start positions
            rect_x=int(screen_width /2)
            rect_y=int(screen_height /2)
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
            points = 0
            badys = True
        else:
            badys = False
    
    #bad boy decision making
    bady_ang = bady_ang + np.random.rand()-0.5
    
    #bady moves
    bady_x = bady_x + int(np.cos(bady_ang)*bady_speed)
    bady_y = bady_y + int(np.sin(bady_ang)*bady_speed)
    
    #count the barries
    OUT = str(points)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(OUT, True, red, bak_color)
    textRect = text.get_rect()
    textRect.center = (50, 50)
    display.blit(text, textRect) 
    
    #food
    pygame.draw.circle(display, red, (ball_x, ball_y), ball_radius, ball_wall)
    
    #bad guys
    if badys:
        pygame.draw.circle(display, blue, (bady_x, bady_y), bady_radius, bady_radius) 
    
    #dick
    pygame.draw.rect(display, jo_color, (rect_x, rect_y, dick_gerth, dick_length))
    
    #balls
    pygame.draw.circle(display, jo_color, (int(rect_x+dick_gerth), rect_y+dick_length), balls_radius, balls_radius)
    pygame.draw.circle(display, jo_color, (int(rect_x), rect_y+dick_length), balls_radius, balls_radius)
    
    #update screen
    pygame.display.update()
    
    #quite
    for event in pygame.event.get() :  
                if event.type == pygame.QUIT : 
                    pygame.quit() 
                    quit() 
                pygame.display.update()

