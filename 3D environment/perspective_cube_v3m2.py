import pygame
import pandas as pd
import numpy as np
pygame.init()

#screen demensions
screen_width = 1200
screen_height = 600

#colors
bak_color = (76, 217, 191)
yellow = (255, 255, 0)
blue = (87, 233, 248)
green = (30, 180, 30)
red = (200,0,0)
black = (0,0,0)

#camera atributes
camera_xyz = [200,100,100]
camera_ang = 0
cam_speed = 20
view_ang_widthxy = np.pi/3
view_ang_widthxz = np.pi/3
snesativity = 1

#box 1 attributes
box_xyz = [700,400,0]
box_ang = 0
box_whl = [50,50,50]

#cube 2 attributes
cube_xyz = [800,250,0]
cube_ang = 0
cube_whl = [50,50,400]

#all cubes
cubes = [[box_xyz, box_ang, box_whl],[cube_xyz, cube_ang, cube_whl]]

#menu vars
viewer_toggle = 1
look_toggle = 0
dist1 = 0
dist2 = 0
mouse = [0,0]
start_mouse = True
mouse_start = [0,0]
mouse_end = [0,0]
mouse_dist = 0


#functions
def ang_dist(x1, y1, x2, y2, ang):
    distx = x2 - x1
    disty = y2 - y1
    dist_xy = 0.000001
    if (distx**2 + disty**2)**0.5 != 0:
        dist_xy = (distx**2 + disty**2)**0.5

    if distx > 0:
        cube_ang = np.arcsin(disty/dist_xy)
    else:
        if disty > 0:
            cube_ang = np.pi - np.arcsin(disty/dist_xy)
        else:
            cube_ang = -np.pi/2 -(np.pi/2 + np.arcsin(disty/dist_xy))

    if ang <= 0:
        ang = 2*np.pi - np.absolute(ang)%(2*np.pi)
    elif ang >= 2*np.pi:
        ang = 2*np.pi - ang%(2*np.pi)

    dif_ang = cube_ang - ang

    if dif_ang < -np.pi:
        dif_ang = 2*np.pi + dif_ang
    elif dif_ang > np.pi:
        dif_ang = dif_ang - 2*np.pi
    
    return distx, disty, dist_xy, cube_ang, dif_ang

def camera_viewxy(viewer, x, y, angle, view_width):
    point1 = (x,y)
    point2 = (x + np.cos(angle-view_width/2)*150, y - np.sin(angle-view_width/2)*150)
    point3 = (x + np.cos(angle+view_width/2)*150, y - np.sin(angle+view_width/2)*150)
    return point1, point2, point3

def camera_viewxz(viewer, x, y, angle, view_width):
    angle = np.absolute(angle)%(2*np.pi)
    point1 = (x,y)
    if angle < np.pi*3/2 and angle > np.pi/2:
        point2 = (x + np.cos(np.pi-view_width/2)*150, y + np.sin(np.pi-view_width/2)*150)
        point3 = (x + np.cos(np.pi+view_width/2)*200, y + np.sin(np.pi+view_width/2)*150)
    else:
        point2 = (x + np.cos(0-view_width/2)*150, y + np.sin(0-view_width/2)*150)
        point3 = (x + np.cos(0+view_width/2)*150, y + np.sin(0+view_width/2)*150)
    return point1, point2, point3

def stationary_cube(xyz, whl):
    cube = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    x1 = xyz[0] - whl[0]/2
    x2 = xyz[0] + whl[0]/2
    y1 = xyz[1] - whl[1]/2
    y2 = xyz[1] + whl[1]/2
    z1 = xyz[2] - whl[2]/2
    z2 = xyz[2] + whl[2]/2
    top = list(range(4))
    bot = list(range(4,8))
    side1 = top[0:2] + [bot[1], bot[0]]
    side2 = top[1:3] + [bot[2], bot[1]]
    side3 = top[2:4] + [bot[3], bot[2]]
    side4 = [top[0], top[3], bot[3], bot[0]]
    
    for i in top:
        cube[i][1] = y1
    for i in bot:
        cube[i][1] = y2
    for i in side1:
        cube[i][0] = x1
    for i in side3:
        cube[i][0] = x2
    for i in side2:
        cube[i][2] = z1
    for i in side4:
        cube[i][2] = z2
    
    tops = []
    bots = []
    sides1 = []
    sides2 = []
    sides3 = []
    sides4 = []

    for i in top:
        tops.append(cube[i])
    for i in bot:
        bots.append(cube[i])
    for i in side1:
        sides1.append(cube[i])
    for i in side3:
        sides2.append(cube[i])
    for i in side2:
        sides3.append(cube[i])
    for i in side4:
        sides4.append(cube[i])

    return tops, bots, sides1, sides2, sides3, sides4

