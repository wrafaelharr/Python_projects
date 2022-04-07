import numpy as np
import random
import pyttsx3

engine = pyttsx3.init()

#chat
'''
chat = True
while chat:
    #get input
    UI = input('whatchu say')

    #quite
    if UI == 'goodbye':
        chat = False
'''

#what to say 
say = 'dante sucks at coding.'

# talk
engine.say(say)
engine.runAndWait()

#what to say 
say = 'He is also mega non bussing bozo plus ratio, and rafael be mad fine and etai is a internet troll'

# talk
engine.say(say)
engine.runAndWait()
engine.endLoop()