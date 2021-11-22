import numpy as np

#peramiters
num_feat = 8
len_sample = 40

#functions
def decode(sample):
    out_text = ''
    for num in sample:
        out_text += chr(num)
    return out_text

#get data function
def get_file():
    #get fileC:\Users\Lrhgr\Desktop\hobbies\python scripts\nick to name
    text=(open("C:\\Users\\Lrhgr\\Desktop\\hobbies\\python scripts\\nick to name\\training_data.txt").read())
    text=text.lower()
    
    return text

#get data
file = get_file()

#find starting position
start_pos = int(np.random.rand()*(len(file)-len_sample))

#get sample
sample = []
used_l = []
for i in range(len_sample):
    num = ord(file[start_pos+i])
    sample.append(num)

    #check used
    if num not in used_l:
        used_l.append(num)

#make fetaures
features = []
labels = []
for i in range(int(len(sample)/(num_feat+1))):
    features.append(sample[i*(num_feat+1):i*(num_feat+1)+num_feat+1])
    labels.append(features[-1][-1])
    del features[-1][-1]

#make out text
out_text = decode(sample)

#print
print(out_text)
print(used_l)
'''
for i in range(len(features)):
    print(decode(features[i]))
    print(decode(labels)[i])
'''