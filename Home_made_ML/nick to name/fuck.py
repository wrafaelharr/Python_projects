import numpy as np

name = 'raflerafleraafaelrafrafyboyraffytaffysafealsnofealrafaelwyattrafaelharrrafaelliamrafaelharrrafael'

len_name = 6

used = {}

for letter in name:
    #find letters used
    if letter not in used:
        used[letter] = 0

    #count letters
    for lets in used:
        if lets == letter:
            used[letter] += 1

#sort by most
high_to = sorted(used, key=lambda k: used[k], reverse=True)

#acosiate letters
let_per_set = 3
num = len(name)
num_sets = round(num/let_per_set)

#create asoc net
let_asoc = {}
for letter in high_to:
    let_asoc[letter] = np.zeros(len(high_to))

#find reverse num
let_num = {}
for num in range(len(high_to)):
    let_num[high_to[num]] = num

#associate
for set_num in range(num_sets):
    set = name[set_num*3:set_num*3+let_per_set]

    let_asoc[set[1]][let_num[set[0]]] += 1
    let_asoc[set[1]][let_num[set[len(set)-1]]] += 1


#find new sets
let_asoc2 = {}
for letter in let_asoc:
    top3 = {0:'',0:'',0:''}
    pos = 0
    for asoc in let_asoc[letter]:
        count = 0
        for numbs in top3:
            if asoc > numbs:
                top3[count] = asoc

                #let_asoc2[letter] = 
                print(top3)
            count += 1
        pos += 1

#print(let_asoc)