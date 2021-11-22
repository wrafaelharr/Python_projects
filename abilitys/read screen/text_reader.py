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

#class
class text_reader():
    #image data
    im = ImageGrab.grab()
    pixel_map = im.load()

    #view settings
    view_pos = [601.37, 295.71]
    view_ratio = (2.5,4)
    res = 15
    zoom = 0.006723
    pan_speed = 20

    #reader settings
    light_threshold = 190

    #veriables
    zoom_h = view_ratio[1]/view_ratio[0]
    pixel_h = int(res*(view_ratio[1]/view_ratio[0]))
    pixel_w = res

    def create_viewer(self):
        #screen size
        scrn_size = (int(self.view_ratio[0]*100*1.5), int(self.view_ratio[1]*100*1.5))

        #create display
        pygame.display.set_caption('Computers view')
        display = pygame.display.set_mode((scrn_size[0], scrn_size[1]))

        return display

    def project_points(self):
        for x_pos in range(self.pixel_w):
            for y_pos in range(slef.pixel_h):
                pass
                

    def update(self):
        #get screen shot
        self.im = ImageGrab.grab()

        #get pixel data
        pixel_map = im.load()

#create objects
txt_read =  text_reader()

display = txt_read.create_viewer()

#produce screen
run = True
while run:
    #dellay and screen reset
    pygame.time.delay(100)
    display.fill(bak_color)

    #get key press inputs
    keys = pygame.key.get_pressed()

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False