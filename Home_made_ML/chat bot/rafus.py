import numpy as np
import random
from textblob import TextBlob
import math

#peramiters
max_len = 30
streng = [1.1, 0.7, 0.01]
randomness = 0.01

#learning net class
class net_class:
    def start_net(self):
        #create empty net on startup
        self.net = []
        
        #net data
        self.max = 0
    
    #net updater
    def add_row(self):
        #if first time
        if len(self.net) < 1:
            #update net row
            self.net.append([0])
        
        #if its not the first tim
        else:
            #update net rows
            for i in range(len(self.net)):
                self.net[i].append(0)
                
            #add new row
            self.net.append([0]*len(self.net[0]))
    
    #manual manipulate
    def add_prob(self, x, y, amount):
        #update net
        self.net[x][y] += amount
        
        #update data
        if (self.net[x][y]) > self.max:
            self.max = self.net[x][y]
    
    #guess a result    
    def guess(self, inp):
        try:
            return self.net[inp]
        except:
            print('input failed on this number:',inp)
            return self.net[random.randint(0, len(self.net)-1)]
    
#functions
def colapse(probs):
    zeros_check = 1
    if (all(x == 0 for x in probs)):
        zeros_check = 0
        
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

def add_trans(word, word_to, num_to):
    word_to[word] = len(word_to)
    num_to.append(word)
    
    return word_to, num_to

def s_sigmoid(max, inp):
    scale = 2
    margin = 0.01
    #find the slope scaler thing
    slope = math.log(1-(scale/(margin+scale)),np.e**-max)
    
    #do the actual sigmatizing
    rel_val = (scale/(1+np.e**(-inp*slope))) - scale/2
    
    return rel_val

def scale(probs, max, scaler):
    new_probs = []
    for prob in probs:
        new_probs.append(s_sigmoid(max, prob)*scaler)
    
    return new_probs

#create nets
nets = [net_class(), net_class(), net_class()]

#start the nets
for net in nets:
    net.start_net()

#translators
word_to = {}
num_to = []
word_types = []

wt_to = {}
wt_num_to = []

#declare
reply_num = []

#memorys
names = []

#chat loop
chat = True
while chat:
    #get my input
    inp = input('input: ')
    user_in = inp.split()
    
    #find type tags
    tagged = TextBlob(inp).tags
    
    #update translators and increase net size
    for word in tagged:
        #update word type translators
        if word[1] not in wt_num_to:
            #update translations
            wt_to, wt_num_to = add_trans(word[1], wt_to, wt_num_to)
            
            #increase net
            nets[2].add_row()
        
        #update word translator
        if word[0] not in num_to:
            #update translations
            word_to, num_to = add_trans(word[0], word_to, num_to)
            
            #update word type list
            word_types.append(wt_to[word[1]])
            
            #increase net
            nets[0].add_row()
            nets[1].add_row()
        
        #find names
        if word[1] == 'NNP':
            names.append(word[0])
    
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
                print('task options (check, add rows, add prob, guess, guess 2, switch, guess type, peram, exit): ')
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
                
                elif task_sel == 'guess type':
                    #get guess input
                    g_input = input('what word type: ')
                    
                    #do the guess
                    guess_probs = nets[select].guess(wt_to[g_input])
                    
                    #convert to words
                    guess_num = colapse(guess_probs)
                    if guess_num[1] == 1:
                        return_type = wt_num_to[guess_num[0]]
                    else:
                        return_type = 'not trained enough'
                    
                    #return result
                    print('seggested next:',return_type)
                    
                elif task_sel == 'switch':
                    select = int(input('new selection: '))
                
                elif task_sel == 'peram':
                    peram_to = input('which peramiter (max_len, strength, randomness): ')
                    
                    if peram_to == 'max_len':
                        max_len = int(input('how long: '))
                    
                    elif peram_to == 'strength':
                        which_stren = int(input('which strength: '))
                        print('currently:',streng[which_stren])
                        
                        new_stren = int(input('how strong: '))
                        streng[which_stren] = new_stren

                    elif peram_to == 'randomness':
                        print('old randomness:',randomness)
                        new_random = int(input('new randomness: '))
                        randomness = new_random
                        
                elif task_sel == 'goodbye':
                    manual_mode = False
                    chat = False
                
                else:
                    print('no task by that name')
                
            except:
                print('incorrect input')
            
    #convert to numbers
    user_num = []
    for word in tagged:
        user_num.append(word_to[word[0]])
            
    #train next word guesses
    size = len(user_in)-1
    for i in range(len(tagged)):
        #learn 1st word back
        if i+1 <= size:
            #learn
            nets[0].add_prob(user_num[i], user_num[i+1], 1)
        
        #learn 2nd word back
        if i+1 <= size and i > 0:
            #learn
            nets[1].add_prob(user_num[i-1], user_num[i+1], 1)
            
        #learn word types
        if i+1 <= size:
            #learn
            nets[2].add_prob(wt_to[tagged[i][1]], wt_to[tagged[i+1][1]], 1)
    
    #get first word
    if inp == 'continue' and len(reply_num) > 2:   
        reply_num = [reply_num[-2], reply_num[-1]]
    else:
        reply_num = [random.randint(0, len(num_to))]
    
    #generate reply
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
                probs = [scale(nets[0].guess(reply_num[-1]), nets[0].max, streng[0])]
                
                #generate probability 2
                if len(reply_num) > 1:
                    probs.append(scale(nets[1].guess(reply_num[-2]), nets[1].max, streng[1]))
                    
                #generate word type probability
                try:
                    type_guess = scale(nets[2].guess(word_types[reply_num[-1]]), nets[2].max, streng[2])
                    best_type = colapse(type_guess)
                    
                    #add type probability
                    type_prob = np.zeros(len(num_to))
                    for i in range(len(type_prob)):
                        if word_types[i] == best_type[0]:
                            type_prob += max(type_guess)
                    probs.append(type_prob)
                except:
                    print(reply_num[-1],'--------------------')
                
                #add the probabiltys
                probs = row_adds(probs)
                
                #add randomness
                if (all(x == 0 for x in probs) != True):
                    for i in range(len(probs)):
                        probs[i] = probs[i] + s_sigmoid(randomness, random.uniform(-randomness, randomness))
                    
                #find word
                word = colapse(probs)
                
                #quite if no suggested words
                if word[1] == 1:
                    #add new word
                    reply_num.append(word[0])
                else:
                    gen = False
            
            #increase word counter
            count += 1                  
       
    #convert reply to to text
    reply = ''
    for num in reply_num:
        try:
            reply += num_to[num] + ' '
        except:
            print(num,'is not in translator')
        
    #reply
    print(word_to)
    print(reply)