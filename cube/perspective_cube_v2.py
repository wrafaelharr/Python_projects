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
speed = 30
view_ang_widthxy = np.pi/3
view_ang_widthxz = np.pi/3
stand_dist = 620

#box attributes
box_xyz = [700,400,0]
box_ang = 0
box_size = 50


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

#viewer functions
def camera_point_finder(viewer, x,y):
    x = viewer[0] + x*unit_spacex
    y = viewer[1] + view_height - y*unit_spacey
    return x,y

def box_point_finder(viewer, x,y, box_size):
    x = viewer[0] + x*unit_spacex - unit_spacex*box_size/2
    y = viewer[1] + view_height - y*unit_spacey - unit_spacey*box_size/2
    box_width = box_size*unit_spacex
    box_height = box_size*unit_spacey
    return x,y,box_width,box_height

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

def cube_ang_distxy(cam_x, cam_y, cube_x, cube_y, cam_ang):
    cube_distx = cube_x - cam_x
    cube_disty = cube_y - cam_y
    box_dist_xy = (cube_distx**2 + cube_disty**2)**0.5

    if cube_distx > 0:
        cube_ang = np.arcsin(cube_disty/box_dist_xy)
    else:
        if cube_disty > 0:
            cube_ang = np.pi - np.arcsin(cube_disty/box_dist_xy)
        else:
            cube_ang = -np.pi/2 -(np.pi/2 + np.arcsin(cube_disty/box_dist_xy))

    if cam_ang < 0:
        cam_ang = 2*np.pi - np.absolute(cam_ang)%(2*np.pi)
    elif cam_ang > 2*np.pi:
        cam_ang = 2*np.pi - cam_ang%(2*np.pi)
    
    dif_ang = cube_ang - cam_ang

    if dif_ang < -np.pi:
        dif_ang = 2*np.pi + dif_ang
    elif dif_ang > np.pi:
        dif_ang = dif_ang - 2*np.pi
    
    return cube_distx, cube_disty, box_dist_xy, dif_ang, cube_ang

def cube_ang_distxz(cam_x, cam_y, cube_x, cube_y, cam_ang):
    cube_distx = cube_x - cam_x
    cube_disty = cube_y - cam_y
    box_dist_xy = (cube_distx**2 + cube_disty**2)**0.5

    if cube_distx > 0:
        cube_ang = np.arcsin(cube_disty/box_dist_xy)
    else:
        if cube_disty > 0:
            cube_ang = np.pi - np.arcsin(cube_disty/box_dist_xy)
        else:
            cube_ang = -np.pi/2 -(np.pi/2 + np.arcsin(cube_disty/box_dist_xy))

    if cam_ang < 0:
        cam_ang = 2*np.pi - np.absolute(cam_ang)%(2*np.pi)
    elif cam_ang > 2*np.pi:
        cam_ang = 2*np.pi - cam_ang%(2*np.pi)
    
    dif_ang = cube_ang - cam_ang

    if dif_ang < -np.pi:
        dif_ang = 2*np.pi + dif_ang
    elif dif_ang > np.pi:
        dif_ang = dif_ang - 2*np.pi
    
    return box_dist_xy, dif_ang, cube_ang

#draw box class
class cubes:
    xy = [screen_width/2, screen_height/2, 0]
    ang = [0, 0]
    tilt = 0.2
    hwl = [100, 100, 100]
    size = 1
    space = np.pi/2
    def draw(self):
        #loop ang rote
        if self.ang[0] > 2*np.pi:
            self.ang[0] = 0
        elif self.ang[0] < 0:
            self.ang[0] = 2*np.pi
        #loop ang tilt
        if self.ang[1] > np.pi/2:
            self.ang[1] = np.pi/2
        elif self.ang[1] < -np.pi/2:
            self.ang[1] = -np.pi/2
        
        #attach angle and tilt
        self.tilt = self.ang[1]/np.pi/2

        #find top and bottom points
        top_points = []
        bot_points = []
        for i in range(4):
            top_points.append((self.size*self.hwl[1]*np.cos(self.ang[0]+self.space*i)+self.xy[0],
                                self.size*self.hwl[1]*self.tilt*np.sin(self.ang[0]+self.space*i) + self.xy[1] - self.size*self.hwl[0]/2))

            bot_points.append((self.size*self.hwl[1]*np.cos(self.ang[0]+self.space*i)+self.xy[0],
                                self.size*self.hwl[1]*self.tilt*np.sin(self.ang[0]+self.space*i) + self.xy[1] + self.size*self.hwl[0]/2))
        
        #find side points
        A = (top_points[2], top_points[3], 
            bot_points[3], bot_points[2])
        B = (top_points[3], top_points[0], 
            bot_points[0], bot_points[3])
        C = (top_points[0], top_points[1], 
            bot_points[1], bot_points[0])
        D = (top_points[1], top_points[2], 
            bot_points[2], bot_points[1])

        #draw or bottom
        if self.ang[1] > 0:
            pygame.draw.polygon(display, red, top_points)
        else:
            pygame.draw.polygon(display, red, bot_points)

        #draw sides
        if self.ang[0] >= np.pi/4 and self.ang[0] <= 3*np.pi/4:
            pygame.draw.polygon(display, blue, C)
            pygame.draw.polygon(display, green, B)
        elif self.ang[0] >= 3*np.pi/4 and self.ang[0] <= 5*np.pi/4:
            pygame.draw.polygon(display, blue, A)
            pygame.draw.polygon(display, green, B)
        elif self.ang[0] >= 5*np.pi/4 and self.ang[0] <= 7*np.pi/4:
            pygame.draw.polygon(display, blue, A)
            pygame.draw.polygon(display, green, D)
        elif self.ang[0] >= 7*np.pi/4 or self.ang[0] <= np.pi/4:
            pygame.draw.polygon(display, blue, C)
            pygame.draw.polygon(display, green, D)

