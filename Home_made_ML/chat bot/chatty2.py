import numpy as np
import random
import pyttsx3
engine = pyttsx3.init()

#peramiters
max_len = 15
streng = [1.2, 0.7, 1]

#learning net class
class net_class:
    def start_net(self):
        #create empty net on startup
        self.net = []
    
    #net updater
    def add_row(self):
        #if first time
        if len(self.net) < 1:
            #update net row
            self.net.append([0])
            
            #add new row
        
        #if its not the first tim
        else:
            #update net rows
            for i in range(len(self.net)):
                self.net[i].append(0)
                
            #add new row
            self.net.append([0]*len(self.net[0]))
    
    #manual manipulate
    def add_prob(self, x, y, amount):
        self.net[x][y] += amount
    
    #guess a result    
    def guess(self, inp):
        try:
            return self.net[inp]
        except:
            print('input failed on this number:',inp)
            return self.net[random.randint(0, len(self.net)-1)]
    
#functions
def colapse(probs):
    zeros_check = 0
    if (all(x == 0 for x in probs)):
        zeros_check = 1
        
    return [probs.index(max(probs)), zeros_check]

def row_adds(probs):
    new_prob = []
    
    #add them
    for i in range(len(probs[0])):
        #add
        prob = 0
        for probo in probs:
            prob += probo[i]
            
        #return
        new_prob.append(prob)
    
    return new_prob

def add_word(word, word_to, num_to):
    word_to[word] = len(word_to)
    num_to.append(word)
    
    return word_to, num_to
    
    
#create nets
nets = [net_class(), net_class(), net_class()]

#start the nets
for net in nets:
    net.start_net()

#convert numbers and letters
word_to = {}
num_to = []

#declare
reply_num = []

#chat loop
chat = True
while chat:
    #get my input
    inp = input('input: ')
    user_in = inp.split()
    
    #option to quite
    if inp == 'goodbye':
        chat = False
    
    #manual net controls
    elif inp == 'manual':
        #get selection
        select = input('which: ')
        
        #set to manual mode
        manual_mode = True
        
        while manual_mode:
            try:
                #convert select
                select = int(select)
                
                #select tasks
                print('task options: check, add rows, add prob, guess, guess 2, switch, exit')
                task_sel = input('task: ')
                
                if task_sel == 'exit':
                    manual_mode = False
                
                elif task_sel == 'check':                 
                    print(nets[select].net)
                
                elif task_sel == 'add rows':
                    amount = input('how many: ')
                    
                    for i in range(int(amount)):
                        #effect nets
                        nets[select].add_row()
                    
                    #show results
                    print(nets[select].net)
                    
                elif task_sel == 'add prob':
                    #whats it look like now
                    print(nets[select].net)
                    
                    #get manual pos
                    pos = input('add x and y sep by space: ')
                    
                    #convert pos to usable
                    pos = pos.split()
                    for i in range(2):
                        pos[i] = int(pos[i])
                    
                    #effect nets
                    nets[select].add_prob(pos[0],pos[1],1)
                    
                    #show results
                    print(nets[select].net)
                
                elif task_sel == 'guess':
                    #get row to guess
                    row = input('row: ')
                    
                    #get guess data
                    data = nets[select].guess(int(row))
                    
                    #find the guess
                    guess = colapse(data)
                    
                    #return info
                    print('best guest:',guess)
                
                elif task_sel == 'guess more':
                    datas = []
                    row_collect = True
                    while row_collect:
                        #get row to guess
                        row = input('row: ')
                        
                        if row == 'done':
                            row_collect = False
                        else:
                            #get guess data
                            datas.append(nets[select].guess(int(row)))
                    
                    #add rows
                    new_data = row_adds(datas)
                    
                    #find the guess
                    guess = colapse(new_data)
                    
                    #return info
                    print(new_data)
                    print('best guest:',guess)
                
                elif task_sel == 'switch':
                    select = int(input('new selection: '))
                    
                else:
                    print('no task by that name')
                
            except:
                print('incorrect input')
            
    #update translators
    for word in user_in:
        if word not in num_to:
            #update translations
            word_to, num_to = add_word(word, word_to, num_to)
            
            #update the nets
            for net in nets:
                net.add_row()
    
    #learn
    size = len(user_in)-1
    for i in range(len(user_in)):
        #learn 1st word back
        if i+1 <= size:
            #learn
            nets[0].add_prob(word_to[user_in[i]], word_to[user_in[i+1]], streng[0])
        
        #learn 2nd word back
        if i+1 <= size and i > 0:
            #learn
            nets[1].add_prob(word_to[user_in[i-1]], word_to[user_in[i+1]], streng[1])
            
        #learn to reply
        if reply_num != []:
            for num in reply_num:
                nets[2].add_prob(word_to[user_in[i]], num, streng[2]/len(reply_num))
    
    #get first word
    if inp == 'continue' and len(reply_num) > 2:   
        reply_num = [reply_num[-2], reply_num[-1]]
    else:
        reply_num = [random.randint(0, len(num_to))]
    
    #generate reply
    try:
        count = 0
        gen = True
        while gen:
            #max out
            if count > max_len:
                gen = False
            #otherwise
            else:
                if len(num_to) > 0:
                    #generate probability 1
                    probs = [nets[0].guess(reply_num[-1])]
                    
                    #generate probability 2
                    if len(reply_num) > 1:
                        probs.append(nets[1].guess(reply_num[-2]))
                    
                    #generate reply probability
                    if reply_num != []:
                        probs.append(nets[2].guess(word_to[user_in[random.randint(0, len(user_in)-1)]]))
                    
                    #add the probabiltys
                    probs = row_adds(probs)
                        
                    #find word
                    word = colapse(probs)
                    
                    #quite if no suggested words
                    if word[1] == 0:
                        #add new word
                        reply_num.append(word[0])
                    else:
                        gen = False
                
                #increase word counter
                count += 1                  
    except:
        print('fuck')
    #convert numbers to words
    reply = ''
    for num in reply_num:
        if num < len(reply_num)-1:
            reply += num_to[num] + ' '
    
    #reply
    print(reply)

    # talk
    engine.say(reply)
    engine.runAndWait()
