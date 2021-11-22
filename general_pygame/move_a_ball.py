import pygame
import numpy as np
pygame.init()

#perminants
screen_height = 600
screen_width = 1000
ground_height = 150
ground_x = 0
ground_y = screen_height-ground_height
daynight = 1

#colors
moon_color = (100,100,200)
printer_color = (200,100,100)
skirt_color = (200,100,200)
bak1_color = (130,0,130)
ground_color = (80,0,0)
black = (0,0,0)
monkey_color = (150,150,150)

#characters demensions
printer_width = 50
skirt_height = 30
printer_height = 20
printer_skirt = printer_width*0.30
monkey_width = 10
monkey_height = 10

#character positions
printer_x = (screen_width-printer_width)*0.5
printer_y = ground_y-skirt_height/2
monkey_x = [0,0,0,0]
monkey_y = [0,0,0,0]
monkey_ang = [0,0,0,0]
for i in range(4):
    monkey_x[i] = screen_width/2
    monkey_y[i] = ground_y+0.5*ground_height-0.5*monkey_height


#printer stats
power = 0

#background movement start postion
moon_y = screen_height
moon_x = 800

#ball start demensions
moon_radius = 30
moon_wall = 30

count = 0
rund = []
bak_color = bak1_color

test = []
#main game
run = True
while run:
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    game = True
    while game:
        #dellay and screen reset
        count = count+1
        pygame.time.delay(30)
        display.fill(bak_color)
        
        #moon orbit
        if count > 1:
            moon_y = moon_y-3*daynight
            moon_x = moon_x-1
            count = 0
        if moon_y < 0-moon_radius*1.5:
            daynight = -1
            bak_color = bak1_color
        if moon_y > screen_height:
            daynight = 1
            bak_color = bak1_color
        if moon_x-moon_radius < 0:
            daynight = 1
        
        #sun set
        if moon_y+moon_radius < ground_y:
            bak_color = list(bak_color)
            bak_color[1] = int(bak_color[1]*np.absolute(moon_y/(screen_height/2)))
            if np.absolute(int(bak_color[2]*np.absolute(moon_y/(screen_height*2/3))))<255 and np.absolute(int(bak_color[2]*np.absolute(moon_y/(screen_height*2/3))))>0:
                bak_color[2] = np.absolute(int(bak_color[2]*np.absolute(moon_y/(ground_y))))
            if np.absolute(int(bak_color[0]*np.absolute(moon_y/(screen_height*2/3))))<255 and np.absolute(int(bak_color[0]*np.absolute(moon_y/(screen_height*2/3))))>0:
                bak_color[0] = int(bak_color[0]*np.absolute(moon_y/(ground_y+ground_height/2)))
            bak_color = tuple(bak_color)
        
        #charge when teh suns out
        if moon_y < ground_y:
            power = np.round(power+(moon_y/screen_height)*2)
        
        #monkeys
        for i in range(4):
            #random rotation
            monkey_ang[i] = monkey_ang[i] + (np.pi/4)*(np.random.random_sample()-0.5)
            
            #stay on the ground
            if monkey_y[i] <= ground_y:
                if monkey_ang[i] < np.pi*3/2:
                    monkey_ang[i] = np.pi/2
                elif monkey_ang[i] > np.pi*3/2:
                    monkey_ang[i] = np.pi/2
            
            #don't go to low
            if monkey_y[i] >= screen_height+monkey_height*5:
                if monkey_ang[i] < np.pi/2:
                    monkey_ang[i] = np.pi*3/2
                elif monkey_ang[i] > np.pi/2:
                    monkey_ang[i] = np.pi*3/2
                        
            #move based on rotation
            monkey_y[i] = monkey_y[i] + np.sin(monkey_ang[i])*4
            monkey_x[i] = monkey_x[i] + np.cos(monkey_ang[i])*4
            
            #lOOP:
            #angle
            if monkey_ang[i] <= 0:
                monkey_ang[i] = 2*np.pi
            elif monkey_ang[i] >= 2*np.pi:
                monkey_ang[i] = 0 
            #sides       
            if np.absolute(monkey_x[i]-(screen_width/2)) > (screen_width/2)+monkey_width*4:
                if monkey_x[i]-(screen_width/2) > 0:
                    monkey_x[i] = 0-monkey_width*2
                elif monkey_x[i]-(screen_width/2) < 0:
                    monkey_x[i] = screen_width+monkey_width*2
        
        #draw proscribed shapes
        if daynight == 1:
            pygame.draw.circle(display, moon_color, (moon_x, moon_y), moon_radius, moon_wall)
        pygame.draw.rect(display, ground_color, (ground_x, ground_y, screen_width, screen_height))
        points = [(printer_x-printer_skirt,printer_y+skirt_height),(printer_x+printer_width+printer_skirt,printer_y+skirt_height),(printer_x+printer_width,printer_y),(printer_x,printer_y)]
        pygame.draw.polygon(display, skirt_color, points)
        pygame.draw.rect(display, printer_color, (printer_x, printer_y, printer_width, printer_height))
        pygame.draw.rect(display, monkey_color, (monkey_x[0], monkey_y[0], monkey_width, monkey_height))
        pygame.draw.rect(display, monkey_color, (monkey_x[1], monkey_y[1], monkey_width, monkey_height))
        pygame.draw.rect(display, monkey_color, (monkey_x[2], monkey_y[2], monkey_width, monkey_height))
        pygame.draw.rect(display, monkey_color, (monkey_x[3], monkey_y[3], monkey_width, monkey_height))
        
        OUT = 'power:  '+str(power)+'V moon_y: '+str(moon_y)
        font = pygame.font.Font('freesansbold.ttf', 12) 
        text = font.render(OUT, True, printer_color, bak_color)
        textRect = text.get_rect()
        textRect.center = (screen_width//2, screen_height//2)
        display.blit(text, textRect)
        
        #make the game quit properly
        pygame.display.update()
        
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()
print(test)