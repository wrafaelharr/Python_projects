import pygame
import numpy as np
pygame.init()

#screen demensions
screen_height = 600
screen_width = 900

#colors
bak_color = (0,0,20)
raf_color = (150,0,0)
white = (255,255,255)

#ball demensions
ball_size = 15

#paddle demensions
paddle_width = 23
paddle_height = paddle_width*4

#paddle start info
paddle_y = [(screen_height-paddle_height)*0.5,(screen_height-paddle_height)*0.5]
paddle_x = [0,screen_width-paddle_width]
paddle_vel = [0,0]
prev_pos = 0

#ball start info
ball_ang = np.random.random()*2*np.pi
ball_vel = 5
ball_veli = ball_vel
ball_pos = [screen_width/2,screen_height/2]

#starting point values
R_points = 0
L_points = 0

while True:
    
    pygame.display.set_caption('pong')
    display = pygame.display.set_mode((screen_width,screen_height))
    
    while True:
        #loop ball ang
        if ball_ang <= 0:
            ball_ang = 2*np.pi
        elif ball_ang >= 2*np.pi:
            ball_ang = 0 
                
        #reset screen
        pygame.time.delay(30)
        display.fill(bak_color)
        
        #move left the paddle
        keys = pygame.key.get_pressed()
        if paddle_y[0] < screen_height - paddle_height and paddle_y[0] > 0:
            if keys[pygame.K_UP]:
                paddle_y[0] = paddle_y[0] - 10
            elif keys[pygame.K_DOWN]:
                paddle_y[0] = paddle_y[0] + 10
        else:
            if  screen_height/2 < paddle_y[0]+paddle_height:
                paddle_y[0] = paddle_y[0] - 1
            elif paddle_y[0] < screen_height/2:
                paddle_y[0] = paddle_y[0] + 1
                
        #move right the paddle
        keys = pygame.key.get_pressed()
        if paddle_y[1] < screen_height - paddle_height and paddle_y[1] > 0:
            if keys[pygame.K_LEFT]:
                #paddle_y[1] = paddle_y[1] - 10
                ball_ang = ball_ang + 0.3
            elif keys[pygame.K_RIGHT]:
                #paddle_y[1] = paddle_y[1] + 10
                ball_ang = ball_ang - 0.3
        else:
            if  screen_height/2 < paddle_y[1]+paddle_height:
                paddle_y[1] = paddle_y[1] - 1
            elif paddle_y[1] < screen_height/2:
                paddle_y[1] = paddle_y[1] + 1
        
        #bounce off walls
        if (ball_pos[1]-ball_size < 0 and ball_ang > np.pi) or (ball_pos[1]+ball_size > screen_height and ball_ang < np.pi):
            ball_ang = 2*np.pi - ball_ang 
        
            
        #find paddle instentainius velocity
        paddle_vel[0] = np.absolute(paddle_y[0]-prev_pos)
        paddle_vel[1] = np.absolute(paddle_y[1]-prev_pos)
        prev_pos = paddle_y[0]
        
        #bounce off paddles
        if ball_pos[0]+ball_size > screen_width-paddle_width or  ball_pos[0]-ball_size < paddle_width:
            if ball_pos[0] < screen_width/2:
                for i in np.arange(paddle_y[0],paddle_y[0]+paddle_height):
                    if int(ball_pos[1] + ball_size) > i and int(ball_pos[1] - ball_size) < i:
                        ball_ang = np.pi - ball_ang
            else:
                for i in np.arange(paddle_y[1],paddle_y[1]+paddle_height):
                    if int(ball_pos[1] + ball_size) > i and int(ball_pos[1] - ball_size) < i:
                        ball_ang = np.pi - ball_ang
        
        #ball movement
        ball_pos[0] = ball_pos[0] + np.cos(ball_ang)*ball_vel
        ball_pos[1] = ball_pos[1] + np.sin(ball_ang)*ball_vel
        
        #draw figures
        pygame.draw.rect(display, raf_color, (paddle_x[0], paddle_y[0], paddle_width, paddle_height))
        pygame.draw.rect(display, raf_color, (paddle_x[1], paddle_y[1], paddle_width, paddle_height))
        pygame.draw.circle(display, white, (int(ball_pos[0]), int(ball_pos[1])), ball_size, ball_size)
        
        #feild lines
        pygame.draw.circle(display, white, (int(screen_width/2), int(screen_height/2)), 100, 2)
        pygame.draw.line(display, white, (screen_width/2,screen_height), (screen_width/2, 0), 2)
        
        #when you die
        if ball_pos[0]+ball_size*3 < 0:
            ball_pos[0] = screen_width/2
            ball_pos [1] = screen_height/2
            ball_vel = 0
            L_points = L_points+1
        if ball_pos[0]-ball_size*3 > screen_width:
            ball_pos[0] = screen_width/2
            ball_pos[1] = screen_height/2
            ball_vel = 0
            R_points = R_points+1
        
        #display points
        OUT1 = str(R_points)
        OUT2 = str(L_points)
        font = pygame.font.Font('freesansbold.ttf', 30) 
        text1 = font.render(OUT1, True, white, bak_color)
        text2 = font.render(OUT2, True, white, bak_color)
        textRect1 = text1.get_rect()
        textRect2 = text2.get_rect()
        textRect1.center = (screen_width/4,100)
        textRect2.center = (screen_width*3/4,100)
        display.blit(text1, textRect1)
        display.blit(text2, textRect2)
        
        #reset game
        if ball_pos[0] == screen_width/2 and ball_pos[1] == screen_height/2:
            if keys[pygame.K_TAB]:
                ball_vel = ball_veli
                ball_ang = np.random.random()*2*np.pi
        
        #update screen
        pygame.display.update()
        
        #quit properly
        for event in pygame.event.get() :  
                    if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                    pygame.display.update()