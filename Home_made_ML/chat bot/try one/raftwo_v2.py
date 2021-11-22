import numpy as np

#peramiters
sent_length = 15

#veriables
enco = []
net = []
frow = []
net2 = []
frow2 = []
nxt = 0

#chat fucntion
chat = True
while chat:
    #get input
    user_in = input('Input: ')

    #get words
    words = user_in.split()

    #encoder
    len_change = len(enco)
    for wrd in words:
        if wrd not in enco:
            enco.append(wrd)
    len_change = -(len_change-len(enco))

    #decoder
    deco = {}
    for i in range(len(enco)):
        deco[enco[i]] = i

    #close off
    if user_in == 'goodbye':
        chat = False
    
    #build net
    frow += [0]*len_change
    frow2 += [0]*len_change
    for i in range(len_change):
        net.append(frow)
        net2.append(frow)

    #find best replys
    best_rep = []
    for wrd in words:
        best = max(net[deco[wrd]])
        count = 0
        for num in net[deco[wrd]]:
            if num == best:
                best_rep.append(enco[count])
            count += 1

    #reply
    reply = ''
    rando = int(np.random.rand()*len(enco))
    wrds = best_rep + enco[rando-3:rando]
    count = 0
    while wrds:
        #find next word
        if reply:
            nxt = max(net2[deco[reply.split()[-1]]])
            count2 = 0
            for pos in net2[deco[reply.split()[-1]]]:
                if pos == nxt:
                    leto = count2
                count2 += 1

        rand_sel = int(np.random.rand()*len(wrds))

        #find more likely
        if nxt:
            if nxt > max(net[deco[reply[-1]]]):
                wordos = enco[leto]
            else:
                wordos = wrds[rand_sel]
        else:
            wordos = wrds[rand_sel]


        reply += wordos+' '
        del wrds[rand_sel]

        if np.random.rand()*100 < sent_length:
            break
        count += 1
    print(reply)

    #learn
    count = 0
    for wrd in words:
        feat = deco[wrd]
        try:
            label = deco[reply.split()[count]]

            net[label][feat] += 1
        except:
            pass

        count += 1
    
    #learn structure
    for i in range(len(words)-1):
        net2[words[i]][words[i+1]] += 1
    
print(net)
print(enco)
print(deco)