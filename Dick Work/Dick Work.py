import pygame
import numpy as np
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#menu colors
on_color = (100,150,120)
lime = (0,255,0)
menu_color = (10,20,50)
ground_color = (130,30,30)
moon_color = (200,200,200)
dick_color = (255,84,167)

#game colors
bak_color = (165,23,115)
player_color = (130,30,30)
barry_color = (222,49,99)
blue = (50,50,200)
white = (200,200,200)

#menu background info
on = [False,True,False]
count = 0
moon_height = screen_height/3
moon_radius = 40
ground_dist = screen_height/2+80
ground_height = screen_height-ground_dist

#positions
player_x = [screen_width/2,]
player_y = [screen_height/2,]
barry_x = int(screen_width*np.random.rand())
barry_y = int(screen_height*np.random.rand())
bady_x = int(screen_width*np.random.rand())
bady_y = int(screen_height*np.random.rand())
nut_x = []
nut_y = []
dick_x = [screen_width/2,]
dick_y = [ground_dist+ground_height/2,]
chase_x = []
chase_y = []
cop_x = []
cop_y = []

#angle
player_ang = 1.5*np.pi
shaft_ang = [1.5*np.pi,]
bady_ang = 2*np.pi*np.random.rand()
nut_ang = []
dick_ang = 2*np.pi*np.random.rand()

#speeds
player_move = 6
player_rotation = np.pi/30
bady_speed = 2
nut_speed = 7
dick_move = 6

#dimensions
menu_dick_length = 20
dick_length = 20
barry_radius = 10
bady_radius = 10
nut_radius = 5
player_radius = int(dick_length/2)
dick_radius = int(dick_length/2)

#game rules
dick_increase = 14
points = dick_length
collision = False
rotation_increase = 1000 #higher the less
delete = False
n = []
chase_dist = 20

#menu extras
star_move = 2
star_x = []
star_y = []
star_ang = []
for i in range(20):
            star_x.append(screen_width*np.random.rand())
            star_y.append(ground_dist*np.random.rand())
            star_ang.append(2*np.pi*np.random.rand())

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((screen_width,screen_height))

