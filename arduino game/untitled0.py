import numpy as np
import matplotlib.pyplot as plt
import time
import serial
import pygame

ser = serial.Serial('COM5',9600)

run = True
while run:
    st = ser.readline()
    
    if ser.readline()[:] != "b'\xff37\r\n'": # Make sure that the read line isn't this as this is the first line outputted from the serial and it causes errors in the code
            b = ser.readline() # read a byte string line from the Arduino's serial output
            string_n = b.decode() # decode byte string into regular Python string
            int_b = float(string_n)
    print(int_b)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ENTER]:
        run = False

ser.close()