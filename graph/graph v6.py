import pygame
import pandas as pd
import numpy
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
bak_color = (76, 217, 191)
yellow = (255, 255, 0)
blue = (87, 233, 248)
green = (30, 180, 30)
red = (200,0,0)
black = (0,0,0)

#helpful funcs
def write_text(string, size, color, highlight, x, y):
    font = pygame.font.Font('Aaargh.ttf', size)
    text = font.render(string, True, color, highlight)
    textRect = text.get_rect()
    textRect.center = (x, y)
    display.blit(text, textRect)

#graph class
class plots:
    x = 0
    y = 0
    size = 200
    color = (93, 248, 87)
    ui_color = (87, 233, 248)
    weight_and_bias = (0,0)
    line = []
    scatter = ([])
    width = size*1.5
    height = size
    ticks = 7
    def draw(self):
        #background    
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.size))

        #find edges
        if self.scatter:
            #find minimums
            if min(self.scatter[0])-10 > 0:
                gu_min_x = min(self.scatter[0])-10
            else:
                gu_min_x = 0

            all_y = self.scatter[1] + self.line
            if min(all_y)-10 > 0:
                gu_min_y = min(all_y)-10
            else:
                gu_min_y = 0
            
            #find maximums
            gu_max_x = max(self.scatter[0]+[len(self.line)])
            gu_max_y = max(all_y)
        else:
            gu_min_x = 0
            gu_min_y = 0
            gu_max_x = 0
            gu_max_y = 0

        #spacing ratio
        gu_width = gu_max_x - gu_min_x
        gu_height = gu_max_y - gu_min_y
        if gu_width and gu_height:
            spacing_ratio = (self.width/gu_width, self.height/gu_height)
        else:
            spacing_ratio = (0, 0)
        
        #the spacings
        spacing = (self.width/self.ticks, self.height/self.ticks)
        label_spacing = (gu_width/self.ticks, gu_height/self.ticks)

        #extra shortcuts
        base = self.y + self.height

        #draw ticks and labels
        for i in range(self.ticks+1):
            #ticks
            pygame.draw.rect(display, (0,0,0), (self.x+spacing[0]*i, base-4, 3, 8))
            pygame.draw.rect(display, (0,0,0), (self.x-4, base-3-spacing[1]*i, 8, 3))

            #labels
            if i%2:
                write_text(str(round(i*label_spacing[0],1)), 15, black, bak_color, self.x+spacing[0]*i, base+30)
            else:
                write_text(str(round(i*label_spacing[0],1)), 15, black, bak_color, self.x+spacing[0]*i, base+15)
            write_text(str(round(i*label_spacing[1],1)), 15, black, bak_color, self.x-30, base-4-spacing[1]*i)
        
        #scatter
        if self.scatter:
            for i in range(len(self.scatter[0])):
                x = self.x + spacing_ratio[0]*self.scatter[0][i]
                y = base - spacing_ratio[1]*self.scatter[1][i]
                pygame.draw.circle(display, yellow, (x, y), 5, 5)
        
        #line
        for i in range(len(self.line)-1):
            x1 = self.x+spacing_ratio[0]*i
            x2 = self.x+spacing_ratio[0]*(i+1)
            y1 = base-spacing_ratio[1]*self.line[i]
            y2 = base-spacing_ratio[1]*self.line[i+1]
            pygame.draw.line(display, blue, (x1, y1), (x2, y2), 5)

        #weight and biase
        if self.weight_and_bias != (0,0):
            width = self.size*1.5
            height = self.size
            x1 = self.x
            x2 = self.x + 10000*spacing_ratio[0]
            y1 = self.y + height - self.weight_and_bias[1]*spacing_ratio[1]
            y2 = y1 - self.weight_and_bias[0]*spacing_ratio[1]
            overlap_y = (self.weight_and_bias[0]+self.weight_and_bias[1])*spacing_ratio[1] - height
            overlap_x = 10000*spacing_ratio[0] - width
            sub_y = (10000*spacing_ratio[1]*overlap_x)/self.weight_and_bias[0]
            sub_x = (10000*spacing_ratio[0]*overlap_y)/self.weight_and_bias[0]
            '''
            if overlap_y > 0:
                y2 += overlap_y
                x2 -= sub_x'''
            pygame.draw.line(display, red, (int(x1), int(y1)), (int(x2), int(y2)), 5)
        

#create plots
plot1 = plots()

#create display
pygame.display.set_caption('graphs')
display = pygame.display.set_mode((screen_width, screen_height))

run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #draw graph
    plot1.x = screen_width/2
    plot1.y = screen_height/2
    plot1.scatter = ([1,9,8,5,6,7,3], [3,4,3,2,1,2,3])
    plot1.line = [1,2,3,3,4,2]
    plot1.weight_and_bias = (500,1)
    plot1.draw()

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False