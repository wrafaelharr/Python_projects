import numpy as np

#peramiters
sent_len = 10

#variables
enco = {}
word_bank = []
net = []
mark_net = []
reply = []

#intro
chat = True
print('-------HELLO--------')

#chat loop
while chat:
    #say hello
    user_in = input('User in: ')

    #end
    if user_in == 'goodbye':
        chat = False
        print('Goodbye')
    
    #break down
    user_words = user_in.split()

    #add to word bank
    num_added = len(word_bank)
    for word in user_words:
        if word not in word_bank:
            word_bank.append(word)
    num_added = len(word_bank) - num_added

    #decoder
    count = 0
    for word in word_bank:
        enco[word] = count
        count += 1
    
    #expand net width
    for i in range(len(net)):
        net[i].append(0)
        mark_net[i].append(0)

    #expand learning net hieght
    blank_row = [0]*len(word_bank)
    for i in range(num_added):
        net.append(blank_row)
        mark_net.append(blank_row)
    
    #markov learn
    for i in range(len(user_words)-1):
        mark_net[enco[user_words[i]]][enco[user_words[i+1]]] += 1
    
    #make first word
    rand_word = int(np.random.rand()*len(word_bank))
    reply.append(word_bank[rand_word])
    
    
    #right sentance
    for i in range(sent_len):
        best_let = mark_net[enco[reply[-1]]]
        for i in range(len(best_let)):
            if best_let[i] == max(best_let) and sum(best_let) != 0:
                nxt_let = i
            else:
                nxt_let = int(np.random.rand()*len(word_bank))

        reply.append(word_bank[nxt_let])
    
    #create out text
    out_txt = ''
    for word in reply:
        out_txt += ' '+word

    #print out
    print(out_txt)