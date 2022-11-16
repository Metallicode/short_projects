from PIL import Image
import os, sys

path = os.getcwd()
dirs = os.listdir(path)

def resize_aspect_fit(percentage_size=50):
	for item in dirs:
		if item == '.DS_Store' or item == 'resize_images.py':
			continue
		elif os.path.isfile(path+'/'+item):
			im = Image.open(path+'/'+item)
			f, e = os.path.splitext(path+'/'+item)
			size = im.size
			ratio = float(final_size) / max(size)
			new_image_size = tuple([int(x*ratio) for x in size])
			im = im.resize(new_image_size, Image.ANTIALIAS)
			new_im = Image.new("RGB", (new_image_size[0], new_image_size[1]))
			new_im.paste(im)
			new_im.save(f + 'resized.jpg', 'JPEG', quality=90)
             
             
resize_aspect_fit(int(input("Enter percentage size of new images (i.e 35):\n")))
