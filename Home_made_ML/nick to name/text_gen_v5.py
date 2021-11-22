import numpy as np

#peramiters
num_feat = 15
len_xl_net = 2
len_sample = 10000

#get data function
def get_file():
    #get fileC:\Users\Lrhgr\Desktop\hobbies\python scripts\nick to name
    text=(open("C:\\Users\\Lrhgr\\Desktop\\hobbies\\python scripts\\nick to name\\training_data.txt").read())
    text=text.lower()
    
    return text

#get data
file = get_file()

#find starting phrase
random_position = round((len(file)-num_feat)*np.random.rand())
start = file[random_position:random_position+num_feat]

#shorten file
random_position = round((len(file)-num_feat)*np.random.rand())
file = file[random_position:random_position+len_sample]

#encoder
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?!;:'
deco = ''
for letter in abc:
    if (letter in file or letter in start) and letter != '\n':
        deco += letter

#decoder
enco = {}
for i in range(len(deco)):
    enco[deco[i]] = i


#encode file
data = []
bad_letters = []
for letter in file:
    try:
        data.append(enco[letter])
    except:
        bad_letters.append(letter)

#create features and labels
features = []
labels = []
for i in range(len(data)-num_feat):
    features.append(data[i:i+num_feat])
    labels.append(data[i+num_feat])

#randomize features and labels
new_feat = []
new_lab = []
while labels:
    i = round((len(labels)-1)*np.random.rand())
    new_lab.append(labels[i])
    new_feat.append(features[i])

    del labels[i], features[i]
labels = new_lab
features = new_feat

#asocciation class
class asoc():
    net = []
    net_size = len(deco)
    xl_net = [len(deco)**len_xl_net, len(deco)]
    both = []

    def create(self):
        self.net = np.zeros((self.net_size, self.net_size))
    
    def create_v2(self):
        self.net = np.zeros((self.net_size, self.net_size))
    
    def train(self, feat_num):
        for i in range(len(labels)):
            self.y = features[i][feat_num]
            self.x = labels[i]

            self.net[self.y][self.x] += 1

            self.both.append([self.y, self.x])


#create and train asoc
asocs = []
for i in range(num_feat):
    asocs.append(asoc())
    asocs[i].create()
    asocs[i].train(i)


#num predict function
def pred(feature):
    odds = []
    for i in range(num_feat):
        odds.append(asocs[i].net[feature[i]])

    predic = {}
    for num in range(len(enco)):
        predic[num] = 0
        for i in range(num_feat):
            predic[num] += odds[i][num]

        predic[num] = predic[num]/num_feat

    predo = predic
    predic = sorted(predic, key=lambda k: predic[k], reverse=True)

    return predic

#letter predict function
def lpred(txt):
    txt = txt[-num_feat:]
    code = []
    for i in txt:
        code.append(enco[i])
    
    pred_num = pred(code)

    return deco[pred_num[0]]

#make a sentance
out_txt = start
for i in range(70):
    out_txt += lpred(out_txt)

#labels to text
label_txt = ''
for label in labels:
    label_txt += deco[label]

#print
print(start)
print(out_txt)
print(enco[' '])
print(asocs[1].net[0][enco[' ']])
print(asocs[1].net[0])
