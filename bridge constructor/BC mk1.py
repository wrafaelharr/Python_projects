import pygame
import numpy as np
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
sky_blue = (135, 206, 235)
brown = (152, 118, 84)
yellow = (255, 255, 0)
silver = (192, 192, 192)

#game options
land1 = 250
land2 = 200
land_width1 = 150
land_width2 = 150

#functions
def draw_anchor(xy):
    x = xy[0]
    y = xy[1]
    radius = 7
    bourder = 2
    pygame.draw.circle(display, yellow, (int(x), int(y)), radius, radius)
    pygame.draw.circle(display, (0,0,0), (int(x), int(y)), radius, bourder)

def draw_beams(anchor1, anchor2):
    pygame.draw.line(display, silver, anchor1, anchor2, 8)

#hold data
anchors = [(land_width1, screen_height-land1),(screen_width-land_width2, screen_height-land2)]
beams = []
dist_to = 0

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((screen_width,screen_height))

while True:
    #menu
    game = True
    while game:
        #dellay and screen reset
        pygame.time.delay(30)
        display.fill(sky_blue)

        #mouse points
        mouse = pygame.mouse.get_pos()

        #draw ground
        pygame.draw.rect(display, brown, (0, screen_height-land1, land_width1, land1))
        pygame.draw.rect(display, brown, (screen_width-land_width2, screen_height-land2, land_width2, land2))

        #find closest anchor
        which = 0
        this_one = 0
        dif = 300
        for i in anchors:
            which += 1

            x = i[0]
            y = i[1]

            mouseX = mouse[0]
            mouseY = mouse[1]

            if np.absolute(mouseX-x) < dif:
                dif = np.absolute(mouseX-x)
                this_one = which
        this_one -= 1
        
        #find dist
        if this_one > -1:
            x = anchors[this_one][0]
            y = anchors[this_one][1]
            dist_to = ((np.absolute(mouse[0]-x))*2+(np.absolute(mouse[1]-y))*2)**0.5
        
        #draw beams
        for i in beams:
            anch1 = i[0]
            anch2 = i[1]

            draw_beams(anchors[anch1], anchors[anch2])

        #example
        if dist_to < 20:
            draw_beams(mouse, anchors[this_one])

        #no overlap
        if dist_to > 6:
            #mouse anchor
            draw_anchor((mouse))
        else:
            if pygame.mouse.get_pressed()[0] and dist_to > 6:
                beams.append((this_one,len(anchors)-1)) 

        #draw anchors
        for i in anchors:
            draw_anchor(i)

        #create new anchors
        if pygame.mouse.get_pressed()[0] and dist_to > 6:
            anchors.append(mouse)
            beams.append((this_one,len(anchors)-1))

        #update display
        pygame.display.update()

        #quite properly
        for event in pygame.event.get() :  
            if event.type == pygame.QUIT : 
                pygame.quit() 
            pygame.display.update()