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
silver = (150, 150, 150)
white = (230,210,200)

#game info
landA_h = 250
landB_h = 200
landC_h = 100
landA_w = 150
landB_w = 150
landC_w = 100

#hold data
anchors = [(landA_w, screen_height-landA_h),(screen_width-landB_w, screen_height-landB_h),(screen_width/2,screen_height-landC_h)]
anchor_forces = [0,0,0]
beams = []
select = -1
test = False

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

def find_dist(xy1,xy2):
    x1 = xy1[0]
    y1 = xy1[1]

    x2 = xy2[0]
    y2 = xy2[1]

    return ((np.absolute(x1-x2))*2+(np.absolute(y1-y2))*2)**0.5

def draw_text(OUT, color, bak_color, size, x, y):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(OUT, True, color, bak_color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    display.blit(text, textRect)

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((screen_width,screen_height))

#main
while True:
    #game
    game = True
    while game:
        #dellay and screen reset
        pygame.time.delay(30)
        display.fill(sky_blue)

        #mouse points
        mouse = pygame.mouse.get_pos()

        #draw ground
        pygame.draw.rect(display, brown, (0, screen_height-landA_h, landA_w, landA_h))
        pygame.draw.rect(display, brown, (screen_width-landB_w, screen_height-landB_h, landB_w, landB_h))
        pygame.draw.rect(display, brown, (screen_width/2-landC_w/2, screen_height-landC_h, landC_w, landC_h))

        #new beams
        select_dist = find_dist(anchors[select],mouse)
        if select > -1 and select_dist < 30:
            draw_beams(anchors[select],mouse)
            if select_dist > 6 and pygame.mouse.get_pressed()[0]:
                if dist_to < 6:
                    beams.append((select,this_one))
                else:
                    anchors.append(mouse)
                    anchor_forces.append(1)
                    beams.append((select,len(anchors)-1))

        else:
            select = -1
        
        #draw beams
        for i in beams:
            draw_beams(anchors[i[0]],anchors[i[1]])

        #draw anchors
        for i in anchors:
            draw_anchor(i)

        #find closest x wise
        current_min = 300
        count = 0
        this_one = -1
        for i in anchors:
            diferrence = np.absolute(mouse[0] - i[0])
            if diferrence <  current_min:
                current_min = diferrence
                this_one = count
            count += 1

        #find distance to closest
        dist_to = find_dist(anchors[this_one],mouse)
        
        #no overlap
        if dist_to > 6 and test == False:
            #mouse anchor
            draw_anchor((mouse))
        else:
            if pygame.mouse.get_pressed()[0]:
                select = this_one
        
        #test
        for i in range(len(anchors)):
            anchors[i] = (anchors[i][0], anchors[i][1]+anchor_forces[i])

        #explain text
        explain_text = 'press T: test'
        draw_text(explain_text, white, sky_blue, 30, screen_width/2, 40)
        
        #update display
        pygame.display.update()

        #quite properly
        for event in pygame.event.get() :  
            if event.type == pygame.QUIT : 
                pygame.quit() 