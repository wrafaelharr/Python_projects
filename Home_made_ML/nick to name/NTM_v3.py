import numpy as np

#permeters
nicks = 'rafael'
name_len = 6
first_letter = 'r'

#find common ness and top used letters
def mos_common(txt, length):
    #veriables
    times_used = {}

    #find times used
    for letter in nicks:
        #add if not found
        if letter not in times_used:
            times_used[letter] = 0
        else:   
            #count time used
            times_used[letter] += 1

    #find name letters
    name_lets = sorted(times_used, key=lambda k: times_used[k], reverse=True)
    name_lets = name_lets[0:name_len]

    return name_lets

def asoc_1layer(name_lets, nicks):
    #create framework
    asocs_r = {}
    asocs_l = {}
    let_to = {}
    pos = 0
    for letter in name_lets:
        asocs_r[letter] = {}
        asocs_l[letter] = {}
        for let in name_lets:
            asocs_r[letter][let] = 0
            asocs_l[letter][let] = 0
        pos += 1

    #find asocs
    pos = 0
    for letter in nicks:
        if letter in name_lets:
            #socs
            if nicks[pos-1] in name_lets:
                asocs_l[letter][nicks[pos-1]] += 1

            if pos+1 < len(nicks):
                if nicks[pos+1] in name_lets:
                    asocs_r[letter][nicks[pos+1]] += 1
        
        pos += 1

    for letter in name_lets:
        asocs_r[letter] = sorted(asocs_r[letter], key=lambda k: asocs_r[letter][k], reverse=True)
    
    return asocs_l, asocs_r

def asoc_read(asocs_r):
    if first_letter in name_lets:
        name = first_letter
    else:
        name = name_lets[round(np.random.rand()*(name_len-1))]

    for i in range(name_len-1):
        if len(name) > 2:
            if name[-2] != asocs_r[name[i]][0]:
                name += asocs_r[name[i]][0]
            else:
                name += asocs_r[name[i]][1]
        else:
            name += asocs_r[name[i]][0]
    
    return name

def asoc_read_v2(asocs_l, asocs_r):
    if first_letter in name_lets:
        name = first_letter
    else:
        name = name_lets[round(np.random.rand()*(name_len-1))]

    for i in range(name_len-1):
        if len(name) > 2:
            if name[-2] != asocs_r[name[i]][0]:
                name += asocs_r[name[i]][0]
            else:
                #name += asocs_r[name[i]][1]

                for nxt_let in asocs_l:
                    if name[-1] == nxt_let[0]:
                        name += nxt_let
                        
        else:
            name += asocs_r[name[i]][0]
    
    return name

#workzone
name_lets = mos_common(nicks, name_len)
print(name_lets)

asocs = asoc_1layer(name_lets, nicks)
print(asoc_read(asocs[1]))
print(asoc_read_v2(asocs[0], asocs[1]))

print(asocs[1]['f'])