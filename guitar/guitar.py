import time
import pygame
import numpy as np
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
import os
os.getcwd()

#bango cord order: G, D, G2, B, D2

#screen demensions
screen_width = 1200
screen_height = 790

#colors
bak_color = (100,200,0)
red = (200,0,0)
blue = (0,200,240)

#assighn sounds
strings = ['bangoG.mp3','bangoD.mp3','bangoG2.mp3','bangoB.mp3','bangoD2.mp3']
string_key = [pygame.K_g, pygame.K_f, pygame.K_d, pygame.K_s, pygame.K_a]
strike = np.zeros(len(strings))
for i in range(len(strings)):
    strings[i] = pygame.mixer.Sound(strings[i])
    strike[i] = 1

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen_width,screen_height))

run = True
while run:
    #delay and screen reset
    pygame.time.delay(30)
    display.fill(bak_color)

    #check for string strikes
    for i in range(len(strings)):
        keys=pygame.key.get_pressed()
        if keys[string_key[i]] and strike[i]:
            pygame.mixer.Channel(i).play(strings[i])
            strike[i] = 0
        elif keys[string_key[i]] == False:
            strike[i] = 1

    #update screen
    pygame.display.update()
    
    #quite
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            run = False