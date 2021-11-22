import numpy as np

#permeters
nicks = 'leahsofiaharrsoffypofesissyleahhardsofialeahsofiaharrsososofia'
name_len = 5
first_letter = 's'

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

print(name_lets)
print(name)
print(asocs_r['s'])