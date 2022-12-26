import pygame
import numpy
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
red = (200, 0, 0)
blue = (100, 100, 200)
black = (0,0,0)

#format peramiters
margin = 100

#veribles
userin = ''
compout = ''
NumToKey = {97:'a',98:'b',99:'c',100:'d',101:'e',102:'f',103:'g',104:'h',105:'i',106:'j',107:'k',108:'l',
            109:'m',110:'n',111:'o',112:'p',113:'q',114:'r',115:'s',116:'t',117:'u',118:'v',119:'w',120:'x',
            121:'y',122:'z', 46:'.',32:' '}#,13:'\n'}
keys = pygame.key.get_pressed()

#functions
def WriteText(in_str, color, bcolor, size, pos):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(in_str, True, color, bcolor)
    textRect = text.get_rect()
    textRect.center = pos
    display.blit(text, textRect)

#create display
pygame.display.set_caption('talk')
display = pygame.display.set_mode((screen_width, screen_height))

#main game
run = True
while run:
    #dellay and screen reset
    pygame.time.delay(30)
    display.fill(red)

    #computer out
    WriteText("Comp Out:", blue, black, 30, (100, margin/2))
    WriteText(compout, blue, black, 30, (100, margin/2))

    #user in
    WriteText("User In:", blue, black, 30, (80, screen_height/2))
    WriteText(userin, blue, black, 20, (10+len(userin)*5, screen_height/2+50))

    #get inputs
    for num in NumToKey:
        if keys[num] and pygame.key.get_pressed()[num] == False: userin += NumToKey[num]
    if  keys[8]: userin = userin[:-1]
    keys = pygame.key.get_pressed() 

    #find keys
    #print(keys[13])
    '''
    for i in range(len(keys)):
        if keys[i]: print(i)
    '''

    #make the game quit properly and update screen
    pygame.display.update()
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        pygame.display.update()