while True:
    #menu
    menu = True
    while menu:
        #dellay and screen reset
        pygame.time.delay(30)
        display.fill(menu_color)
            
        #getting key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and on[1] == True:
            menu = False
        elif keys[pygame.K_DOWN]:
            on[1] = False
            on[2] = True
        elif keys[pygame.K_UP]:
            on[1] = True
            on[2] = False
        elif keys[pygame.K_RIGHT] and on[2]:
            menu_dick_length = menu_dick_length +2
        elif keys[pygame.K_LEFT] and on[2]:
            menu_dick_length = menu_dick_length -2
        
        #menu items
        title = ['DICK WORK',50]
                
        #positions
        spacing = 70
        title_pos = (screen_width/2, screen_height/3)
        start_pos = (screen_width/2, screen_height/3+spacing)
        difik_pos = (screen_width/2, screen_height/3+spacing*2)
        
        #lists
        words = [title[0],'start','difficulty']
        pos = [title_pos,start_pos,difik_pos]
        size = [title[1],20,20]
        
        for i in range(len(words)):
            
            if on[i]:
                active = on_color
            else:
                active = menu_color
                
            #draw
            font = pygame.font.Font('freesansbold.ttf', size[i])
            text = font.render(words[i], True, lime, active)
            textRect = text.get_rect()
            textRect.center = pos[i]
            display.blit(text, textRect) 
        
        #move the moon
        moon_height = moon_height + 1/2
        
        #loop moon
        if moon_height > screen_height*3/4:
            moon_height = -moon_radius
        
        #stars
        for i in range(len(star_x)):
            star_ang[i] = star_ang[i] + (np.pi/12)*np.random.rand()
            
            if star_x[i] < 0:
                star_ang[i] = 0
            elif star_x[i] > screen_width:
                star_ang[i] = np.pi
            elif star_y[i] < 0:
                star_ang[i] = 0.5*np.pi
            elif star_y[i] > ground_dist:
                star_ang[i] = 1.5*np.pi
                
            star_x[i] = star_x[i] + star_move*np.cos(star_ang[i])
            star_y[i] = star_y[i] + star_move*np.sin(star_ang[i])
            pygame.draw.circle(display, white, (int(star_x[i]), int(star_y[i])), nut_radius, nut_radius)
        
        #draw background
        #moon
        pygame.draw.circle(display, moon_color, (int(screen_width*5/6), int(moon_height)), moon_radius, moon_radius)
        pygame.draw.circle(display, menu_color, (int(screen_width*5/6-15), int(moon_height-5)), moon_radius, moon_radius)
        #ground
        pygame.draw.rect(display, ground_color, (0, ground_dist, screen_width, screen_height))
        
        #dick cission making
        dick_ang = dick_ang + (np.random.rand()-0.5)/2
        
        #stay on the ground
        if dick_y[-1] > screen_height+dick_length*2:
            dick_ang = 1.5*np.pi
        elif dick_y[-1] < ground_dist+dick_radius:
            dick_ang = 0.5*np.pi
        elif dick_x[-1] < -dick_radius*1.3:
            dick_x[-1] = screen_width + dick_radius*1.3
        elif dick_x[-1] > screen_width+dick_radius*1.3:
            dick_x[-1] = -dick_radius*1.3
            
        cop_x.append(dick_x[0]) 
        cop_y.append(dick_y[0])
        
        if len(cop_x) > chase_dist:
            del cop_x[0],cop_y[0]
            len(cop_x)
            
        
        #dick move
        dick_x.append(int(dick_x[-1] + dick_move*np.cos(dick_ang)))
        dick_y.append(int(dick_y[-1] + dick_move*np.sin(dick_ang)))
        shaft_ang.append(dick_ang)
        
        #adjust dick length
        if len(dick_x) > menu_dick_length:
            for p in range(len(dick_x)-dick_length):
                del dick_x[p],dick_y[p],shaft_ang[p]
                
        #draw cop
        pygame.draw.circle(display, blue, (int(cop_x[0]), int(cop_y[0])), bady_radius, bady_radius)
        
        #draw dick
        for i in range(len(dick_x)):
            #draw tip bump
            if i == len(dick_x)-2:
                pygame.draw.circle(display, dick_color, (int(dick_x[i]), int(dick_y[i])), int(dick_radius*1.3), int(dick_radius*1.3))
            #shaft circles
            pygame.draw.circle(display, dick_color, (int(dick_x[i]), int(dick_y[i])), dick_radius, dick_radius)
        
        #draw balls 
        ball_radius = int(player_radius*1.5)
        pygame.draw.circle(display, dick_color, (int(dick_x[0]+10*np.cos(shaft_ang[0]+np.pi/2)), int(dick_y[0]+10*np.sin(shaft_ang[0]+np.pi/2))), ball_radius, ball_radius)
        pygame.draw.circle(display, dick_color, (int(dick_x[0]+10*np.cos(shaft_ang[0]-np.pi/2)), int(dick_y[0]+10*np.sin(shaft_ang[0]-np.pi/2))), ball_radius, ball_radius)
        
        #update screen
        pygame.display.update()
        
        #quite properly 
        for event in pygame.event.get() :  
            if event.type == pygame.QUIT : 
                pygame.quit() 
                #quit() 
            pygame.display.update()
            
    
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
    points = dick_length
    collision = False
    rotation_increase = 1000 #higher the less
    delete = False
    n = []
    
    
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
                bady_radius = bady_radius + 1
                delete = True
                n.append(i)
            else:   
                pygame.draw.circle(display, white, (int(nut_x[i]), int(nut_y[i])), nut_radius, nut_radius)
                delete = False
        
        #delete nut
        if delete:
            for s in n:
                try:
                    del nut_ang[s],nut_x[s],nut_y[s]
                except:
                   print('')
        else:
            n = []
        
        #player move
        player_x.append(player_x[-1] + player_move*np.cos(player_ang))
        player_y.append(player_y[-1] + player_move*np.sin(player_ang))
        shaft_ang.append(player_ang)
        
        #bady moves
        bady_x = bady_x + int(np.cos(bady_ang)*bady_speed)
        bady_y = bady_y + int(np.sin(bady_ang)*bady_speed)
        
        #adjust dick length
        if len(player_x) > dick_length:
            for p in range(len(player_x)-dick_length):
                del player_x[p],player_y[p],shaft_ang[p]
        if dick_length < int(dick_increase/2) and points < int(dick_increase/2):
            cube = False
            
        left = False
        right = False
        up = False
        down = False
        #draw player
        for i in range(len(player_x)):
            #calc distance to barry for each sphere
            barry_dist = int(((barry_x-player_x[i])**2+(barry_y-player_y[i])**2)**0.5)
            
            #dist to enemy
            bady_dist = int(((bady_x-player_x[i])**2+(bady_y-player_y[i])**2)**0.5)
            
            #wrap
            if player_x[i] < bady_x:
                left = True
            elif player_x[i] > bady_x:
                right = True
            if player_y[i] < bady_y:
                up = True
            elif player_y[i] > bady_y:
                down = True
            
            if left and right and up and down:
                cube = False
            
            #draw tip bump
            if i == len(player_x)-2:
                pygame.draw.circle(display, player_color, (int(player_x[i]), int(player_y[i])), int(player_radius*1.3), int(player_radius*1.3))
                
                #collision detection
                if barry_dist < player_radius*1.3+barry_radius:
                    collision = True
                else:
                    collision = False
                if bady_dist < player_radius*1.3+bady_radius:
                    bady_coll = True
                else:
                    bady_coll = False
                    
            #draw shaft
            #shaft circles
            pygame.draw.circle(display, player_color, (int(player_x[i]), int(player_y[i])), player_radius, player_radius)
            
            #jump barry
            if barry_dist < player_radius+barry_radius:
                collision = True
            else:
                collision = False
            if bady_dist < player_radius+bady_radius:
                bady_coll = True
            else:
                bady_coll = False
        
        #collsion
        if collision:
            #reset barry postion
            barry_x = int(screen_width*np.random.rand())
            barry_y = int(screen_height*np.random.rand())
            
            #increase dick length
            dick_length = dick_length + dick_increase
            
            #increase points
            points = points+dick_increase
            
            #increase nut
            nut_x.append(player_x[-1])
            nut_y.append(player_y[-1])
            nut_ang.append(player_ang)
        if bady_coll and dick_length > dick_increase:
            bak_color = (200,0,0)
            points = points - int(dick_increase/2)
            dick_length = dick_length - int(dick_increase/2)
        else:
            bak_color = (165,23,115)
            
        #death
        if dick_length < 3 or points < 3:
            cube = False
        
        #tick to balls loop
        #dist to balls
        ball_rx = int(player_x[0]+10*np.cos(shaft_ang[0]+np.pi/2))
        ball_ry = int(player_y[0]+10*np.sin(shaft_ang[0]+np.pi/2))
        ball_lx = int(player_x[0]+10*np.cos(shaft_ang[0]-np.pi/2))
        ball_ly = int(player_y[0]+10*np.sin(shaft_ang[0]-np.pi/2))
        ball_loop_dist_r = int(((ball_rx-player_x[-1])**2+(ball_ry-player_y[-1])**2)**0.5)
        ball_loop_dist_l = int(((ball_lx-player_x[-1])**2+(ball_ly-player_y[-1])**2)**0.5)
        
        if ball_loop_dist_r < ball_radius+player_radius*1.3 or ball_loop_dist_r < ball_radius+player_radius*1.3:
            bak_color = (0,100,0)
        else:
            bak_color = (165,23,115)

        
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