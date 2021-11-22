import numpy as np

def get_file():
    #get fileC:\Users\Lrhgr\Desktop\hobbies\python scripts\nick to name
    text=(open("C:\\Users\\Lrhgr\\Desktop\\hobbies\\python scripts\\nick to name\\training_data.txt").read())
    text=text.lower()
    
    return text

#get training text
train_file = get_file()

#assighn text 
sample = train_file[:20000]


#perameters
read_wind = 20

#find starting word
rand_pos = round(np.random.rand()*(len(sample)-read_wind))
start = sample[rand_pos: rand_pos+read_wind]

#encoder
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?!'

#manage data
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
unicodables = []
enco = []
for letter in sample:
    try:
        enco.append(abc_to[letter])
    except:
        unicodables.append(letter)

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

    def train(self, feature, label, lay_num):
        dist_scaler = lay_num/read_wind
        self.layer[feature][label] += 1*dist_scaler

#create layers
used_nums = range(len(abc_to))
layers = []
for i in range(read_wind):
    #create layer objects
    layers.append(asoc())

    #create layer structure
    layers[i].create(used_nums)

    #train layer
    for n in range(len(labels)):
        layers[i].train(features[n][i], labels[n], i)

def pred(feature):
    odds = []
    for i in range(read_wind):
        #print(feature)
        odds.append(layers[i].layer[feature[i]])

    predic = {}
    for num in used_nums:
        predic[num] = 0
        for i in range(read_wind):
            predic[num] += odds[i][num]

        predic[num] = predic[num]/read_wind

    predic = sorted(predic, key=lambda k: predic[k], reverse=True)

    return predic

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
for i in range(70):
    out_txt += lpred(out_txt)

#print(layers[0].layer[0])
print(out_txt[:read_wind])
print(out_txt[read_wind:])
#print(lpred('fuc'))