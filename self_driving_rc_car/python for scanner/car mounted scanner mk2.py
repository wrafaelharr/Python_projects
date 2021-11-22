import matplotlib.pyplot as plt
import time
import serial
import pygame
import numpy as np
pygame.init()

#open com
ser = serial.Serial('COM3',9600)

#colors
bak_color = (100,200,0)
red = (200,0,0)
blue = (0,200,240)

#screen demensions
screen_width = 1200
screen_height = 790

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen_width,screen_height))

#varable defs
int_b = 0
angle = 0
dist = 0
dist2 = 0
distances1 = []
distances2 = []
angles = []

run = True
while run:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    if ser.readline()[:] != "b'\xff37\r\n'": # Make sure that the read line isn't this as this is the first line outputted from the serial and it causes errors in the code
        b = ser.readline() # read a byte string line from the Arduino's serial output
        string_n = b.decode() # decode byte string into regular Python string
        int_b = float(string_n)
        
    #interpret data
    if int_b > 9999:
        dist = int(((int_b % 100)/97)*700)
        dist2 = int((((int_b / 100) % 100)/97)*700)
    elif int_b > 0:
        angle = int(int_b % 1000)
    
    distances1.append(dist)
    distances2.append(dist2)
    angles.append(angle)
    
    if len(angles) > 40:
        del distances1[0], distances2[0], angles[0]

    for i in range(len(angles)):
        x1 = int(screen_width/2 + np.cos(angles[i])*distances1[i])
        y1 = int(screen_height/2 + np.sin(angles[i])*distances1[i])
        x2 = int(screen_width/2 - np.cos(angles[i])*distances1[i])
        y2 = int(screen_height/2 - np.sin(angles[i])*distances1[i])
        
        pygame.draw.circle(display, red, (x1, y1), 5, 5)
        pygame.draw.circle(display, red, (x2, y2), 5, 5)
    
    print(x1)
    
    #update screen
    pygame.display.update()
    
    #quite
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            run = False
            ser.close()