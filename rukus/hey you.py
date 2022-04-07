import numpy as np
import pyttsx3

engine = pyttsx3.init()

# learning net
class net():
    

# chat loop
chat = True
while(chat):
    # jget input
    User_in = input('command: ')

    #close chat
    if User_in == 'quit':
        chat = False

    #parse words
    User_words = User_in.split()
    
    #talk
    say = ''
    if User_words[0] == 'say:':
        say = User_in[len(User_words[0]):]

    # learn


    # talk
    engine.say(say)
    engine.runAndWait()

