'''
with open('readme.txt', 'w') as f:
    #f.write('readme')
    f.writelines('john said not to tell\n')
    f.close()

    #tabstxt = f.readlines()
'''
tabstxt = open('c:\\Users\\Lrhgr\\Documents\\GitHub\\Python_projects\\guitar\\tabs.txt','a')

tabstxt.writelines('694209000')[0]

print(tabstxt.readlines())

tabstxt.close()