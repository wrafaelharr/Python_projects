import numpy as np

sample1 = 'feyeah Im that dude just a little rude got some attitude. You know how it goes throwing blows, drive around my grows you look a lil gross. I know someone you dont I got whatchu need the shneed and a little speed'
sample2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?! fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuckfuckfuck fuckfuck fuck fuck fuck fuck fu fuf fu fu fu uck uck uck uck ck ck ck uck uck'
sample3 = 'i kno wthis might not work itbut maybe it jsut needs lots of text to feed to it i just gotta get this boy to be responsive somehow and not just get stuck on a single letter i think it could just not have enough'
sample4 = 'data to populate its giant grid thing i built idk this is probably what tensor flow does but i dont know what a tensor is I know how to make this becouse i just came up with it peice by peice didnt even'
sample5 = 'google that shit just figured it out feels good but i still gotta get it working'
sample = sample1 #+ sample2 + sample3 + sample4 + sample5
sample = 'fuck you es'
read_wind = 3
read_len = len(sample)
start = 'yes'

#encoder
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?!'

#shortain
num_to = []
for letter in abc:
    if letter in sample:
        num_to.append(letter)

#decoder
abc_to = {}
for i in range(len(num_to)):
    abc_to[num_to[i]] = i

#encode
enco = []
for letter in sample:
    enco.append(abc_to[letter])

#get features and labels
features = []
labels = []
for i in range(len(enco)-read_wind):
    labels.append(enco[i+read_wind])
    features.append(enco[i: i+read_wind])

#asociation layer
class asoc():
    layer = {}

    def create(self, options):
        for feature in options:
            self.layer[feature] = {}
            for label in options:
                self.layer[feature][label] = 0

    def train(self, feature, label):
        self.layer[feature][label] += 1

#create layers
layer1 = asoc()
layer2 = asoc()
layer3 = asoc()

#generate structure
used_nums = range(len(abc_to))
layer1.create(used_nums)
layer2.create(used_nums)
layer3.create(used_nums)

#train the layers
for i in range(len(labels)):
    layer1.train(features[i][0], labels[i])
    layer2.train(features[i][1], labels[i])
    layer3.train(features[i][2], labels[i])

#predict function
def pred(feature):
    odds1 = layer1.layer[feature[0]]
    odds2 = layer2.layer[feature[1]]
    odds3 = layer3.layer[feature[1]]

    pred = {}
    for num in used_nums:
        pred[num] = (odds1[num] + odds2[num] + odds3[num])/3
    
    pred = sorted(pred, key=lambda k: pred[k], reverse=True)

    return pred

#letter predict function
def lpred(txt):
    txt = txt[-read_wind:]

    code = []
    for i in txt:
        code.append(abc_to[i])
    
    pred_num = pred(code)

    return num_to[pred_num[0]]

#make a sentance
out_txt = start
for i in range(20):
    out_txt += lpred(out_txt)
    
#print(features)
#print(labels)
print(out_txt)
print(lpred('fuc'))
print(pred([0,2,3]))
