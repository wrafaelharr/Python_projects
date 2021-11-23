import pygame
import numpy as np
from PIL import Image
pygame.init()

#get image
monkey = 'C:\\Users\\Lrhgr\\Documents\\GitHub\\art\\monkey pics\\image.jpg'
im = Image.open(monkey)

#get size
im_width, im_height = im.size

#get pixel data
pixel_map = im.load()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
bak_color = (90,90,200)
green = (0, 153 ,0)

#functions
def map_to_scrn(map_size, scrn_size, point):
    margin_x = 30
    margin_y = 25

    x_cons = (scrn_size[0] - margin_x*2)/map_size[0]
    y_cons = (scrn_size[1] - margin_y*2)/map_size[1]

    #find new point
    pos_x = point[0]*x_cons + margin_x
    pos_y = point[1]*y_cons + margin_y

    return pos_x, pos_y

#veriables
res = 100
width_pos = -1
height_pos = 0
wid_per_pos = int(im_width/res)
hi_per_pos = int(im_height/res)
scrn_size = (screen_width,screen_height)

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((screen_width,screen_height))
display.fill(bak_color)

#produce screen
run = True
while run:
    #dellay and screen reset
    pygame.time.delay(10)
    #display.fill(bak_color)

    #increase counter
    width_pos += 1
    if width_pos > res:
        width_pos = 0
        height_pos += 1

        if height_pos > res:
            height_pos = 0
    
    try:
        #find pixel pos
        pos = (width_pos*wid_per_pos, height_pos*hi_per_pos)
        color = pixel_map[pos[0], pos[1]]

        #draw circle
        pygame.draw.circle(display, color, (map_to_scrn(im.size, scrn_size, (width_pos*wid_per_pos, height_pos*hi_per_pos))), 5, 5)
    except:
        print('DANG')

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False