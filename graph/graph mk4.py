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
bak_color = (76, 217, 191)
yellow = (255, 255, 0)
blue = (87, 233, 248)
green = (30, 180, 30)
black = (0,0,0)

#helpful funcs
def write_text(string, size, color, highlight, x, y):
    font = pygame.font.Font('Shadded South Personal Use.ttf', size)
    text = font.render(string, True, color, highlight)
    textRect = text.get_rect()
    textRect.center = (x, y)
    display.blit(text, textRect)

#classes
class plots:
    x = 0
    y = 0
    size = 200
    color = (93, 248, 87)
    ui_color = (87, 233, 248)
    line_data = []
    scatter_data = ([])
    def draw():
        highest_y = 0
        highest_x = 0

        #background
        back_width = plots.size*1.5       
        pygame.draw.rect(display, plots.color, (plots.x, plots.y, back_width, plots.size))

        #labels
        max_x = numpy.max(plots.scatter_data[0])
        max_y = numpy.max(plots.scatter_data[1])
        if max_x < len(plots.line_data):
            max_x = len(plots.line_data)
        if max_y < numpy.max(plots.line_data):
            max_y = numpy.max(plots.line_data)
        labels_x = max_x/7
        labels_y = max_y/7

        #marks
        space_x = back_width/7
        space_y = plots.size/7
        for i in range(8):
            #x marks
            pygame.draw.rect(display, (0,0,0), (plots.x+space_x*i, plots.y+plots.size-4, 3, 8))
            write_text(str(round(i*labels_x,1)), 9, black, bak_color, plots.x+space_x*i, plots.y+plots.size+12)
            
            #y marks
            pygame.draw.rect(display, (0,0,0), (plots.x-4, plots.y+space_y*i-3, 8, 3))
            write_text(str(round((7-i)*labels_y,1)), 9, black, bak_color, plots.x-15, plots.y+space_y*i-3)

        #draw scatter
        amount = len(plots.scatter_data[0])
        base = plots.y+plots.size
        for i in range(amount):
            pygame.draw.circle(display, yellow, (plots.x+plots.scatter_data[0][i]*back_width/max_x, base-plots.scatter_data[1][i]*plots.size/max_y), 7, 7)
        
        #draw line
        for i in range(len(plots.line_data)-1):
            pygame.draw.line(display, blue, (plots.x+i*space_x, base-plots.line_data[i]*space_y), (plots.x+(i+1)*space_x, base-plots.line_data[i+1]*space_y), 5)

#create display
pygame.display.set_caption('fuck a cuck')
display = pygame.display.set_mode((screen_width,screen_height))

#create plots
plot1 = plots
plot2 = plots

run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #draw graph1
    plot1.scatter_data = ([1, 2, 3, 4, 2], [1, 4, 9, 16, 18])
    plot1.line_data = [1, 4, 5, 2]
    plot1.x = screen_width/2 - plot1.size*2
    plot1.y = screen_height/2 - plot1.size/2
    plot1.draw()

    #draw graph2
    plot2.x = screen_width/2 + plot1.size
    plot2.y = screen_height/2 - plot1.size/2
    plot2.scatter_data = ([])
    #plot2.draw()

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False