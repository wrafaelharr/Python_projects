import pygame as pg
pg.init()

wind = pg.display.set_mode((500,500))

pg.display.set_caption('ask your mom how my dick tastes')

width = 5
height = 5

x = 250-0.5*width
y = 250-0.5*height

pg.draw.rect(wind, (255, 0, 0), (400, 0, 100, 500))

run = True
while run:
    pg.time.delay(100)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_TAB]:
        break
    if keys[pg.K_LEFT]:
        x = x-10
    if keys[pg.K_RIGHT]:
        x = x+10
    if keys[pg.K_UP]:
        y = y-10
    if keys[pg.K_DOWN]:
        y = y+10
    if keys[pg.K_LSHIFT]:
        width = width+2
        height = height+2
    if keys[pg.K_RSHIFT]:
        width = width-2
        height = height-2
    if x>400:
        break
    
    pg.draw.rect(wind, (0, 255, 0), (x, y, width, height))
    pg.display.update()


pg.quit()