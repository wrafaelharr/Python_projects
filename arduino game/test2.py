import numpy as np
import matplotlib.pyplot as plt
import time
import serial
ser = serial.Serial('COM3',9600)

#ditector box demensions
top = 10
bot = 0
left = 0.1
right = 10

#game perams
length = 2.0
width = 0.20
ball_size = 100
N = 11
runs = 30
pad_speed = 7.5
paddle1 = 4.0
moves = {2.0:-1,1.0:1,0.0:0,3.0:3,4.0:4}
for i in range(runs):
    #read controller
    st = ser.readline()
    tim=time.time()
    if ser.readline()[:] != "b'\xff37\r\n'": # Make sure that the read line isn't this as this is the first line outputted from the serial and it causes errors in the code
        b = ser.readline() # read a byte string line from the Arduino's serial output
        string_n = b.decode() # decode byte string into regular Python string
        int_b = float(string_n)
        
    paddle = np.zeros(N)
    if paddle1 <= 7.5 and moves[int_b<=2]:
        paddle.append(paddle[-1]+moves[int_b])
    else:
        paddle.append(paddle[-1])
    #game controls
    ball_x = 5
    ball_y = 4.5
    move = np.arange(0,pad_speed,pad_speed/runs)
    paddle2 = move[-i]
    paddle1 = paddle[-1]
    
    #inner paddle workings
    hieghts = np.zeros(N)
    paddle[0] = length 
    paddle[-1] = length
    hieghts[0] = paddle1
    hieghts[-1] = paddle2
    #graph set up
    ind = np.arange(N)
    fig = plt.figure()
    ax = fig.add_axes([0,10,1,1])
    #ax definitions
    ax.scatter(ball_x,ball_y,s=ball_size)
    ax.bar(ind, hieghts, width, color='w')
    ax.bar(ind, paddle, width,bottom=hieghts, color='b')
    ax.set_title('pong')
    ax.set_xticks(ind)
    ax.set_yticks(np.arange(0, 11, 1))
    #show
    plt.show()
    #time delay
    time.sleep(.1)
#test cirks
ax.scatter(right,6,s=200)
ax.scatter(left,6,s=200)

ser.close()
