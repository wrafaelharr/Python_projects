import pygame
import numpy
pygame.init()

#funcs
def dist(ob1y,ob1x,ob2y,ob2x):
    ydif = ((ob1y-ob2y)**2)**0.5
    xdif = ((ob1x-ob2x)**2)**0.5
    dst = (ydif**2+xdif**2)**0.5
    if ob1y<ob2y:
        if ob1x<=ob2x:
            y = 1
            x = 1
        if ob1x>=ob2x:
            y = 1
            x = -1
    if ob1y>=ob2y:
        if ob1x<=ob2x:
            y = -1
            x = 1
        if ob1x>=ob2x:
            y = -1
            x = -1
    return dst,y,x

#colors
jo_color = (100,100,200)
fu_color = (200,100,100)
bak_color = (130,0,130)

#start demensions
ball_size = 25
ball_wall = 2 
rect_height = 20
rect_width = 20
screen_height = 600
screen_width = 1200

booty = 0

numsect = 6
negone = numsect-1
#start positions
ball_rux = int(screen_width/numsect)
ball_ruy = int(screen_height/numsect)
ball_rdx = int(screen_width/numsect)
ball_rdy = int(negone*screen_height/numsect)
ball_lux = int(negone*screen_width/numsect)
ball_luy = int(screen_height/numsect)
ball_ldx = int(negone*screen_width/numsect)
ball_ldy = int(negone*screen_height/numsect)
rect1_y = (screen_height/2)-rect_height/2
rect1_x = (screen_width/2)-rect_width/2
rep_x = []
rep_y = []

run = True
while run:
    pygame.display.set_caption('fineass')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    
    game = True
    while game:
        pygame.time.delay(30)
        display.fill(bak_color)
        
        TLdis = dist(rect1_y,rect1_x,ball_luy,ball_lux)
        TRdis = dist(rect1_y,rect1_x,ball_ruy,ball_rux)
        BLdis = dist(rect1_y,rect1_x,ball_ldy,ball_ldx)
        BRdis = dist(rect1_y,rect1_x,ball_rdy,ball_rdx)
        
        hVals = numpy.array([TLdis[0],TRdis[0],BLdis[0],BRdis[0]])
        hVals_y = numpy.array([TLdis[1],TRdis[1],BLdis[1],BRdis[1]])
        hVals_x = numpy.array([TLdis[2],TRdis[2],BLdis[2],BRdis[2]])
        
        print(min(hVals),hVals==min(hVals),'\n',hVals)
        
        if min(hVals)<300:
            try:
                rect1_y = rect1_y+200/int(min(hVals)*hVals_y[hVals==min(hVals)])
                rect1_x = rect1_x+200/int(min(hVals)*hVals_y[hVals==min(hVals)])
            except:
                print('mid')
        #if rect1_y<
        #rect1_y = rect1_y-300/int(dist(rect1_y,rect1_x,ball_ruy,ball_rux))
        #rect1_x = rect1_x-300/int(dist(rect1_y,rect1_x,ball_ruy,ball_rux))
        booty = booty+1
        print('booty',booty)
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            rect1_y = rect1_y-5
        if keys[pygame.K_DOWN]:
            rect1_y = rect1_y+5
        if keys[pygame.K_RIGHT]:
            rect1_x = rect1_x+5
        if keys[pygame.K_LEFT]:
            rect1_x = rect1_x-5
        
        pygame.draw.rect(display, jo_color, (rect1_x, rect1_y, rect_height, rect_width))
        pygame.draw.circle(display, fu_color, (ball_rux, ball_ruy), ball_size, ball_wall)
        pygame.draw.circle(display, fu_color, (ball_rdx, ball_rdy), ball_size, 3)
        pygame.draw.circle(display, fu_color, (ball_lux, ball_luy), ball_size, 3)
        pygame.draw.circle(display, fu_color, (ball_ldx, ball_ldy), ball_size, 3)
        
        pygame.display.update()
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()
pygame.quit