import pygame 
import numpy as np
import DWfuncs as fun
pygame.init()

def menu_func():
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
            
        #quite
        for event in pygame.event.get() :  
            if event.type == pygame.QUIT : 
                pygame.quit() 
                quit() 
            pygame.display.update()