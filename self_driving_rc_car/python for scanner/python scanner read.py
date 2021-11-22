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

#ancor
mid_x = []
mid_y = []
for i in range(100):
    mid_x.append(screen_width/2)
    mid_y.append(screen_height/2)
ang = 0
dist = 0
count = 0

run = True
while run:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)
    
    #increase count
    count = count+1
    if count > len(mid_x)-1:
        count = 0
    #read serial
    st = ser.readline()
    
    if ser.readline()[:] != "b'\xff37\r\n'": # Make sure that the read line isn't this as this is the first line outputted from the serial and it causes errors in the code
            b = ser.readline() # read a byte string line from the Arduino's serial output
            string_n = b.decode() # decode byte string into regular Python string
            int_b = float(string_n)
    
    #seperate data
    if int_b > 10000:
        ang = (int_b-10000)*np.pi/180
    elif int_b < 10000:
        if int_b < 1300:
            dist = int_b
        else:
            dist = 1300
            
    
    #draw circles
    try:
        mid_x[count] = screen_width/2+dist*np.cos(ang)/3
        mid_y[count] = screen_height/2-dist*np.sin(ang)/3
    except:
        print(count)
    
    #target
    pygame.draw.circle(display, blue, (int(screen_width/2), int(screen_height/2)), 15, 15)
    pygame.draw.circle(display, blue, (int(screen_width/2), int(screen_height/2)), 200, 100)
    pygame.draw.circle(display, blue, (int(screen_width/2), int(screen_height/2)), 400, 100)
    pygame.draw.circle(display, blue, (int(screen_width/2), int(screen_height/2)), 600, 100)
    
    #distances
    for i in range(6):
        if i != 2 and i != 4 and i != 0:
            OUT = str(100*i)+'mm'
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(OUT, True, bak_color, blue)
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/2-10-100*i)
            display.blit(text, textRect) 
        elif i == 0:
            OUT = str(100*i)
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(OUT, True, bak_color, blue)
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/2)
            display.blit(text, textRect)
        else:
            OUT = str(100*i)+'mm'
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(OUT, True, blue, bak_color)
            textRect = text.get_rect()
            textRect.center = (screen_width/2, screen_height/2-10-100*i)
            display.blit(text, textRect)  
    
    #draw objs   
    for i in range(len(mid_x)):
        pygame.draw.circle(display, red, (int(mid_x[i]), int(mid_y[i])), 5, 5)
    
    #update screen
    pygame.display.update()
    
    #quite
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            run = False
            ser.close()