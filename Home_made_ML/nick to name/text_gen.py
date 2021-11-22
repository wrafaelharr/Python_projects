import numpy as np

#perameters
sample_txt = 'yeah Im that dude just a little rude got some attitude. You know how it goes throwing blows, drive around my grows you look a lil gross. I know someone you dont I got whatchu need the shneed and a little speed'
read_dist = 3
read_len = 5
first_let = 'y'

#abc encoder
abcs1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!$()*&^'

#find how many letter are used
abcs = ''
for letter in abcs1:
    if letter in sample_txt:
        abcs += letter

#abc decoder
abc_to = {}
count = 0
for letter in abcs:
    abc_to[letter] = count
    count += 1

#encode txt
enco_txt = ''
for letter in sample_txt:
    enco_txt += str(abc_to[letter]) 

#make features and labels
features = []
labels = []
weights = np.zeros(read_dist)
for i in range(read_len):
    features.append(enco_txt[i:i+read_dist])
    labels.append(enco_txt[i+read_dist])

#idk


'''
#create association network
asoc_net = {}
for num in range(len(abcs)):
    asoc_net[num] = {}
    for num2 in range(len(abcs)):
        asoc_net[num][num2] = np.zeros(read_dist)

#asoc
for pos in range(len(labels)):
    count = 0
    for inpt in features[pos]:
        asoc_net[int(labels[pos])][int(inpt)][count] += 1
        count += 1
'''   

print(labels)
print(features)
print()