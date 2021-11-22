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

#shapes
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

    side_groups = top, bot, side1, side2, side3, side4

    return cube, side_groups  #,tops, bots, sides1, sides2, sides3, sides4

#functions
def ang_dist(x1, y1, x2, y2, ang):
    distx = x2 - x1
    disty = y2 - y1
    dist = (distx**2 + disty**2)**0.5

    if distx > 0:
        cube_ang = np.arcsin(disty/dist)
    else:
        if disty > 0:
            cube_ang = np.pi - np.arcsin(disty/dist)
        else:
            cube_ang = -np.pi/2 -(np.pi/2 + np.arcsin(disty/dist))

    if ang <= 0:
        ang = 2*np.pi - np.absolute(ang)%(2*np.pi)
    elif ang >= 2*np.pi:
        ang = 2*np.pi - ang%(2*np.pi)

    dif_ang = cube_ang - ang

    if dif_ang < -np.pi:
        dif_ang = 2*np.pi + dif_ang
    elif dif_ang > np.pi:
        dif_ang = dif_ang - 2*np.pi
    
    return dist, cube_ang, dif_ang

def da_to_xy(dif_ang_x, dif_ang_y, view_width, view_height):
    corners = []
    #find position x
    ang_ratio = dif_ang_x/(view_width/2)
    
    ang_ratioy = dif_ang_y/(view_height/2)
    x = screen_width/2 - ang_ratio*screen_width/2
    y = screen_height/2 - ang_ratioy*screen_height/2

    return (x,y)
    

#classes
class cube:
    whl = (100, 200, 300)
    xyz = [200, whl[1]/2, 600]
    ang_xzr = (0, 0, 0)
    colors = (red, blue, green, blue, green, red)

    def draw(self, cam_xyz, cam_angs_xy, view_angs):
        #find corner points IN:(whl, xyz, ang_xzr), OUT:(corners_xyz, side_groups)
        corners_xyz, side_groups = stationary_cube(self.xyz, self.whl)

        #sort into polys IN:(corners_xyz, side_groups) OUT:(poly_xyz, side_num)
        poly_xy = []
        poly_ad = []
        side_num = list(range(len(side_groups)))
        for i in side_groups:
            poly_xy.append([])
            poly_ad.append(0)
            count = 0
            for n in i:
                count += 1
                #find dist and ang IN:(poly_xyz) OUT:(poly_da)
                dist_xz, cube_ang_x, dif_ang_x = ang_dist(cam_xyz[0], cam_xyz[2], corners_xyz[n][0], corners_xyz[n][2], cam_angs_xy[0])
                dist, cube_ang, dif_ang = ang_dist(0, cam_xyz[1], dist_xz, corners_xyz[n][1], cam_angs_xy[1])

                #convert 3d to 2d IN:(poly_da) OUT:(poly_xy)
                xy = da_to_xy(dif_ang, dif_ang_x, view_angs[0], view_angs[1])

                #add the distances
                poly_ad[-1] += dist

                #append
                poly_xy[-1].append(xy)
            
            #average the distances
            poly_ad[-1] = poly_ad[-1]/count

        #sort cubes by dist large to small IN:(poly_xy, poly_ad, side_num) OUT:(flat_cube, cube_avg_dist, side_num)
        sorted_ad = sorted(poly_ad)
        flat_cube = []
        avg_dist = sum(poly_ad)/len(poly_ad)

        count = 0
        while sum(poly_ad) != 0:
            for i in range(len(poly_ad)):
                if poly_ad[i] == sorted_ad[count]:
                    flat_cube.append(poly_xy[i])
                    side_num[count] = i
                    poly_ad[i] = 0
                    count += 1
        
        return flat_cube, avg_dist, side_num

#scene facts
#camera atributes
camera_xyz = [200,100,100]
camera_angs_xy = [0,0]
cam_speed = 20
camera_view_angles = [np.pi/3, np.pi/3]


#create objects
polygons = []
distances = []
side_numbers = []
cubes = []
for i in range(2):
    cubes.append(cube())

#create display
pygame.display.set_caption('cubes')
display = pygame.display.set_mode((screen_width, screen_height))

#main
run = True
while run:
    #delay and screen reset
    pygame.time.delay(60)
    display.fill(bak_color)

    #find polygon info
    for i in range(len(cubes)):
        polys_xy, avg_dist, side_nums = cubes[i].draw(camera_xyz, camera_angs_xy, camera_view_angles)
        polygons.append(polys_xy)
        distances.append(avg_dist)
        side_numbers.append(side_nums)
    
    #sort polygons by distance
    sorted_dist = sorted(distances)
    polys = []
    side_ident = []
    count = 0
    while sum(distances) != 0:
        for i in range(len(distances)):
            if distances[i] == sorted_dist[count]:
                polys.append(polygons[i])
                side_ident.append(side_numbers[i])
                distances[i] = 0
                count += 1

    #draw polygons
    for i in range(len(polygons)):
        for n in range(len(polygons[i])):
            #color = cubes[i].colors[side_ident[i][n]]
            pygame.draw.polygon(display, blue, polys[i][n])
    
    #get key press inputs
    keys = pygame.key.get_pressed()

    #mouse movement
    mouse = pygame.mouse.get_pos()
    mouse_dif = (mouse[0]-screen_width/2, mouse[1]-screen_height/2)

    camera_angs_xy[0] -= mouse_dif[0]/(screen_width*3)

    #walk around
    if keys[pygame.K_w]:
        camera_xyz[0] += np.cos(camera_angs_xy[0])*cam_speed
        camera_xyz[1] += np.sin(camera_angs_xy[0])*cam_speed
    elif keys[pygame.K_s]:
        camera_xyz[0] += np.cos(camera_angs_xy[0]+np.pi)*cam_speed
        camera_xyz[1] += np.sin(camera_angs_xy[0]+np.pi)*cam_speed
    if keys[pygame.K_a]:
        camera_xyz[0] += np.cos(camera_angs_xy[0]+np.pi/2)*cam_speed
        camera_xyz[1] += np.sin(camera_angs_xy[0]+np.pi/2)*cam_speed
    elif keys[pygame.K_d]:
        camera_xyz[0] += np.cos(camera_angs_xy[0]-np.pi/2)*cam_speed
        camera_xyz[1] += np.sin(camera_angs_xy[0]-np.pi/2)*cam_speed

    #update screen
    pygame.display.update()

    #quite properly
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            pygame.quit() 
            run = False