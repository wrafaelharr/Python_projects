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

class cubes:
    xy = [screen_width/2, screen_height/2, 0]
    ang = [0, 0]
    tilt = 0.2
    hwl = [100, 100, 100]
    size = 1
    space = np.pi/2
    def draw(self):
        #loop ang rote
        if self.ang[0] > 2*np.pi:
            self.ang[0] = 0
        elif self.ang[0] < 0:
            self.ang[0] = 2*np.pi
        #loop ang tilt
        if self.ang[1] > np.pi/2:
            self.ang[1] = np.pi/2
        elif self.ang[1] < -np.pi/2:
            self.ang[1] = -np.pi/2
        
        #attach angle and tilt
        self.tilt = self.ang[1]/np.pi/2

        #find top and bottom points
        top_points = []
        bot_points = []
        for i in range(4):
            top_points.append((self.size*self.hwl[1]*np.cos(self.ang[0]+self.space*i)+self.xy[0],
                                self.size*self.hwl[1]*self.tilt*np.sin(self.ang[0]+self.space*i) + self.xy[1] - self.size*self.hwl[0]/2))

            bot_points.append((self.size*self.hwl[1]*np.cos(self.ang[0]+self.space*i)+self.xy[0],
                                self.size*self.hwl[1]*self.tilt*np.sin(self.ang[0]+self.space*i) + self.xy[1] + self.size*self.hwl[0]/2))
        
        #find side points
        A = (top_points[2], top_points[3], 
            bot_points[3], bot_points[2])
        B = (top_points[3], top_points[0], 
            bot_points[0], bot_points[3])
        C = (top_points[0], top_points[1], 
            bot_points[1], bot_points[0])
        D = (top_points[1], top_points[2], 
            bot_points[2], bot_points[1])

        #draw or bottom
        if self.ang[1] > 0:
            pygame.draw.polygon(display, red, top_points)
        else:
            pygame.draw.polygon(display, red, bot_points)

        #draw sides
        if self.ang[0] >= np.pi/4 and self.ang[0] <= 3*np.pi/4:
            pygame.draw.polygon(display, blue, C)
            pygame.draw.polygon(display, green, B)
        elif self.ang[0] >= 3*np.pi/4 and self.ang[0] <= 5*np.pi/4:
            pygame.draw.polygon(display, blue, A)
            pygame.draw.polygon(display, green, B)
        elif self.ang[0] >= 5*np.pi/4 and self.ang[0] <= 7*np.pi/4:
            pygame.draw.polygon(display, blue, A)
            pygame.draw.polygon(display, green, D)
        elif self.ang[0] >= 7*np.pi/4 or self.ang[0] <= np.pi/4:
            pygame.draw.polygon(display, blue, C)
            pygame.draw.polygon(display, green, D)

#camera atributes
camera_xyz = [200,50,200]
camera_ang = 0
speed = 30

#box attributes
box_xyz = [300,0,400]
box_ang = 0

#create objects
cube1 = cubes()

#create display
pygame.display.set_caption('cubes')
display = pygame.display.set_mode((screen_width, screen_height))

#main
run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #tilt cube
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        camera_xyz[2] += speed*np.cos(camera_ang)
        camera_xyz[0] += speed*np.sin(camera_ang)
    if keys[pygame.K_DOWN]:
        camera_xyz[2] -= speed*np.cos(camera_ang)
        camera_xyz[0] -= speed*np.sin(camera_ang)
    if keys[pygame.K_LEFT]:
        camera_ang += 0.04
    if keys[pygame.K_RIGHT]:
        camera_ang -= 0.04
    
    #change size
    if keys[pygame.K_p]:
        cube1.size -= 0.04
    elif keys[pygame.K_l]:
        cube1.size += 0.04
    
    #find x z dist to box
    cube_distx = box_xyz[0]-camera_xyz[0]
    cube_distz = box_xyz[2]-camera_xyz[2]
    cube_distxz = (cube_distx**2+cube_distz**2)**.5
    if int(cube_distx/cube_distxz)%2 != True:
        ang3 = np.arcsin(cube_distx/cube_distxz)
    else:
        ang3 = np.pi*3/2 - np.arcsin(cube_distx/cube_distxz)
    ang2 = ang3 - camera_ang

    #move x
    cube1.xy[0] = screen_width/2-cube_distxz*np.sin(ang2)

    #find dist
    cube_dist = (camera_xyz[1]**2 + cube_distxz**2)**.5
    if int((camera_xyz[1]-box_xyz[1])/cube_dist)%2 != True:
        ang4 = np.arcsin((camera_xyz[1]-box_xyz[1])/cube_dist)
    else:
        ang4 = np.pi*3/2 - np.arcsin((camera_xyz[1]-box_xyz[1])/cube_dist)

    #move y
    cube1.xy[1] = screen_height - cube_dist*np.sin(ang4)
    cube1.ang[1] = (np.pi/2)-ang4

    #change siize
    norm_dist = 400
    cube1.size = norm_dist/cube_dist
    
    #rotate cube
    
    cube1.ang[0] = np.pi/2-camera_ang

    #draw cube
    cube1.draw()

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False