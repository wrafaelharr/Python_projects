import numpy as np

def get_file():
    #get fileC:\Users\Lrhgr\Desktop\hobbies\python scripts\nick to name
    text=(open("C:\\Users\\Lrhgr\\Desktop\\hobbies\\python scripts\\nick to name\\training_data.txt").read())
    text=text.lower()
    
    return text

#get training text
train_file = get_file()

#perameters
read_wind = 10
train_size = 100000
train_slope = 2#high = less drop off
same_scale = 0.01#smaller = more effect
dif_scaler = 4#bigger = more
random_scale = 0

#randomize sample
rand_pos = round(np.random.rand()*len(train_file))
sample = train_file[rand_pos:rand_pos+train_size]

#find starting word and sample
rand_pos = round(np.random.rand()*(train_size-read_wind))
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

#shuffle features and labels
new_feat = []
new_lab = []
while labels:
    i = round((len(labels)-1)*np.random.rand())
    new_lab.append(labels[i])
    new_feat.append(features[i])

    del labels[i], features[i]
labels = new_lab
features = new_feat

#asociation layer
class asoc():
    layer = {}

    def create(self, options):
        for feature in options:
            self.layer[feature] = {}
            for label in options:
                self.layer[feature][label] = 0

    def train(self, feature, label, lay_num, itter):
        #training rules
        dist_scaler = lay_num/read_wind
        itter_scaler = 1/(n/train_slope+1)

        samness_scaler = 1
        difness = 1
        if feature == label:
            samness_scaler = same_scale  
        if feature != label:
            difness = dif_scaler
        randness = 1+(random_scale*np.random.rand())

        self.layer[feature][label] += 10*dist_scaler*itter_scaler*samness_scaler*difness*randness

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
        layers[i].train(features[n][i], labels[n], i, n)

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