import numpy as np

#peramiters
sentence_length = 15

#chat funstionfu
words = []
word = ''
enco = []
net = []
chatting = True
while chatting:
    #get my side
    Uin = input('User In: ')

    #find words
    for letter in Uin:
        if letter == ' ' or letter == '.':
            words.append(word)
            word = ''
        else:
            word += letter
    if Uin != ' ' and Uin != '.':
        words.append(word)
        word = ''

    #quite
    if Uin == 'goodbye':
        chatting = False

    #encoder
    for wrd in words:
        if wrd not in enco:
            enco.append(wrd)

    #decoder
    deco = {}
    count = 0
    for wrd in enco:
        deco[count] = wrd
        count += 1

    #asociate words
    new_wrds = len(enco)
    #net = np.zeros(len(enco))
    #net = np.vstack([net, [1,2]])
    
    
    #reply
    reply = ''
    wrds = enco
    while wrds:
        rand_sel = int(np.random.rand()*len(wrds))
        reply += wrds[rand_sel]+' '
        del wrds[rand_sel]

        if np.random.rand()*100 < sentence_length:
            break
    print(reply)

print('----------------net')
print(net)

print('----------------------------------')
print('GOODBYE SIR')

print(enco)