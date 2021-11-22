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

#get screen shot
im = ImageGrab.grab()
#screenshot.show()

#get pixel data
pixel_map = im.load()

#perameters
view_pos = [601.37, 295.71]
view_ratio = (2.5,4)
res = 15
zoom = 0.006723
pan_speed = 20
light_threshold = 190
zoom_h = view_ratio[1]/view_ratio[0]
#print(int(res*(view_ratio[1]/view_ratio[0])))

#states
learn = False
stop = True

#screen size
scrn_size = (int(view_ratio[0]*100*1.5), int(view_ratio[1]*100*1.5))

#ratios
x_res_ratio = scrn_size[0]/res
y_res_ratio = scrn_size[1]/int(res*(view_ratio[1]/view_ratio[0]))

#functions
def screen(x,y):
    zoom_h2 = zoom_h*zoom
    x_pos_const = x/scrn_size[0]
    y_pos_const = y/scrn_size[1]

    sample_pos_x = im.size[0]*x_pos_const*zoom
    sample_pos_y = im.size[1]*y_pos_const*zoom_h2

    return sample_pos_x, sample_pos_y

#encoder
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?!;:'
deco = abc

#decoder
enco = {}
for i in range(len(deco)):
    enco[deco[i]] = i

#create asociation networks
pixel_h = int(res*(view_ratio[1]/view_ratio[0]))
pixel_w = res
asoc_cube = np.zeros((pixel_h, pixel_w, len(deco)))
guess = np.zeros(len(deco))

#create display
pygame.display.set_caption('snake')
display = pygame.display.set_mode((scrn_size[0], scrn_size[1]))

#produce screen
run = True
while run:
    #dellay and screen reset
    pygame.time.delay(100)
    display.fill(bak_color)

    #get key press inputs
    keys = pygame.key.get_pressed()

    #move around
    if keys[pygame.K_LEFT]:
        view_pos[0] -= screen(x_res_ratio, y_res_ratio)[0]
    elif keys[pygame.K_RIGHT]:
        view_pos[0] += screen(x_res_ratio, y_res_ratio)[0]
    if keys[pygame.K_UP]:
        view_pos[1] -= screen(x_res_ratio, y_res_ratio)[1]
    elif keys[pygame.K_DOWN]:
        view_pos[1] += screen(x_res_ratio, y_res_ratio)[1]
    
    #zooom
    if keys[pygame.K_z]:
        zoom += 0.1*zoom
    elif keys[pygame.K_x]:
        zoom -= 0.1*zoom
    
    #learn
    if keys[pygame.K_l]:
        learn = True
        label = '@'
        while label not in deco:
            label = input('What letter is this: ')
        label = enco[label]

    #update screen shot
    if keys[pygame.K_u]:
        im = ImageGrab.grab()
        pixel_map = im.load()

    #draw circles
    sline_y = int(pixel_h/2)
    spaces = []
    for x_pos in range(res):
        for y_pos in range(pixel_h):

            #position
            pos_x = x_pos*x_res_ratio + x_res_ratio/2
            pos_y = y_pos*y_res_ratio + y_res_ratio/2

            #find color
            try:
                color = pixel_map[screen(pos_x,pos_y)[0]+view_pos[0], screen(pos_x,pos_y)[1]+view_pos[1]]
            except:
                color = (0,0,0)
            
            #gray scale
            avg_light = (color[0]+color[1]+color[2])/3

            #highlights new data
            if avg_light < light_threshold:
                pixel_map[screen(pos_x,pos_y)[0]+view_pos[0], screen(pos_x,pos_y)[1]+view_pos[1]] = red

                guess += asoc_cube[y_pos][x_pos]
                #train asoc
                if learn == True:
                    asoc_cube[y_pos][x_pos][label] += 1
                    keyboard.press_and_release('RIGHT')
                    
            #find spaces
            if y_pos == sline_y:
                if avg_light > light_threshold:
                    color = green
                    for i in range(int(pixel_h/2)+1):
                        height = pos_y - i*y_res_ratio
                        height2 = pos_y + i*y_res_ratio
                        
                        try:
                            color = pixel_map[screen(pos_x,height)[0]+view_pos[0], screen(pos_x,height)[1]+view_pos[1]]
                            color2 = pixel_map[screen(pos_x,height2)[0]+view_pos[0], screen(pos_x,height2)[1]+view_pos[1]]
                        except:
                            color = (0,0,0)
                            color2 = (0,0,0)
                            
                        #gray scale
                        avg_light = (color[0]+color[1]+color[2])/3
                        avg_light2 = (color2[0]+color2[1]+color2[2])/3
                        
                        #top side
                        if avg_light > light_threshold:
                            pygame.draw.circle(display, green, (pos_x, height), 12, 2)
                        else:
                            break
                        #bottom side
                        if avg_light2 > light_threshold:
                            pygame.draw.circle(display, green, (pos_x, height2), 12, 2)
                        else:
                            break
                        
                        #find the space
                        if i == int(pixel_h/2):
                            spaces.append(x_pos)

            #draw
            pygame.draw.circle(display, color, (pos_x, pos_y), 10, 10)
    learn = False

    #guess
    if keys[pygame.K_g]:
        #find final guess
        for i in range(len(guess)):
            if guess[i] == max(guess):
                letter = i
        print(deco[letter])

    #draw spaces
    for space in spaces:
        pygame.draw.rect(display, green, (space*x_res_ratio+5, 0, 10, scrn_size[1]))

    #check for each space
    if pixel_w-1 in spaces and pixel_w-2 not in spaces and stop:
        #guess
        keyboard.press_and_release('g')

        #online work once
        stop = False

    if pixel_w-1 not in spaces or pixel_w-2 in spaces:
        view_pos[0] += screen(x_res_ratio, y_res_ratio)[0]/2
        stop = True

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False