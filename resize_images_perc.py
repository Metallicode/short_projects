from PIL import Image
import os, sys

path = os.getcwd()
dirs = os.listdir(path)

def resize_by_percentage(percentage_size=50):
	for item in dirs:
		print(item, __file__)
		if item == '.DS_Store' or item == __file__:
			continue
		elif os.path.isfile(path+'/'+item):
			im = Image.open(path+'/'+item)
			f, e = os.path.splitext(path+'/'+item)
			new_image_size = ((im.size[0]//100)*percentage_size, (im.size[1]//100)*percentage_size)
			im = im.resize(new_image_size, Image.ANTIALIAS)
			new_im = Image.new("RGB", (new_image_size[0], new_image_size[1]))
			new_im.paste(im)
			new_im.save(f + 'resized.jpg', 'JPEG', quality=90)
             
             
resize_by_percentage(int(input("Enter percentage size of new images (i.e 35):\n")))
