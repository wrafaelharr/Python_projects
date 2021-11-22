import pygame
import numpy as np
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
bak_color = (165,23,115)
player_color = (130,30,30)
barry_color = (255,255,0)
blue = (50,50,200)
white = (200,200,200)

#postions
player_x = [screen_width/2,]
player_y = [screen_height/2,]
barry_x = int(screen_width*np.random.rand())
barry_y = int(screen_height*np.random.rand())
bady_x = int(screen_width*np.random.rand())
bady_y = int(screen_height*np.random.rand())
nut_x = []
nut_y = []

#angle
player_ang = 1.5*np.pi
shaft_ang = [1.5*np.pi,]
bady_ang = 2*np.pi*np.random.rand()
nut_ang = []

#speeds
player_move = 6
player_rotation = np.pi/30
bady_speed = 4
nut_speed = 10

#dimensions
dick_length = 20
barry_radius = 10
bady_radius = 10
nut_radius = 5

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((screen_width,screen_height))

#game rules
player_radius = int(dick_length/2)
dick_increase = 1
points = 0
collision = False
rotation_increase = 1000 #higher the less
delete = False

#main game
cube = True
while cube:    
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    #relative demensions
    ball_radius = int(player_radius*1.5)
        
    #controll rotation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rotation = player_rotation+np.pi/rotation_increase
        player_ang = player_ang + player_rotation
    elif keys[pygame.K_LEFT]:
        player_ang = player_ang - player_rotation
        player_rotation = player_rotation+np.pi/rotation_increase
    else:
        player_rotation = np.pi/30
    
    #looop
    #player
    if player_y[-1] < -player_radius:
        player_ang = np.pi/2
    elif player_y[-1] > screen_height+player_radius:
        player_ang = np.pi*1.5
    if player_x[-1] > screen_width+ball_radius:
        player_x[-1] = -ball_radius
    elif player_x[-1] < -ball_radius:
        player_x[-1] = screen_width+ball_radius
    #bady
    if bady_x < -bady_radius:
        bady_ang = 0
    elif bady_x > screen_width+bady_radius:
        bady_ang = np.pi
    elif bady_y < -bady_radius:
        bady_y = screen_height+bady_radius
    elif bady_y > screen_height+bady_radius:
        bady_y = -bady_radius
        
    #angles
    #player angle loop
    if player_ang > np.pi*2:
        player_ang = 0
    elif player_ang < 0:
        player_ang = np.pi*2
    
    #bady angle loop    
    if bady_ang > np.pi*2:
        bady_ang = 0
    elif bady_ang < 0:
        bady_ang = np.pi*2
    
    #bad boy decision making
    bady_ang = bady_ang + (np.random.rand()-0.5)/2
    
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
        
        #bady/nut collision
        if nut_dist < bady_radius+nut_radius:
            bady_radius = bady_radius + 2
            delete = True
            n = i
        else:   
            pygame.draw.circle(display, white, (int(nut_x[i]), int(nut_y[i])), nut_radius, nut_radius)
            delete = False
    
    #delete nut
    if delete:       
        del nut_ang[n],nut_x[n],nut_y[n]
    
    #player move
    player_x.append(player_x[-1] + player_move*np.cos(player_ang))
    player_y.append(player_y[-1] + player_move*np.sin(player_ang))
    shaft_ang.append(player_ang)
    
    #bady moves
    bady_x = bady_x + int(np.cos(bady_ang)*bady_speed)
    bady_y = bady_y + int(np.sin(bady_ang)*bady_speed)
    
    if len(player_x) > dick_length:
        del player_x[0]
        del player_y[0]
        del shaft_ang[0]
    
    
    #draw player
    for i in range(len(player_x)):
        #calc distance to barry for each sphere
        barry_dist = int(((barry_x-player_x[i])**2+(barry_y-player_y[i])**2)**0.5)
        
        #draw tip bump
        if i == len(player_x)-2:
            pygame.draw.circle(display, player_color, (int(player_x[i]), int(player_y[i])), int(player_radius*1.3), int(player_radius*1.3))
            
            #collision detection
            if barry_dist < player_radius*1.3+barry_radius:
                collision = True
            else:
                collision = False
                
        #draw shaft
        else:
            #shaft circles
            pygame.draw.circle(display, player_color, (int(player_x[i]), int(player_y[i])), player_radius, player_radius)
            
            #jump barry
            if barry_dist < player_radius+barry_radius:
                collision = True
            else:
                collision = False
    
    #collsion
    if collision:
        #reset barry postion
        barry_x = int(screen_width*np.random.rand())
        barry_y = int(screen_height*np.random.rand())
        
        #increase dick length
        dick_length = dick_length + dick_increase
        
        #increase points
        points = points+1
        
        #increase nut
        nut_x.append(player_x[-1])
        nut_y.append(player_y[-1])
        print(player_ang)
        nut_ang.append(player_ang)
    
    #draw balls        
    pygame.draw.circle(display, player_color, (int(player_x[0]+10*np.cos(shaft_ang[0]+np.pi/2)), int(player_y[0]+10*np.sin(shaft_ang[0]+np.pi/2))), ball_radius, ball_radius)
    pygame.draw.circle(display, player_color, (int(player_x[0]+10*np.cos(shaft_ang[0]-np.pi/2)), int(player_y[0]+10*np.sin(shaft_ang[0]-np.pi/2))), ball_radius, ball_radius)
    
    #draw barrys
    pygame.draw.circle(display, barry_color, (barry_x, barry_y), barry_radius, barry_radius)
    
    #badys
    pygame.draw.circle(display, blue, (bady_x, bady_y), bady_radius, bady_radius)
    
    #count the barries
    OUT = str(points)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(OUT, True, player_color, bak_color)
    textRect = text.get_rect()
    textRect.center = (50, 50)
    display.blit(text, textRect) 
    
    #update screen
    pygame.display.update()
    
    #make the game quit properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update()