import pygame as pg
import numpy as np
pg.init()

win = pg.display.set_mode((500,500))

pg.display.set_caption('Big Shlongs')

linecolor = 255, 255, 0
x = 240
y = 240
width = 2
height = 2
vel = 5

while running:
    pg.time.delay(100)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill(bgcolor)
    pygame.draw.line(screen, linecolor, (0, y), (width-1, y))
    
    y += dir
    if y == 0 or y == height-1: dir *= -1
    
    pg.draw.rect(win, (255,0,0),(x,y,width,height))
    pg.display.update()