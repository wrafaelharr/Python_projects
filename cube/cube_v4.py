import pygame
import pandas as pd
import numpy as np
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

#cube start locaton
cube_xyz = (0,12,12)
cube_whl = (100,50,100)
cube_xy = [screen_width/2, screen_height/2]
cube_ang = [0,0]
point_spacing = np.pi/2
cubeT__size = 100
top_height = 0.2
cube_width = 0
front_panelx = False
switch = False
count = 0
change_color = False

#create display
pygame.display.set_caption('graphs')
display = pygame.display.set_mode((screen_width, screen_height))

run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #switch
    if front_panelx:
        print(switch)
        switch = min(front_panelx)+cube_width/2 < cube_xy[0]

    #rotate
    cube_ang[0] += 0.01

    #find cube points
    top_points = []
    bottom_points = []
    left_points = []
    side_points = []
    front_panelx = []
    for i in range(4):
        x = cube_xy[0] + cubeT__size*np.cos(cube_ang[0] + point_spacing*i)
        y = cube_xy[1] - top_height*cubeT__size*np.sin(cube_ang[0] + point_spacing*i)
        top_points.append((x, y + cube_whl[1]))
        bottom_points.append((x, y - cube_whl[1]))
    
    #find front panel
    for i in top_points:
        if i[1] > (cube_xy[1] + cube_whl[1]):
            left_points.append(i)
    left_points.append(left_points[0])
    del left_points[0]
    for i in bottom_points:
        if i[1] > (cube_xy[1] - cube_whl[1]):
            left_points.append(i)
    
    #find side panel
    for i in left_points:
        front_panelx.append(i[0])
    cube_width = max(front_panelx)-min(front_panelx)

    if min(front_panelx)+cube_width/2 < cube_xy[0]:
        for i in top_points + bottom_points:
            if i[0] > cube_xy[0]:
                side_points.append(i)
    else:
        for i in top_points + bottom_points:
            if i[0] < cube_xy[0]:
                side_points.append(i)

    #correct side points
    side_points.append(side_points[-2])
    del side_points[-3]

    #switch sides
    if switch != min(front_panelx)+cube_width/2 < cube_xy[0]:
        count += 1
        change_color = True
    else:
        change_color = False
    
    #print(change_color)

    #draw cube
    pygame.draw.polygon(display, red, bottom_points)

    #sides
    pygame.draw.polygon(display, green, left_points)
    pygame.draw.polygon(display, blue, side_points)

    #poop
    pygame.draw.circle(display, yellow, (min(front_panelx), cube_xy[1] - cube_whl[1]), 5, 5)
    pygame.draw.circle(display, yellow, side_points[-1], 5, 5)

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False