import pygame
import numpy
pygame.init()

#colors
jo_color = (100,100,200)
fu_color = (200,100,100)

#start demensions
ball_size = 30
ball_wall = 2 
rect_height = 20
rect_width = 20

#start positions
ball_x = 500
ball_y = 250
rect_y = 600
rect_x = 400
bar_x = []
bar_y = []

run = True
while run:
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((1200,600))
    
    bar_x = numpy.arange(0,1200,10)
    bar_y = numpy.sin(bar_x)
    for i in range(len(bar_x)):
        pygame.draw.rect(display, jo_color, (bar_y[i], bar_x[i], rect_height, rect_width))
        
    pygame.draw.circle(display, fu_color, (ball_x, ball_y), ball_size, ball_wall)
    
    pygame.display.update()
    for event in pygame.event.get() :  
                if event.type == pygame.QUIT : 
                    pygame.quit() 
                    quit() 
                pygame.display.update()
pygame.quit