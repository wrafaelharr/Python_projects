import pygame
import numpy as np
pygame.init()

#functions
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

#perminants
screen_height = 600
screen_width = 1000

#colors
text_color = (200,100,100)
zeph_color = (100,100,200)
raf_color = (150,150,150)
bak_color = (80,0,0)
win_color = (130,0,130)
black = (0,0,0)
red = (255,0,0)

#character dimensions
monkey_width = []
monkey_height = []
barry_radius = 20
barry_wall = barry_radius
excile = 2000

#character position
raf_life = [10,10,10,10,10,10,10,10]
raf_x = list(np.zeros(8))
raf_y = list(np.zeros(len(raf_x)))
raf_ang = []
for i in range(len(raf_x)):
    raf_ang.append((np.pi)*(np.random.random_sample()*2))
raf_power = list(np.zeros(len(raf_x)))
barry_x = screen_width/3
barry_y = screen_height/3
for i in range(len(raf_ang)):
    raf_x[i] = screen_width/2
    raf_y[i] = screen_height/2
    
    
for i in range(len(raf_ang)):
    monkey_width.append(30)
    monkey_height.append(30)
    
power_avg = []
power = 0

run = True
while run:
    
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    game = True
    while game:
        #dellay and screen reset
        pygame.time.delay(30)
        display.fill(bak_color)
        
        for i in range(len(raf_ang)):
            #random rotation
            raf_ang[i] = raf_ang[i] + (np.pi/4)*(np.random.random_sample()-0.5)
                        
            #move based on rotation
            raf_y[i] = raf_y[i] + np.sin(raf_ang[i])*4
            raf_x[i] = raf_x[i] + np.cos(raf_ang[i])*4
            
            #loop angle
            if raf_ang[i] <= 0:
                raf_ang[i] = 2*np.pi
            elif raf_ang[i] >= 2*np.pi:
                raf_ang[i] = 0 
                
            #loop sides
            if raf_y[i] <= 0:
                raf_ang[i] = np.pi/2
            if raf_y[i]+monkey_height[i] >= screen_height:
                raf_ang[i] = np.pi*3/2
            if raf_x[i] <= 0:
                raf_ang[i] = 0
            if raf_x[i]+monkey_width[i] >= screen_width:
                raf_ang[i] = np.pi
        
        #kill each other
        for i in range(int(len(raf_ang)/2)):
            for n in np.arange(int(len(raf_ang)/2),int(len(raf_ang))):
                if raf_y[i]+monkey_width[i] > raf_y[n] and raf_y[i] < raf_y[n]+monkey_width[n] and raf_x[i]+monkey_width[i] > raf_x[n] and raf_x[i] < raf_x[n]+monkey_width[n]:
                    if raf_power[i] > raf_power[n]:
                        raf_y[n] = -excile
                    if raf_power[i] < raf_power[n]:
                        raf_y[i] = -excile
                        
        #dont walk on eachother
        for i in range(int(len(raf_ang))):
            for n in range(int(len(raf_ang))):
                if raf_y[i]+monkey_width[i] > raf_y[n] and raf_y[i] < raf_y[n]+monkey_width[n] and raf_x[i]+monkey_width[i] > raf_x[n] and raf_x[i] < raf_x[n]+monkey_width[n]:
                    if raf_y[i] < raf_y[n] and raf_x[i] < raf_x[n]:
                        raf_ang[i] = np.pi*3/4
                        raf_ang[n] = np.pi*7/4
                    elif raf_y[i] > raf_y[n] and raf_x[i] < raf_x[n]+monkey_width[i]/2:
                        raf_ang[i] = np.pi/4
                        raf_ang[n] = np.pi*5/4
                    elif raf_y[i]+monkey_height[i] < raf_y[n] and raf_x[i] > raf_x[n]:
                        raf_ang[i] = np.pi*5/4
                        raf_ang[n] = np.pi/4
                    elif raf_y[i]+monkey_height[i] > raf_y[n] and raf_x[i] > raf_x[n]+monkey_width[i]/2:
                        raf_ang[i] = np.pi*7/4
                        raf_ang[n] = np.pi*3/4
                        
        
        #draw shapes
        #grapes
        pygame.draw.circle(display, red, (int(barry_x), int(barry_y)), barry_radius, barry_wall)
        
        #rafs
        pygame.draw.rect(display, raf_color, (raf_x[0], raf_y[0], monkey_width[0], monkey_height[0]))
        pygame.draw.rect(display, raf_color, (raf_x[1], raf_y[1], monkey_width[1], monkey_height[1]))
        pygame.draw.rect(display, raf_color, (raf_x[2], raf_y[2], monkey_width[2], monkey_height[2]))
        pygame.draw.rect(display, raf_color, (raf_x[3], raf_y[3], monkey_width[3], monkey_height[3]))
        #zephs
        pygame.draw.rect(display, zeph_color, (raf_x[4], raf_y[4], monkey_width[4], monkey_height[4]))
        pygame.draw.rect(display, zeph_color, (raf_x[5], raf_y[5], monkey_width[5], monkey_height[5]))
        pygame.draw.rect(display, zeph_color, (raf_x[6], raf_y[6], monkey_width[6], monkey_height[6]))
        pygame.draw.rect(display, zeph_color, (raf_x[7], raf_y[7], monkey_width[7], monkey_height[7]))
        
        
        #get a berry
        for i in range(len(raf_ang)):
            metobarry = []
            
            distance_TL = list(dist(raf_y[i],raf_x[i],barry_y,barry_x))
            distance_TR = list(dist(raf_y[i],raf_x[i]+monkey_width[i],barry_y,barry_x))
            distance_BL = list(dist(raf_y[i]+monkey_height[i],raf_x[i],barry_y,barry_x))
            distance_BR = list(dist(raf_y[i]+monkey_height[i],raf_x[i]+monkey_width[i],barry_y,barry_x))
            
            distance_centr = list(dist(raf_y[i]+monkey_height[i]/2,raf_x[i]+monkey_width[i]/2,barry_y,barry_x))
            
            metobarry.append(distance_TL[0])
            metobarry.append(distance_TR[0])
            metobarry.append(distance_BL[0])
            metobarry.append(distance_BR[0])
            
            
            for n in metobarry:
                if int(n) < barry_radius or distance_centr < monkey_width:
                    raf_power[i] = raf_power[i]+1
                    monkey_width[i] = monkey_width[i]+5*barry_radius/10
                    monkey_height[i] = monkey_height[i]+5*barry_radius/10
                    barry_radius = int(barry_radius*(np.random.random_sample()+0.5))
                    barry_wall = barry_radius
                    barry_x = screen_width/2*(np.random.random_sample()+0.5)
                    barry_y = screen_height/2*(np.random.random_sample()+0.5)
        
        #chase barry
        for i in range(len(raf_ang)):
            find = list(dist(raf_y[i]+monkey_height[i]/2,raf_x[i]+monkey_height[i]/2,barry_y,barry_x))
            if find[1] > 0 and find[2] < 0:
                d_to_b = np.pi*3/4
            elif find[1] < 0 and find[2] > 0:
                d_to_b = np.pi/4
            elif find[1] < 0 and find[2] > 0:
                d_to_b = np.pi*5/4    
            elif find[1] < 0 and find[2] < 0:
                d_to_b = np.pi*7/4
                
            if (1-find[0]/600) > 0:
                muilty = (1-find[0]/300)
            else:
                muilty = 0
                
            if raf_ang[i] < d_to_b:
                raf_ang[i] = raf_ang[i]+(np.pi/6)*muilty
            elif raf_ang[i] > d_to_b:
                raf_ang[i] = raf_ang[i]-(np.pi/6)
        
                
        #report power
        OUT = 'raf power:  '+str(raf_power[0:4])+'  zeph power'+str(raf_power[4:8])
        font = pygame.font.Font('freesansbold.ttf', 12) 
        text = font.render(OUT, True, text_color, bak_color)
        textRect = text.get_rect()
        textRect.center = (screen_width//2, screen_height*10/12)
        display.blit(text, textRect)
        
        #report lives
        for i in range(len(raf_ang)):
            if raf_y[i] < -monkey_height[i]:
                raf_life[i] = 10-np.round(((raf_y[i])**2)**0.5*10/excile)
            else:
                raf_life[i] = 10
                
        OUT = 'raf living:  '+str(raf_life[0:4])+'  zeph living'+str(raf_life[4:8])
        font = pygame.font.Font('freesansbold.ttf', 12) 
        text = font.render(OUT, True, text_color, bak_color)
        textRect = text.get_rect()
        textRect.center = (screen_width//2, screen_height*11/12)
        display.blit(text, textRect)
        
        #update screen
        pygame.display.update()
        
        #declare winner
        if 10 not in raf_life[0:4] or 10 not in raf_life[4:8]:
            death_screen = True
            while True:
                font = pygame.font.Font('freesansbold.ttf', 32) 
                if 1 not in raf_life[0:4]:
                    text = font.render('zeph wins', True, black, win_color) 
                elif 1 not in raf_life[4:8]:
                    text = font.render('raf wins', True, black, win_color) 
                textRect = text.get_rect()  
                textRect.center = (screen_width / 2, screen_height/ 2) 
                display.fill(win_color)
                display.blit(text, textRect) 
                
                #restart
                keys = pygame.key.get_pressed()
                if keys[pygame.K_TAB]:
                    #character position
                    raf_life = [10,10,10,10,10,10,10,10]
                    raf_x = list(np.zeros(8))
                    raf_y = list(np.zeros(len(raf_x)))
                    raf_ang = []
                    for i in range(len(raf_x)):
                        raf_ang.append((np.pi)*(np.random.random_sample()*2))
                    raf_power = list(np.zeros(len(raf_x)))
                    barry_x = screen_width/3
                    barry_y = screen_height/3
                    for i in range(len(raf_ang)):
                        raf_x[i] = screen_width/2
                        raf_y[i] = screen_height/2
                    #remove death screen
                    death_screen = False
                
                for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()
        
        #quit properly
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()