#create objects
cube1 = cubes()

#create display
pygame.display.set_caption('cubes')
display = pygame.display.set_mode((screen_width, screen_height))

#main
run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        camera_xyz[0] += speed*np.cos(camera_ang)
        camera_xyz[1] += speed*np.sin(camera_ang)
    if keys[pygame.K_DOWN]:
        camera_xyz[0] -= speed*np.cos(camera_ang)
        camera_xyz[1] -= speed*np.sin(camera_ang)
    if keys[pygame.K_LEFT]:
        camera_ang += 0.04
    if keys[pygame.K_RIGHT]:
        camera_ang -= 0.04
    
    #find relative cube info
    cube_distx, cube_disty, box_dist_xy, dif_ang, cube_ang = cube_ang_distxy(camera_xyz[0], camera_xyz[1], box_xyz[0], box_xyz[1], camera_ang)
    cube_dist, dif_ang_xz, cube_ang_xz = cube_ang_distxz(camera_xyz[0], camera_xyz[2], box_xyz[0], box_xyz[2], 0)

    #find cube angle
    cube1.ang = [cube_ang, cube_ang_xz]

    #find cube position x
    ang_ratio = dif_ang/(view_ang_widthxy/2)
    ang_ratioxz = dif_ang_xz/(view_ang_widthxz/2)
    cube1.xy[0] = screen_width/2 - ang_ratio*screen_width/2
    cube1.xy[1] = screen_height/2 - ang_ratioxz*screen_height/2

    #find cube size
    cube1.size = stand_dist/cube_dist

    #draw cube
    cube1.draw()

    #find viewer xy
    view_camera_xy = camera_point_finder(viewer1, camera_xyz[0], camera_xyz[1])
    view_box_xy = box_point_finder(viewer1, box_xyz[0], box_xyz[1], box_size)

    #find viewer xz
    view_camera_xz = camera_point_finder(viewer2, camera_xyz[0], camera_xyz[2])
    view_box_xz = box_point_finder(viewer2, box_xyz[0], box_xyz[2], box_size)

    #draw view backgrounds
    pygame.draw.rect(display, green, viewer1)
    pygame.draw.rect(display, green, viewer2)

    #draw camaera view
    pygame.draw.polygon(display, blue, camera_viewxy(viewer1, view_camera_xy[0], view_camera_xy[1], camera_ang, view_ang_widthxy))
    pygame.draw.polygon(display, blue, camera_viewxz(viewer1, view_camera_xz[0], view_camera_xz[1], camera_ang, view_ang_widthxz))

    #fuck
    pygame.draw.line(display, black, (view_camera_xy[0], view_camera_xy[1]), (view_camera_xy[0]+np.cos(cube_ang)*30, view_camera_xy[1]-np.sin(cube_ang)*30), 3)
    pygame.draw.line(display, black, (view_camera_xy[0], view_camera_xy[1]), (view_camera_xy[0]+np.cos(camera_ang)*30, view_camera_xy[1]-np.sin(camera_ang)*30), 3)

    #draw viewer box and camers
    pygame.draw.circle(display, blue, view_camera_xy, 7) 
    pygame.draw.circle(display, blue, view_camera_xz, 7)
    pygame.draw.rect(display, red, view_box_xy)
    pygame.draw.rect(display, red, view_box_xz)

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False