# import pygame module in this program 
import pygame 
  
pygame.init() 
   
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
red = (255, 0, 0)
black = (0,0,0)
  
X = 500
Y = 500
   
display_surface = pygame.display.set_mode((X, Y )) 
  
pygame.display.set_caption('Show Text') 
   
font = pygame.font.Font('freesansbold.ttf', 32) 

text = font.render('DEATH', True, black, red) 

textRect = text.get_rect()  

textRect.center = (X // 2, Y // 2) 

while True : 
    
    display_surface.fill(red) 
    
    display_surface.blit(text, textRect) 
    
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update()  