import pygame
import numpy as np
pygame.init()   

#screen demensions
screen_width = 600
screen_height = 600

def graph(surface, color, width, slope, graph_x = 0, graph_y = 0, ticks_x = 12,ticks_y = 12,label_size = 20, bak_color = (0,0,0)):
    
    #colors
    white = (255,255,255)
    
    #change later
    margin = 50
    
    #important graph locations
    origen_y = screen_height-margin
    origen_x = 0+margin
    
    #unit definitions
    unit_x = screen_width/ticks_x
    unit_y = screen_height/ticks_y
    
    #graph
    start_x = origen_x
    start_y = origen_y
    end_x = screen_width
    end_y = origen_y-unit_y*slope*((screen_height/unit_x)-1)
    if end_y < 0:
        end_y = 0
    start_pos = (start_x,start_y)
    end_pos = (end_x,end_y)
    
    #graph line
    pygame.draw.line(surface, color, start_pos, end_pos, width)
    
    #graph origen lines
    pygame.draw.line(surface, white, (0,origen_y), (screen_width,origen_y), width)
    pygame.draw.line(surface, white, (origen_x,screen_height), (origen_x,0), width)
    
    #draw ticks
    for i in np.arange(origen_x,screen_width,unit_x):
            pygame.draw.line(surface, white, (i,origen_y+label_size/2), (i,origen_y-label_size/2), width)
            
            #numbers
            if i > origen_x:
                OUT = str(int(((screen_width)/unit_x)-((screen_width-i)/unit_x)-1))
                font = pygame.font.Font('freesansbold.ttf', 10) 
                text = font.render(OUT, True, white, bak_color)
                textRect = text.get_rect()
                textRect.center = (i, origen_y+label_size)
                display.blit(text, textRect)
            
    for i in np.arange(origen_x,screen_height,unit_y):
            pygame.draw.line(surface, white, (origen_x+label_size/2,i), (origen_x-label_size/2,i), width)
            
            #numbers
            if i < origen_y:
                OUT = str(int((screen_height-i)/unit_x)-1)
                font = pygame.font.Font('freesansbold.ttf', 10) 
                text = font.render(OUT, True, white, bak_color)
                textRect = text.get_rect()
                textRect.center = (origen_x-label_size,i)
                display.blit(text, textRect)

#main
run = True
while run:
    #create window
    pygame.display.set_caption('graph')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    #variables
    color = (255,0,0)
    width = 2
    surface = display
    
    #graph talk
    slope = 1
    
    
    #graph
    graph(surface, color, width,slope)
    
    #update screen
    pygame.display.update()
    
    #quit properly
    for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()