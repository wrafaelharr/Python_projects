import pyautogui
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

#functions
def dino_loc():
    pyautogui.locateOnScreen(r'C:\Users\Lrhgr\Desktop\dino.png')

def get_pixl(x, y):
    myScreenshot = pyautogui.screenshot()
    #myScreenshot.getpixel((x, y))

    poops = myScreenshot.size()
    print(poops)

#create display
pygame.display.set_caption('cubes')
display = pygame.display.set_mode((screen_width, screen_height))

#main
run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #get key press inputs
    keys = pygame.key.get_pressed()

    #randomize
    if keys[pygame.K_r]:
        pix_val = get_pixl(200, 200)
    
        print(pix_val)

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False


#dinoloc = pyautogui.locateOnScreen(r'C:\Users\Lrhgr\Desktop\dino.png')
#myScreenshot = pyautogui.screenshot()
#myScreenshot.save(r'C:\Users\Lrhgr\Desktop\screenshot1.png')
#