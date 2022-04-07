import numpy as np

#functions
def GrowNet(net, by):
    for j in range(by):
        #increase the net height
        net.append([0])

        #increase the net width
        for i in range(len(net)):
            #find amount increase
            short_by = len(net[0]) - len(net[i])

            #inlarge
            if len(net[0]) < len(net): net[i].append(0)
            for n in range(short_by): net[i].append(0)

    return net

#banks
word_to = {}
num_to = []

#nets
net1 = []

#main loop
run = True
while run:
    #get input
    user_in = input('INPUT:')

    #create reply
    say = ''

    #get words
    words = user_in.split()

    #remember words
    for word in words:
        if word not in num_to:
            #increase number to word list
            num_to.append(word)

            #increase word to number dictionary
            word_to[word] = len(num_to)

            #grow net
            net1 = GrowNet(net1, 1)

    #learn
    for i in range(len(words)-2):
        print(len(words))
        print(words[i],words[i+1])
        net1[word_to[words[i]]][word_to[words[i+1]]] += 1

    #guess
    for i in range(5):
        #first word
        #print(words[np.random(0, len(words))])
        asoc = []
        if len(say) == 0: asoc = net1[0]
        else: asoc = word_to[say.split()[-1]]

        #add word
        max_asoc = max(asoc)
        for a in range(len(asoc)):
            if asoc[a] == max_asoc:
                guess = a

        #update words
        say += num_to[net1[word_to[say.split()[-1]]][a]]
    #say = (word_to,net1)

    #end loop
    if user_in == 'goodbye': run = False

    #machine out
    print(say)

print('GOODBYE')