from PIL import Image

#Read image
im = Image.open('C:\\Users\\Lrhgr\\Desktop\\hobbies\\programing\\image stuff\\image.jpg')

#Display image  
#im.show()

#get size
width, height = im.size

#get pixel data
pixel_map = im.load()

print(pixel_map[0, 0])