import pygame 
import numpy as np
import DWfuncs as fun
pygame.init()

#colors
on_color = (100,150,120)
lime = (0,255,0)
menu_color = (10,20,50)
ground_color = (130,30,30)
moon_color = (200,200,200)

#screen demensions
screen_height=600
screen_width=1200

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen_width,screen_height))

on = [False,True,False]
count = 0
moon_height = screen_height/3
moon_radius = 40

menu = True
#menu
while menu:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(menu_color)
        
    #getting key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        menu = False
    elif keys[pygame.K_DOWN]:
        on[1] = False
        on[2] = True
    elif keys[pygame.K_UP]:
        on[1] = True
        on[2] = False
    
    
           
        
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
    
    #draw background
    pygame.draw.circle(display, moon_color, (int(screen_width*5/6), int(moon_height)), moon_radius, moon_radius)
    pygame.draw.circle(display, menu_color, (int(screen_width*5/6-15), int(moon_height-5)), moon_radius, moon_radius)
    pygame.draw.rect(display, ground_color, (0, screen_height/2+80, screen_width, screen_height))
    
    #update screen
    pygame.display.update()
    
    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update() 