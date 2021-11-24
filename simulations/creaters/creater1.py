import numpy as np
import pygame
import datetime as dt

#screen info
screen = (1500, 900)

#color
BackG_colors = (150,10,200)
yellow_green = (154,205,50)
green = (0,200,0)
yellow = (255,255,0)
red = (200,0,0)
dark_red = (100,0,0)
blue = (0,0,200)

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen[0], screen[1]))

#characters
class erbos():
    gen_max_hung = 800
    view_dist = 15
    color_grad = 10 #bigger is darker

    #on enitiate
    def __init__(self):
        #pos info
        self.pos = [0, screen[1]*np.random.rand()]
        self.ang = 0

        #food info
        self.ang_fdelta = 0
        self.food_ang = 0
        self.food_dist = 0
        self.pray_dist = 0

        #atributes
        self.speed = 1
        self.size = 10
        self.hunger = 0
        self.max_hunger = 100

        #data
        self.age = 0
        self.color = yellow_green

        #assighn number
        self.erbo_num = len(erbo)

    #ability to fnd food
    def find_food(self, veg_locs):
        #find distances
        dists = []
        for locals in veg_locs:
            delta_x = abs(locals[0]-self.pos[0])
            delta_y = abs(locals[1]-self.pos[1])
            dists.append(round((delta_x**2 + delta_y**2)**0.5, 2))
        
        #find smallest
        if dists:
            closest = min(dists)
        else:
            closest = 0
        
        #find index of smallest
        if closest > 0:
            select = dists.index(closest)
        else:
            select = 0
        
        #assighn distance
        self.food_dist = closest

        #find veggie location
        if veg_locs:
            delta_x = veg_locs[select][0]-self.pos[0]
            delta_y = self.pos[1]-veg_locs[select][1]
        else:
            delta_x = 0
            delta_y = 0
        
        #find angle one half
        if delta_x != 0:
            ang = np.arctan(delta_y/delta_x)
        else:
            ang = 0
        
        #find angle other half
        if delta_x < 0:
            ang += np.pi
        
        #normalize
        if ang < 0:
            ang += 2*np.pi

        
        #exclusion zone
        if erby.pos[0] < exclude_x or erby.pos[0] > screen[0]-exclude_x or erby.pos[1] < exclude_y or erby.pos[1] > screen[1]-exclude_y:
            #assighn angle
            if closest < self.size*self.view_dist:
                self.food_ang = ang

        return select
    
    #hunt
    def hunt(self, erbo_locs):
        if erbo_locs:
            #find distances
            dists = []
            for locals in erbo_locs:
                delta_x = abs(locals[0]-self.pos[0])
                delta_y = abs(locals[1]-self.pos[1])
                dists.append(round((delta_x**2 + delta_y**2)**0.5, 2))
            
            #find smallest
            if dists:
                closest2 = min(dists)
            else:
                closest2 = 0
            
            #find index of smallest
            if closest2 > 0:
                select2 = dists.index(closest2)
            else:
                select2 = 0
            
            #assighn distance
            self.pray_dist = closest2

            #find location
            if erbo_locs:
                delta_x = erbo_locs[select2][0]-self.pos[0]
                delta_y = self.pos[1]-erbo_locs[select2][1]
            else:
                delta_x = 0
                delta_y = 0
            
            #find angle one half
            if delta_x != 0:
                ang = np.arctan(delta_y/delta_x)
            else:
                ang = 0
            
            #find angle other half
            if delta_x < 0:
                ang += np.pi
            
            #normalize
            if ang < 0:
                ang += 2*np.pi

            self.food_ang = ang

            return select2
        
    #move
    def move(self):
        #age
        self.age += 1

        #move
        self.pos[0] += np.cos(self.food_ang)*self.speed
        self.pos[1] -= np.sin(self.food_ang)*self.speed

    #die
    def die(self):
        #fix erbo num
        for erby in erbo:
            if erby.erbo_num > self.erbo_num:
                erby.erbo_num -= 1
        
        #deleete self
        del erbo[self.erbo_num] 

    #hunger
    def starve(self):
        #get hungry
        self.hunger += 1
        
        #starve to death
        if self.hunger > self.max_hunger:#*self.size/10 > self.max_hunger:
            self.die()
        
        #shrink to death
        if self.size < 0:
            self.die()

    #draw
    def draw(self):
        pygame.draw.circle(display, self.color, self.pos, self.size, self.size)
        pygame.draw.circle(display, self.color, (self.pos[0]+np.cos(self.food_ang)*self.size, self.pos[1]-np.sin(self.food_ang)*self.size), 4, 4)

    #spawn
    def spawn(self):
        if len(erbo) < max_erbo_spawn:
            #give birth
            erbo.append(erbos())
            erbo[-1].pos[0] = self.pos[0]+self.size*2*np.cos(2*np.pi*np.random.rand())
            erbo[-1].pos[1] = self.pos[1]+self.size*2*np.cos(2*np.pi*np.random.rand())

            #drift or not
            if self.size > 4:
                erbo[-1].food_ang = self.food_ang

            #change some stuff
            change = evolve_rate*(0.5-np.random.rand())

            erbo[-1].speed = self.speed - change*0.07
            erbo[-1].size = int(self.size + change)
            erbo[-1].max_hunger = self.gen_max_hung + erbo[-1].size

            #color
            gree = self.color_grad*erbo[-1].size
            if gree < 200 and gree >= 0:
                erbo[-1].color = (154, gree ,50)
            elif gree < 0:
                erbo[-1].color = (154, 0, 50)
            else:
                erbo[-1].color = yellow_green

    #eat veg
    def eat(self):
        if self.food_dist < (self.size + 7) and veg_locs:
            #delete veggie
            del veg_locs[select]

            #feed
            self.hunger = 0

            #give birth
            self.spawn()

