import pandas
import pygame
import numpy
import time
#import tensorflow
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
bak_color = (150, 100, 220)
yellow = (255, 255, 0)
green = (30, 180, 30)
black = (0,0,0)

#helpful funcs
def write_text(string, size, color, highlight, x, y):
    font = pygame.font.Font('Shadded South Personal Use.ttf', size)
    text = font.render(string, True, color, highlight)
    textRect = text.get_rect()
    textRect.center = (x, y)
    display.blit(text, textRect)

#sample data
ex_x = (1, 2, 3, 4, 5, 6)
ex_x = numpy.random.randint(8, size=len(ex_x))
ex_y = (12, 9, 8, 4, 3, 1)

#graphs class
class graph:
    def line(display, x, y, x_bound, y_bound, x_label='butts', y_label='tits', width=500, height=500, bourder=30, dash_width=4):
        x_unit = width/(max(x) - min(x))
        y_unit = height/(max(y) - min(y))

        #background
        pygame.draw.rect(display, green, (x_bound-bourder/2, y_bound-height-bourder/2, height+bourder, width+bourder))

        #x marks
        for i in range(round((max(x) - min(x))+1)):
            tick_x = x_bound-dash_width/2 + x_unit*i
            tick_y = y_bound+bourder/2-dash_width*3/2

            pygame.draw.rect(display, black, (tick_x, tick_y, dash_width, dash_width*3))
            write_text(str(i+min(x)), dash_width*3, black, bak_color, tick_x, tick_y+dash_width*6)

        #y marks
        for i in range(round((max(y) - min(y))+1)):
            tick_x = x_bound-bourder/2-dash_width*3/2
            tick_y = y_bound-dash_width/2 - y_unit*i

            pygame.draw.rect(display, black, (tick_x, tick_y, dash_width*3, dash_width))
            write_text(str(i+min(y)), dash_width*3, black, bak_color, tick_x-dash_width*3, tick_y)


    def scatter(display, x, y, x_bound, y_bound, point_size=5, width=200, height=200, bourder=30, dash_width=4):
        x_unit = width/(max(x) - min(x))
        y_unit = height/(max(y) - min(y))

        line_x1 = 0
        line_y1 = 0
        line_x2 = 0
        line_y2 = 0

        #background
        pygame.draw.rect(display, green, (x_bound-bourder/2, y_bound-height-bourder/2, height+bourder, width+bourder))

        #x marks
        for i in range(round((max(x) - min(x))+1)):
            tick_x = x_bound-dash_width/2 + x_unit*i
            tick_y = y_bound+bourder/2-dash_width*3/2

            pygame.draw.rect(display, black, (tick_x, tick_y, dash_width, dash_width*3))
            write_text(str(i+min(x)), dash_width*3, black, bak_color, tick_x, tick_y+dash_width*6)

        #y marks
        for i in range(round((max(y) - min(y))+1)):
            tick_x = x_bound-bourder/2-dash_width*3/2
            tick_y = y_bound-dash_width/2 - y_unit*i

            pygame.draw.rect(display, black, (tick_x, tick_y, dash_width*3, dash_width))
            write_text(str(i+min(y)), dash_width*3, black, bak_color, tick_x-dash_width*3, tick_y)

        '''
        for i in ((x[i]-min(x))*x_unit + x_bound, y_bound -(y[i]-min(y))*y_unit):
            first = True
            if first:
                xer = i
            else:
                yer = i
        
        find = True
        for i in range(max(xer)-min(xer)):
            if find == True:
                first = True
                if first == True:
                    if min(xer)+i in x:
                        line_x1 = x[i]
                        line_y1 = y[i]
                else:
                    if min(xer)+i in x:
                        line_x2 = x[i]
                        line_y2 = y[i]'''


        pygame.draw.line(display, yellow, (line_x1, line_y1), (line_x2, line_y2), width)

        #check lengths
        if len(x) != len(y):
            print('error non matching variable length')

        #draw points
        else:
            for i in range(len(x)):
                #points
                pygame.draw.circle(display, yellow, ((x[i]-min(x))*x_unit + x_bound, y_bound -(y[i]-min(y))*y_unit), point_size, point_size)


    def line(display, x, y, x_bound, y_bound, point_size=5, width=200, height=200, bourder=30, dash_width=4):
        x_unit = width/(max(x) - min(x))
        y_unit = height/(max(y) - min(y))

        #background
        pygame.draw.rect(display, green, (x_bound-bourder/2, y_bound-height-bourder/2, height+bourder, width+bourder))

        #x marks
        for i in range(round((max(x) - min(x))+1)):
            tick_x = x_bound-dash_width/2 + x_unit*i
            tick_y = y_bound+bourder/2-dash_width*3/2

            pygame.draw.rect(display, black, (tick_x, tick_y, dash_width, dash_width*3))
            write_text(str(i+min(x)), dash_width*3, black, bak_color, tick_x, tick_y+dash_width*6)

        #y marks
        for i in range(round((max(y) - min(y))+1)):
            tick_x = x_bound-bourder/2-dash_width*3/2
            tick_y = y_bound-dash_width/2 - y_unit*i

            pygame.draw.rect(display, black, (tick_x, tick_y, dash_width*3, dash_width))
            write_text(str(i+min(y)), dash_width*3, black, bak_color, tick_x-dash_width*3, tick_y)

        #check lengths
        if len(x) != len(y):
            print('error non matching variable length')

        #draw points
        else:
            for i in range(len(x)):
                #points
                pygame.draw.circle(display, yellow, ((x[i]-min(x))*x_unit + x_bound, y_bound -(y[i]-min(y))*y_unit), point_size, point_size)


#create display
pygame.display.set_caption('fuck a cuck')
display = pygame.display.set_mode((screen_width,screen_height))

run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #test grapher
    graph.scatter(display, ex_x, ex_y, screen_width/2, screen_height/2)

    graph.line(display, ex_x, ex_y, screen_width/2-400, screen_height/2+200)

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False