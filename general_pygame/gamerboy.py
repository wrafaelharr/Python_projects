import pygame as pg
pg.init()

game=True
end=True
 
red = (255, 0, 0)
black = (0,0,0)
blap = (255, 120, 180)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

pg.display.set_caption('ask your mom how my dick tastes') 

width = 5
height = 5

wall = 2
size = 40
sy = 100
sx = 100
h = 40
small = 0
win = True

while game:
    wind = pg.display.set_mode((500,500))
    x = 250-0.5*width #player size
    y = 250-0.5*height #player size
    
    sx = 100
    sy = 100
    
    run = True
    while run:
        
        pg.time.delay(30)
        wind.fill(pg.Color("black")) #reset screen
        if h>size:
            pg.draw.rect(wind, (255, 0, 0), (400, 0, 100, 500)) #death wall
        pg.draw.circle(wind, blue, (sx, sy), size, wall)
        
        for event in pg.event.get(): #idk what its for really
            if event.type == pg.QUIT:
                run = False
        #read the keybourd
        keys = pg.key.get_pressed()
        
        #general controls
        if keys[pg.K_TAB]:
            run=False
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
            
        #screen
        
        if y<0:#top loop
            y = y+500
        if y>500:#bottom loop
            y = 0
        if x<0-width: #label if you exit the screen
            font = pg.font.Font('freesansbold.ttf', 12) 
            text = font.render('<CUCK', True, blap, black)
            textRect = text.get_rect()
            textRect.center = (25, y+0.5*width)
            wind.blit(text, textRect)
        if x<-width*3.5: #stay close
            x = -width*3
        
        #circle behavor
        h = ((x-sx)**2+(y-sy)**2)**0.5 #inside circle
        
        if h<size-wall and y<sy and x>sx: #top right
            sx = sx+1
            sy = sy-1
            small = small +1
        if h<size-wall and y<sy and x<sx: #top left
            sx = sx-1
            sy = sy-1
            small = small +1
        if h<size-wall and y>sy and x<sx: #bottom left
            sx = sx-1
            sy = sy+1
            small = small +1
        if h<size-wall and y>sy and x>sx: #bottom right
            sx = sx+1
            sy = sy+1
            small = small +1
        #get out
        
        #draw player
        pg.draw.rect(wind, (0, 255, 0), (x, y, width, height))
        pg.display.update() #update the screen
        print(run,x+width,y) #diognastics
        
        #death
        if (x+width)>400 and h>size:#death wall
            run=False
        
        #win
        if x>500+width:
            while win:
                #print death
                display_surface = pg.display.set_mode((500, 500)) 
                pg.display.set_caption('thats your best freinds girl right there') 
                font = pg.font.Font('freesansbold.ttf', 32) 
                text = font.render('HEY, YOU LIVED... for a bit', True, black, blue) 
                textRect = text.get_rect()  
                textRect.center = (500 // 2, 500 // 2) 
                display_surface.fill(blue)
                display_surface.blit(text, textRect) 
                
                while win: 
                    keys = pg.key.get_pressed()
                    if keys[pg.K_TAB]:
                        win = False
                        print('fuck')
                    for event in pg.event.get() :  
                        if event.type == pg.QUIT : 
                            pg.quit() 
                            quit() 
                        pg.display.update()
            
    #run death screen
    dth = True 
    while dth:
        #size of death screen
        X = 500
        Y = 500
        
        #print death
        display_surface = pg.display.set_mode((X, Y )) 
        pg.display.set_caption('fuck U you lost') 
        font = pg.font.Font('freesansbold.ttf', 32) 
        text = font.render('DEATH', True, black, red) 
        textRect = text.get_rect()  
        textRect.center = (X // 2, Y // 2) 
        display_surface.fill(red)
        display_surface.blit(text, textRect) 
        
        while dth : 
            keys = pg.key.get_pressed()
            if keys[pg.K_TAB]:
                dth = False
                print('fuck')
            for event in pg.event.get() :  
                if event.type == pg.QUIT : 
                    pg.quit() 
                    quit() 
                pg.display.update()  
pg.quit()