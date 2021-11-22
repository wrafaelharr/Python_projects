import pygame
import timeit
import numpy as np
import keyboard
from PIL import Image, ImageGrab
pygame.init()

#colors
bak_color = (90,90,200)
green = (0, 153 ,0)
red = (200, 0, 0)
blue = (0,0,150)

#screen size
screen_width = 800
screen_height = 400

#image data
im = ImageGrab.grab()
im = Image.open('C:\\Users\\Lrhgr\\Desktop\\hobbies\\programing\\image stuff\\image.jpg')
pixel_map = im.load()

#view facts
pos = [0, 0]
zoom = 1.1
res = 30

#move perams
speed = 40

#find screen info
screen_ratio = screen_height/screen_width
color = green

#create map
pix_width = round(res*zoom)
pix_height = round(pix_width*screen_ratio)
screen_map = np.zeros((pix_width, pix_height, 3))

#create display
pygame.display.set_caption('Computers view')
display = pygame.display.set_mode((screen_width, screen_height))

#produce screen
run = True
while run:
    #dellay and screen reset
    pygame.time.delay(50)
    display.fill(bak_color)

    #image data
    im = ImageGrab.grab()
    pixel_map = im.load()

    #get view info
    pix_width = round(res*zoom)
    pix_height = round(pix_width*screen_ratio)
    space_x = screen_width/pix_width
    space_y = screen_height/pix_height
    im_space = round(zoom*im.size[1]/pix_height)

    #get key press inputs
    keys = pygame.key.get_pressed()

    #move up
    if keys[pygame.K_UP]:
        pos[1] -= speed*zoom
    elif keys[pygame.K_DOWN]:
        pos[1] += speed*zoom

    #move over
    if keys[pygame.K_LEFT]:
        pos[0] -= speed*zoom
    elif keys[pygame.K_RIGHT]:
        pos[0] += speed*zoom

    #zoom
    if keys[pygame.K_o]:
        zoom += zoom/5
    elif keys[pygame.K_l]:
        zoom -= zoom/5

    #res
    if keys[pygame.K_i]:
        res -= 10
    elif keys[pygame.K_k]:
        res += 10

    #create maps
    screen_map = np.zeros((pix_width, pix_height, 3))
    black_x = np.zeros((pix_width))
    black_y = np.zeros((pix_height))

    #get to work
    for ix in range(pix_width):
            for iy in range(pix_height):
                #get color
                try:
                    if ix*im_space+pos[0] > 0 and iy*im_space+pos[1] > 0:
                        color = pixel_map[ix*im_space+pos[0], iy*im_space+pos[1]]
                    else:
                        color = green
                except:
                    color = green
                
                screen_map[ix][iy] = color

                #find darkness
                if color == (0, 0, 0):
                    color = red
                    black_x[ix] = (black_x[ix]+ix)/2
                    black_y[iy] += 1

                #draw pixels
                pygame.draw.rect(display, color, (ix*space_x, iy*space_y, round(space_x), round(space_y)))

    #find center of 
    #print(pos_y)
    #pygame.draw.circle(display, blue, (screen_width/2, pos_y), 12, 12)

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False