def draw_poly(cam_xyz, points):
    corners = []
    for i in points:
        distx, disty, dist_xy, cube_ang, dif_ang = ang_dist(cam_xyz[0], cam_xyz[1], i[0], i[1], camera_ang)
        distx, distz, dist_xz, cube_angxz, dif_ang_xz = ang_dist(0, cam_xyz[2], dist_xy, i[2], 0)
        
        #find position x
        ang_ratio = dif_ang/(view_ang_widthxy/2)
        
        ang_ratioxz = dif_ang_xz/(view_ang_widthxz/2)
        x = screen_width/2 - ang_ratio*screen_width/2
        y = screen_height/2 - ang_ratioxz*screen_height/2

        corners.append((x,y))
    if cube_ang < 0:
        cube_ang += 2*np.pi
    return corners, cube_ang, cube_angxz, dist_xy

def draw_cube(cam_xyz, cube_xyz, box_whl,  tops, bots, side1s, side2s, side3s, side4s):
    corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side4s)
    #draw top/bottom
    if cube_angxz < 0:
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side4s)
        pygame.draw.polygon(display, red, corners)
    else:
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side3s)
        pygame.draw.polygon(display, red, corners)

    #draw cube
    corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side4s)
    if cube_ang > 0 and cube_ang < np.pi/2:
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, tops)
        pygame.draw.polygon(display, green, corners)
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side1s)
        pygame.draw.polygon(display, blue, corners)
    elif cube_ang > np.pi/2 and cube_ang < np.pi:
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, tops)
        pygame.draw.polygon(display, green, corners)
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side2s)
        if abs(cam_xyz[0]-cube_xyz[0]) > box_whl[0]/2:
            pygame.draw.polygon(display, blue, corners)
    elif cube_ang > np.pi and cube_ang < np.pi*3/2:
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, bots)
        pygame.draw.polygon(display, green, corners)
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side2s)
        if abs(cam_xyz[0]-cube_xyz[0]) > box_whl[0]/2:
            pygame.draw.polygon(display, blue, corners)
    else:
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, bots)
        pygame.draw.polygon(display, green, corners)
        corners, cube_ang, cube_angxz, dist_xz = draw_poly(cam_xyz, side1s)
        pygame.draw.polygon(display, blue, corners)
    
    return dist_xz


#classes
class viewer:
    #viewer facts
    view_y = screen_height - 150
    view_width = 250
    view_height = view_width/2
    viewer1 = (screen_width/6 - view_width/2, view_y, view_width, view_height)
    viewer2 = (screen_width*5/6 - view_width/2, view_y, view_width, view_height)
    unit_width = screen_width
    unit_height = screen_height
    unit_spacex = view_width/unit_width
    unit_spacey = view_height/unit_height

    def draw(self, camera_pos, box_info):
        #find camera points
        x = self.viewer1[0] + camera_pos[0]*self.unit_spacex
        y = self.viewer1[1] + self.view_height - camera_pos[1]*self.unit_spacey
        x2 = self.viewer2[0] + camera_pos[0]*self.unit_spacex
        z = self.viewer2[1] + self.view_height - camera_pos[2]*self.unit_spacey

        #find cube points
        boxs = []
        for i in box_info:
            x3 = self.viewer1[0] + i[0][0]*self.unit_spacex - self.unit_spacex*i[2][0]/2
            y3 = self.viewer1[1] + self.view_height - i[0][1]*self.unit_spacey - self.unit_spacey*i[2][1]/2
            x4 = self.viewer2[0] + i[0][0]*self.unit_spacex - self.unit_spacex*i[2][0]/2
            y4 = self.viewer2[1] + self.view_height - i[0][2]*self.unit_spacey - self.unit_spacey*i[2][1]/2
            box_width = i[2][0]*self.unit_spacex
            box_height = i[2][1]*self.unit_spacey
            box_length = i[2][2]*self.unit_spacey
            boxs.append((x3, y3, box_width, box_height))
            boxs.append((x4, y4, box_width, box_length))

        #draw view backgrounds
        pygame.draw.rect(display, green, self.viewer1)
        pygame.draw.rect(display, green, self.viewer2)

        #draw camaera view
        pygame.draw.polygon(display, blue, camera_viewxy(self.viewer1, x, y, camera_ang, view_ang_widthxy))
        pygame.draw.polygon(display, blue, camera_viewxz(self.viewer1, x2, z, camera_ang, view_ang_widthxz))
        '''
        #angle indicators
        pygame.draw.line(display, black, (x, y), (x+np.cos(cube_ang)*30, y-np.sin(cube_ang)*30), 3)
        pygame.draw.line(display, black, (x, y), (x[0]+np.cos(camera_ang)*30, y[1]-np.sin(camera_ang)*30), 3)
        '''
        #draw cubes
        for i in boxs:
            pygame.draw.rect(display, red, i)

        #draw camera
        pygame.draw.circle(display, blue, (x,y), 7) 
        pygame.draw.circle(display, blue, (x2,z), 7)

