import numpy as np
import matplotlib.pyplot as plt
import time
import serial

ser = serial.Serial('COM3',9600)

tim = 0
plyr = 0
pr = 0
sped = 0
en = 0
ttim = []
pos = []
cnt = []
right = []
left = []
pos1 = []
moves = {2.0:-1,1.0:1,0.0:0,3.0:3,4.0:4}
run = True

while run:
    for i in range(300):
        st = ser.readline()
        tim=time.time()
        if ser.readline()[:] != "b'\xff37\r\n'": # Make sure that the read line isn't this as this is the first line outputted from the serial and it causes errors in the code
            b = ser.readline() # read a byte string line from the Arduino's serial output
            string_n = b.decode() # decode byte string into regular Python string
            int_b = float(string_n)
            
        print(i)
        fig, ax=plt.subplots()
    
        pos.append(plyr)
        cnt.append(i)
        left.append(np.sin(cnt[-1]*(0.0005*(i+1)))-1)
        right.append(np.sin(cnt[-1]*(0.0005*(i+1)))+1)
        plyr = pos[-1]+moves[int_b]*(0.02*sped)
        pos1.append(plyr)
        
        if moves[int_b]!=0.0:
            sped = sped+2
        if en!=st:
            sped = 1
        
        while len(pos)>20/(0.009*(i+1)):
            del pos[0]
            del cnt[0]
            del left[0]
            del right[0]
        
        ax.scatter(pos[-1],cnt[0]+7)
        ax.plot(left,cnt,'r')
        ax.plot(right,cnt,'r')
        plt.show()
        
        en = ser.readline()
        if len(right)>13:
            if pos[-1]>right[-13] or pos[-1]<left[-13] or int_b==4.0:
                print('you loose \nyou made it',str(cnt[-1])+'ft out of 300ft')
                if cnt[-1]>highscores[-1]:
                    print('NEW HIGHSCORE!')
                    highscores.append(cnt[-1])
                    if len(highscores)>5:
                        del highscores[0]
                print('high scores:',highscores)
                fig, ax=plt.subplots()
                ax.plot(pos1)
                ax.plot(np.sin(np.arange(0,len(pos1)))+1)
                ax.plot(np.sin(np.arange(0,len(pos1)))-1)
                plt.show()
                pos1 = []
                break
        ttim.append(time.time()-tim)
        
    print('\npress start or end: ')
    
    while int_b!=3.0 and int_b!=4.0:    
        b = ser.readline() 
        string_n = b.decode() 
        int_b = float(string_n)
 
    if int_b==3.0:
        print('alright. lets go again')
        tim = 0
        plyr = 0
        pr = 0
        sped = 0
        ttim = []
        pos = []
        cnt = []
        right = []
        left = []
    elif int_b==4.0:
        print('end game')
        break
        
ser.close()
print(sum(ttim))