import pygame as pg
import numpy as np
pg.init()

wind = pg.display.set_mode((500,500))

pg.display.set_caption('ask your mom how my dick tastes')

width = 5
height = 5

x = 250-0.5*width
y = 250-0.5*height

run = True
while run:
    pg.time.delay(100)
    kyb = pg.key.get_pressed()
    if kyb[pg.K_UP]:
        x = x+10
    pg.draw.rect(wind, (0, 255, 0), (x, y, width, height))
    pg.display.update()
pg.quit()