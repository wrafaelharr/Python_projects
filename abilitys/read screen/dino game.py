import pygame
import timeit
import numpy as np
import keyboard
from PIL import Image, ImageGrab
pygame.init()

#screen size
scrn_size = (1700, 600)

#colors
bak_color = (90,90,200)
green = (0, 153 ,0)

#get screen shot
im = ImageGrab.grab()
#screenshot.show()

#get pixel data
pixel_map = im.load()

#perameters
view_pos = [495,-5]
view_size = (200,100)
zoom = 5
max_view = 1600
distance = 50
time = 0
re_time2 = 1.8

#veriabels
speeds = []
score = 0
old_score = 0
time_change = 3
changed = True

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
    #pygame.time.delay(1)
    display.fill(bak_color)

    #get key press inputs
    keys = pygame.key.get_pressed()

    #zoom
    if keys[pygame.K_z]:
        zoom += 1
    elif keys[pygame.K_x]:
        zoom -= 1

    #update screen shot
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

            pygame.draw.circle(display, color, screen_pos, 4, 4)
    
    #dino vision
    prev_dist = distance
    distance = 0
    looking = True
    while looking:
        distance += 1
        vision_point = [139+distance, scrn_size[1]/2+90]
        color = pixel_map[Screen(vision_point[0], vision_point[1])[0], Screen(vision_point[0], vision_point[1])[1]]

        if distance > max_view or color[0] == 83:
            looking = False
        

    #draw view
    pygame.draw.rect(display, green, (139, scrn_size[1]/2+90, distance, 20))
    
    #find speed
    delta_dist = prev_dist-distance
    speed = round(delta_dist/(timeit.timeit()*100))
    if speed < 0.01:
        speed = 0.01
    
    #find when to jump
    t_to_j = distance/speed

    #reation time
    if keys[pygame.K_LEFT]:
        re_time2 -= 0.2
    elif keys[pygame.K_RIGHT]:
        re_time2 += 0.2
    re_time = timeit.timeit()*100+re_time2

    #jump
    if t_to_j < re_time:
        speeds = []
        keyboard.press_and_release('UP')
    
    #change score
    score += round(timeit.timeit()*10, 2)

    #restart
    end_pos = (scrn_size[0]/2-50,scrn_size[1]/2+20)
    pygame.draw.circle(display, green, end_pos, 15, 5)
    color = pixel_map[Screen(end_pos[0], end_pos[1])[0], Screen(end_pos[0], end_pos[1])[1]]
    if color[0] == 83 and changed:
        keyboard.press_and_release('UP')
        print(re_time2)
        mag = ((old_score - round(score,2))**2)**0.5
        if old_score > round(score,2):
            time_change = time_change*(-1)
        
        re_time2 += time_change*0.05*mag/7
        old_score = round(score,2)
        score = 0
        changed = False
    else:
        changed = True

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False