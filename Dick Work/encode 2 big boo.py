abc = 'abcdefghijklmnopqrstuvwxyz '

def numbify(text):
    numbs = ''
    for i in range(len(text)):
        if abc.find(text[i]) < 10:
            numbs = numbs + '0' + str(abc.find(text[i]))
        else:
            numbs = numbs + str(abc.find(text[i]))
    return numbs

def encode(m,b,numbs):
    en_nums = ''
    num_char = int(len(numbs)/2)
    for i in range(num_char):
        x = int(str(numbs[i*2])+str(numbs[i*2+1]))
        y = m*x + b
        if y < 10:
            en_nums = en_nums + '0' + str(y)
        else:
            en_nums = en_nums + str(y)
    return m,b,en_nums

def decode(m,b,en_nums):
    de_nums = ''
    num_char = int(len(en_nums)/2)
    for i in range(num_char):
        y = int(str(en_nums[i*2])+str(en_nums[i*2+1]))
        x = int((y - b)/m)
        if x < 10:
            de_nums = de_nums + '0' + str(x)
        else:
            de_nums = de_nums + str(x)
    return(de_nums)

def textify(numbs):
    text = ''
    num_char = int(len(numbs)/2)
    for i in range(num_char):
        x = int(str(numbs[i*2])+str(numbs[i*2+1]))
        text = text + abc[x]
    return text

m = 3
b = 5
print(encode(m,b,numbify('butt nut')))    
print(textify(decode(3, 5, '0865626283446562')))

run = True
while run:
    which_func = input('encode or decode: ')
    
    if which_func == 'encode':
        message = input('what is your message: ')
        m = int(input('what is your m scrambler: '))
        b = int(input('what is your b scrambler: '))
        print('here is your encoded message: ',encode(m,b,numbify(message)))
    elif which_func == 'decode':
        mb_nums = input('give me the message number: ')
        m = int(input('what is your m scrambler: '))
        b = int(input('what is your b scrambler: '))
        print('here is your decoded message: ',textify(decode(m,b,mb_nums)))
    elif which_func == 'end':
        run = False
    else:
        print('failed input')
    