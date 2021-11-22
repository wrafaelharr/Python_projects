import numpy as np
import pygame

#screen info
screen = (1000, 600)

#color
BackG_colors = (150,10,200)
yellow_green = (154,205,50)
green = (0,200,0)
yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (240,240,255)

#veg peramiters
veg_spawn_rate = 10 #smaller is faster
max_veg = 200 #maximum number of plants
veg_size = 7
start_veg = 40
veg_food = 400 #amoount of food from one veg

#erbo peramiters
start_size = 10
start_speed = 0.4
max_erbos = 30
evolve_speed = 10 #higher is mmore
view_dist = 30

#veg veriables
veg_locs = []
for i in range(start_veg):
    veg_locs.append((screen[0]*np.random.rand(), screen[1]*np.random.rand()))
veg_timer = 0

#ui function
def meters(max, current, color, num):
    #peramiters
    height = 15
    width = 150
    space_x = 20
    space_y = 20
    border = 3
    num_gap = 3
    
    #dependants
    pos_x = space_x
    pos_y = screen[1]-space_y-height-(num*(num_gap+2*height))

    #dist across
    ratio = current/max

    #draw
    pygame.draw.rect(display, white, (pos_x-border, pos_y-border, width+border*2, height+border*2))
    pygame.draw.rect(display, color, (pos_x, pos_y, width*ratio, height))

#geometry functions
def find_ang(point1, point2):
    #find differnces
    delta_x = point1[0] - point2[0]
    delta_y = point1[1] - point2[1]

    #find enitial angle
    ang = np.arctan(delta_y/delta_x)  

    #fix opposite side
    if delta_x > 0:
        ang = ang + np.pi
    
    #normalize
    if ang < 0:
        ang += 2*np.pi

    return ang

#classes
class erbo():
    #class veriables
    max_size = start_size

    #runs upon birth
    def __init__(self):
        #position information
        self.pos = [screen[0]*np.random.rand(), screen[1]*np.random.rand()]
        self.ang = 2*np.pi*np.random.rand()

        #identifier
        self.erbo_num = len(erbos)

        #looks
        self.color = blue

        #atributes
        self.size = start_size
        self.speed = start_speed
        self.food = veg_food
        self.age = 0
        self.feed_rate = 1

        #peramiters
        self.starve_rate = 1

        #attention
        self.select = 0
        self.min_dist = 0

    #spawn
    def spawn(self):
        if len(erbos) < max_erbos:
            #create new
            erbos.append(erbo())

            #look like me
            erbos[-1].pos[0] = self.pos[0] + self.size*(np.random.rand()-0.5)*2
            erbos[-1].pos[1] = self.pos[1] + self.size*(np.random.rand()-0.5)*2

            #new color
            rd = 0
            grn = 0
            bloo = 255*((self.size+1)/(max(sizes)+1))
            self.color = (rd, grn, bloo)

            #new atributes
            mutation = 0.5 - np.random.rand()
            erbos[-1].size = int(self.size + mutation*evolve_speed)
            erbos[-1].feed_rate += mutation*evolve_speed
            erbos[-1].speed += mutation*evolve_speed*0.1

    #death
    def die(self):
        #fix erbo numbers
        for erby in erbos:
            if erby.erbo_num > self.erbo_num:
                erby.erbo_num -= 1

        #delete self
        del erbos[self.erbo_num]

    #find closest
    def find(self, food_locs):
        self.min_dist = ((food_locs[0][0] - self.pos[0])**2 + (food_locs[0][1] - self.pos[1])**2)**0.5
        count = 0

        for veg_pos in food_locs:
            #find distance
            dist = ((veg_pos[0] - self.pos[0])**2 + (veg_pos[1] - self.pos[1])**2)**0.5

            #check if smaller
            if dist < self.min_dist:
                #fix minimum
                self.min_dist = dist

                #find selection
                self.select = count
            else:
                self.select = 0

            #increase counter
            count += 1

    #fallow
    def fallow(self, food_locs):
        #find angle
        if self.select < len(food_locs) and self.select > 0 and self.min_dist < self.size*view_dist:
            ang = find_ang(self.pos, food_locs[self.select])
        else:
            ang = self.ang

        #assighn angle
        self.ang = ang

        #draw pointer
        position = (self.pos[0] + np.cos(self.ang)*self.size*1.1, self.pos[1] + np.sin(self.ang)*self.size*1.1)
        pygame.draw.circle(display, self.color, position, int(self.size/2.5), int(self.size/2.5))

    #move
    def move(self):
        #move
        self.pos[0] += np.cos(self.ang)*self.speed
        self.pos[1] += np.sin(self.ang)*self.speed

        #age
        self.age += 1
        self.food -= self.starve_rate

        if self.food <= 0:
            erby.die()

    #eat
    def eat_veg(self):
        if self.min_dist < self.size + veg_size and self.select >= 0:
            #delete veg
            del veg_locs[self.select]
            
            #get full
            self.food += veg_food*self.feed_rate

            #bread
            self.spawn()

    #draw that puppy
    def draw(self):
        pygame.draw.circle(display, self.color, self.pos, self.size, self.size)
    
#create erbo list
erbos = []
erbos = [erbo()]

#create display
pygame.display.set_caption('fineass')
display = pygame.display.set_mode((screen[0], screen[1]))

#main
run = True
while run:
    #dellay
    pygame.time.delay(10)

    #set background color
    display.fill(BackG_colors)

    #grow vegitation
    veg_timer += 1
    if (veg_timer*(len(veg_locs)/max_veg)*5 > veg_spawn_rate) or len(veg_locs) < 2:
        if len(veg_locs) < max_veg:
            #create new veg
            veg_locs.append((screen[0]*np.random.rand(), screen[1]*np.random.rand()))

        #reset timer
        veg_timer = 0
    
    #data recording
    sizes = []
    speeds = []

    #erbo actions
    for erby in erbos:
        #find info
        sizes.append(erby.size)
        speeds.append(erby.speed)

        #find food
        erby.find(veg_locs)

        #fallow
        erby.fallow(veg_locs)

        #move that pup
        erby.move()

        #eat veg
        erby.eat_veg()

        #draw them
        erby.draw()

    #draw veg
    for locals in veg_locs:
        #highlight closest
        pygame.draw.circle(display, green, locals, veg_size, veg_size)

    #visualize data
    meters(max_veg, len(veg_locs), yellow_green, 0)
    if len(sizes) > 0:
        meters(30, max(sizes), blue, 1)

    #update screen
    pygame.display.update()
    
    #quite properly
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit() 
        pygame.display.update()