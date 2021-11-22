import pygame
import numpy as np
from PIL import Image, ImageGrab
pygame.init()

#screen size
scrn_size = (1200, 600)

#colors
bak_color = (90,90,200)
green = (0, 153 ,0)

#get screen shot
im = ImageGrab.grab()
#screenshot.show()

#get pixel data
pixel_map = im.load()

#perameters
view_pos = [0,0]
view_size = (100,130)
zoom = 7

#functions
def Screen(a,b):
    return (int(view_pos[0]+view_size[0]*(a/scrn_size[0])*zoom), int(view_pos[1]+view_size[1]*(b/scrn_size[1])*zoom))

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((scrn_size[0], scrn_size[1]))
display.fill(bak_color)

#produce screen
run = True
while run:
    #dellay and screen reset
    pygame.time.delay(70)

    #get key press inputs
    keys = pygame.key.get_pressed()

    #move the screen
    if keys[pygame.K_LEFT]:
        view_pos[0] -= 10
    elif keys[pygame.K_RIGHT]:
        view_pos[0] += 10
    if keys[pygame.K_UP]:
        view_pos[1] -= 10
    elif keys[pygame.K_DOWN]:
        view_pos[1] += 10

    #zoom
    if keys[pygame.K_z]:
        zoom += 1
    elif keys[pygame.K_x]:
        zoom -= 1

    #update screen shot
    if keys[pygame.K_u]:
        im = ImageGrab.grab()
        pixel_map = im.load()

    #draw image
    spacing = (scrn_size[0]/view_size[0], scrn_size[1]/view_size[1])
    for pos_y in range(view_size[1]):
        for pos_x in range(view_size[0]):
            screen_pos = (int(pos_x*spacing[0]+spacing[0]/2), int(pos_y*5+spacing[1]/2))
            pix_pos = Screen(screen_pos[0], screen_pos[1])

            try:
                color = pixel_map[pix_pos[0], pix_pos[1]]
            except:
                color = (0,0,0)

            pygame.draw.circle(display, color, screen_pos, 5, 5)

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False