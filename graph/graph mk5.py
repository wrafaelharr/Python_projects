import pygame
import numpy
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

#graph class
class plots:
    x = 0
    y = 0
    size = 200
    color = (93, 248, 87)
    ui_color = (87, 233, 248)
    line_data = []
    scatter_data = ([])
    def draw(self):
        #background
        plot_width = self.size*1.5       
        pygame.draw.rect(display, self.color, (self.x, self.y, plot_width, self.size))

        #graph parts
        if self.line_data or self.scatter_data:
            #find x and y max
            if self.line_data and self.scatter_data:               
                max_x = numpy.max(self.scatter_data[0])
                max_y = numpy.max(self.scatter_data[1])
                if max_x < len(self.line_data)-1:
                    max_x = len(self.line_data)-1
                if max_y < numpy.max(self.line_data):
                    max_y = numpy.max(self.line_data)
            elif self.scatter_data:
                max_x = numpy.max(self.scatter_data[0])
                max_y = numpy.max(self.scatter_data[1])
            else:
                max_x = len(self.line_data)-1
                max_y = numpy.max(self.line_data)
            
            #find spacing
            num_marks = 7
            label_spacing = (max_x/num_marks, max_y/num_marks)
            spacing = (plot_width/num_marks, self.size/num_marks)
            spacing_ratio = (spacing[0]/label_spacing[0], spacing[1]/label_spacing[1])

            #marks
            base = self.y + self.size
            for i in range(num_marks+1):
                pygame.draw.rect(display, (0,0,0), (self.x+spacing[0]*i, base-4, 3, 8))
                pygame.draw.rect(display, (0,0,0), (self.x-4, base-3-spacing[1]*i, 8, 3))

                #labels
                write_text(str(round(i*label_spacing[0],1)), 9, black, bak_color, self.x+spacing[0]*i, base+15)
                write_text(str(round(i*label_spacing[1],1)), 9, black, bak_color, self.x-15, base-4-spacing[1]*i)
            
            #scatter
            if self.scatter_data:
                for i in range(len(self.scatter_data[0])):
                    x = self.x+spacing_ratio[0]*self.scatter_data[0][i]
                    y = base-spacing_ratio[1]*self.scatter_data[1][i]
                    pygame.draw.circle(display, yellow, (x, y), 5, 5)
            
            #line
            for i in range(len(self.line_data)-1):
                x1 = self.x+spacing_ratio[0]*i
                x2 = self.x+spacing_ratio[0]*(i+1)
                y1 = base-spacing_ratio[1]*self.line_data[i]
                y2 = base-spacing_ratio[1]*self.line_data[i+1]
                pygame.draw.line(display, blue, (x1, y1), (x2, y2), 5)

#create display
pygame.display.set_caption('graphs')
display = pygame.display.set_mode((screen_width, screen_height))

#create plots
plot1 = plots()
plot2 = plots()

run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #screen positions
    middle_spacing = 100
    height = screen_height*3/5
    box_x1 = screen_width/2 -middle_spacing -plot1.size*1.5
    box_x2 = screen_width/2 + plot1.size

    #draw graph1
    plot1.scatter_data = ([1, 2, 3, 4, 2], [1, 4, 9, 16, 18])
    plot1.line_data = [1, 4, 5, 20,5,4,3,3,1]
    plot1.x = box_x1
    plot1.y = height
    plot1.draw()

    #draw graph2
    plot2.x = box_x2
    plot2.y = height
    plot2.line_data = [100,70,50,30,20,15,10,10,10]
    plot2.draw()

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False