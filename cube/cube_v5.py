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

#object classes
class cubes:
    xyz = (screen_width/2, screen_height/2, 0)
    ang = [0, 0]
    tilt = 0.2
    hwl = (100, 100, 100)
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
            top_points.append((self.hwl[1]*np.cos(self.ang[0]+self.space*i)+self.xyz[0],
                                self.hwl[1]*self.tilt*np.sin(self.ang[0]+self.space*i) + self.xyz[1] - self.hwl[0]/2))

            bot_points.append((self.hwl[1]*np.cos(self.ang[0]+self.space*i)+self.xyz[0],
                                self.hwl[1]*self.tilt*np.sin(self.ang[0]+self.space*i) + self.xyz[1] + self.hwl[0]/2))
        
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

#find angles and postions


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
        cube1.ang[1] += 0.1
    if keys[pygame.K_DOWN]:
        cube1.ang[1] -= 0.1
    if keys[pygame.K_LEFT]:
        cube1.ang[0] -= 0.04
    if keys[pygame.K_RIGHT]:
        cube1.ang[0] += 0.04

    #draw cube
    cube1.draw()

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False