#veggitation
veg_locs = []
veg_timer = 0
veg_spawn_rate = 0
spawn_ratio = .5 #lower is faster
veg_spawn_max = 120 #actual num

#create an erbo
evolve_rate = 15 #higher is faster
max_erbo_spawn = 80 #max erbos
erbo_timer = 0
erbo = []
erbo = [erbos()]
erbo.append(erbos())

#exclusion zone
exclude_x = 700
exclude_y = 400
delay_timer = 0

#main loop
run = True
while run:
    #dellay
    pygame.time.delay(10)

    #set background color
    display.fill(BackG_colors)
    
    #draaw exclude zone
    pygame.draw.rect(display, (0,0,150), (exclude_x, exclude_y, screen[0]-(2*exclude_x), screen[1]-(2*exclude_y)))


    #grow vegitation
    veg_timer += 1
    if len(veg_locs) < 10:
        veg_spawn_rate = 40*spawn_ratio
    elif len(veg_locs) < 20:
        veg_spawn_rate = 20*spawn_ratio
    else:
        veg_spawn_rate = 10*spawn_ratio
    if (veg_timer > veg_spawn_rate) and len(veg_locs) < veg_spawn_max:
        #create new veg
        veg_locs.append((screen[0]*np.random.rand(), screen[1]*np.random.rand()))

        #reset timer
        veg_timer = 0

    #actions for erbos
    ages = [0]
    speed = [0]
    size = [0]
    erbo_locs = []
    if delay_timer < 700:
        delay_timer += 1
    else:
        for erby in erbo:
            #move erbos
            erby.move()
            
            #get veg
            select = erby.find_food(veg_locs)

            #eat veg
            erby.eat()
            
            #starve
            erby.starve()

            #draw creaters
            erby.draw()

            #find info
            ages.append(erby.age)
            speed.append(erby.speed)
            size.append(erby.size)

            #find locatiuons
            erbo_locs.append(erby.pos)

    #draw veg
    count = 0
    for locals in veg_locs:
        pygame.draw.circle(display, green, locals, 7, 7)

    #feedbakc
    pygame.draw.rect(display, green, (0, screen[1]-len(veg_locs)*4.4-10, 50, 10))
    pygame.draw.rect(display, blue, (0, screen[1]-len(erbo)*8-10, 50, 10))
    pygame.draw.rect(display, red, (0, screen[1]-(max(size))*10-10, 50, 10))
    pygame.draw.rect(display, dark_red, (0, screen[1]-(sum(size)/len(size))*10-10, 50, 10))
    print(size[-1])

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit() 
        pygame.display.update()
pygame.quit