class cuber:
    ang = 0
    whl = [50,100,50]
    xyz = [700,800, whl[1]/2]

    def find_3d(self):
        self.top, self.bot, self.side1, self.side2, self.side3, self.side4 = stationary_cube(self.xyz, self.whl)
    
    def draw(self, cam_xyz):
        dist = draw_cube(cam_xyz, self.xyz, self.whl, self.top, self.bot, self.side1, self.side2, self.side3, self.side4)

        return dist

#create objects
all_cubes = []
view = viewer()
for i in range(len(cubes)):
    all_cubes.append(cuber())

#find pemrinant 3d points
for i in all_cubes:
    i.find_3d()

#create display
pygame.display.set_caption('cubes')
display = pygame.display.set_mode((screen_width, screen_height))

#find distances
cube_dists = np.zeros(len(all_cubes))
for i in range(len(all_cubes)):
    cube_dists[i] = (all_cubes[i].draw(camera_xyz))

#move cubes [box_xyz, box_ang, box_whl]
for i in range(len(cubes)):
    all_cubes[i].xyz = cubes[i][0]
    all_cubes[i].ang = cubes[i][1]
    all_cubes[i].whl = cubes[i][2]

#main
run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #draw that boy
    sorted_dist = sorted(cube_dists)
    sorted_or_not = np.zeros(len(all_cubes))+1
    for i in range(len(all_cubes)):
        cube_dists[i] = all_cubes[i].draw(camera_xyz)


    #get key press inputs
    keys = pygame.key.get_pressed()

    #mouse movement
    old_mouse = mouse
    mouse = pygame.mouse.get_pos()
    mouse_dif = (mouse[0]-screen_width/2, mouse[1]-screen_height/2)
    
    #better camera roatation
    if mouse != old_mouse and start_mouse:
        mouse_start = mouse
        start_mouse = False
    
    else:
        mouse_end = mouse
        if mouse == old_mouse:
            start_mouse = True
    
    if start_mouse == False:
        x1 = mouse_start[0]
        y1 = mouse_start[1]
        x2 = mouse_end[0]
        y2 = mouse_end[1]
        mouse_dist = (x1 - x2)*snesativity
    
    else:
        mouse_dist = 0

    camera_ang += (mouse_dist/screen_width)

    #toggle viewer
    if keys[pygame.K_v]:
        viewer_toggle += 1
    if viewer_toggle%2:
        #draw viewer
        view.draw(camera_xyz, cubes)
    
    #walk around
    if keys[pygame.K_w]:
        camera_xyz[0] += np.cos(camera_ang)*cam_speed
        camera_xyz[1] += np.sin(camera_ang)*cam_speed
    elif keys[pygame.K_s]:
        camera_xyz[0] += np.cos(camera_ang+np.pi)*cam_speed
        camera_xyz[1] += np.sin(camera_ang+np.pi)*cam_speed
    if keys[pygame.K_a]:
        camera_xyz[0] += np.cos(camera_ang+np.pi/2)*cam_speed
        camera_xyz[1] += np.sin(camera_ang+np.pi/2)*cam_speed
    elif keys[pygame.K_d]:
        camera_xyz[0] += np.cos(camera_ang-np.pi/2)*cam_speed
        camera_xyz[1] += np.sin(camera_ang-np.pi/2)*cam_speed

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False