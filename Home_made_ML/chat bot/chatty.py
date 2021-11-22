import numpy as np
import random

#asociations
net1 = []
net2 = []

#conversion
word_to = {}
num_to = []

#main loop
run = True
while run:
    #get the input
    user_in = input('input: ')
    words_in = user_in.split()

    #say goodby
    if user_in == 'goodbye':
        run = False
    
    #check words
    if user_in == 'check:':
        word_to_check = input('check this word:')
        
        print(num_to)
        print(net1[word_to[word_to_check]])
        print(net2[word_to[word_to_check]])
        
        #find likely word
        #add liely hoods
        likely_hood = []
        for i in range(len(net1[reply[-1]])):
            likely_hood.append(net1[reply[-1]][i] + net2[reply[-1]][i])
            
        #find next word
        next_word = likely_hood.index(max(likely_hood))
        
        print(num_to[next_word])
    
    #otherwise
    else:
        #run through inputs
        for word in words_in:
            #check if used
            if word not in num_to:
                #update converters
                word_to[word] = len(word_to)
                num_to.append(word)

                #update net rows
                for i in range(len(net1)):
                    net1[i].append(0)
                    net2[i].append(0)

                #add new row
                net1.append([0]*len(num_to))
                net2.append([0]*len(num_to))
        
        #learn
        for i in range(len(words_in)-1):
            try:
                net1[word_to[words_in[i]]][word_to[words_in[i+1]]] += 1
                if len(words_in) > 3 and i > 0:
                    net2[word_to[words_in[i-1]]][word_to[words_in[i+1]]] += 1
            except:
                print('--------error--------')
                print(i)
                print(i+1)

        #find first word
        reply = [random.randint(0, len(num_to)-1)]

        #generate reply
        count = 0
        gen = True
        while gen:
            #quite if no suggested word
            if (all(x == 0 for x in net1[reply[-1]]) and (len(reply) > 2 and all(x == 0 for x in net2[reply[-2]]))) or count > 6:
                gen = False
                    
            #find next word
            else:
                #add liely hoods
                likely_hood = []
                if len(reply) > 1:
                    for i in range(len(net1[reply[-1]])):
                        likely_hood.append(net1[reply[-1]][i] + net2[reply[-2]][i])
                else:
                    likely_hood = net1[reply[-1]]
                    
                #find next word
                next_word = likely_hood.index(max(likely_hood))
                
                reply.append(net1[reply[-1]][next_word])
            
            #increase backup count
            count += 1

        #convert reply to text
        txt_reply = ''
        for num in reply:
            txt_reply += num_to[num]+' '

        #reply
        print(txt_reply)
