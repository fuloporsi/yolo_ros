from os import listdir
from os.path import isfile, join
from PIL import Image
import os
import struct

def convert(size, box):
	dw = 1./size[0]
	dh = 1./size[1]
	x = (box[0] + box[1])/2.0
	y = (box[2] + box[3])/2.0
	w = box[1] - box[0]
	h = box[3] - box[2]
	x = x*dw
	w = w*dw
	y = y*dh
	h = h*dh
	return (x,y,w,h)	


currentPath = os.getcwd()

i=0
categoryNumber=0
found = False
for root, dirs, files in os.walk(currentPath): 
	for file in files:
		if file.endswith('_crop.png'):
			found=True
			file = os.path.abspath(os.path.join(root,file))
			im = Image.open(file)
			width, height = im.size
			print "Found: "+str(i)+" dim: "+str(width)+" X "+str(height)
			b = (float(0), float(width), float(0), float(height))
			bb=convert((width,height), b)

			f=open(file.split(".")[0] +".txt","w")
			#print file.split(".")[0] 
			#f.write(str(0) + "\n")
			#f.write("0 0 ")
			#f.write(str(width)+" "+str(height))

			#f.write(str(bb))
			f.write(str(categoryNumber) + " " + " ".join([str(a) for a in bb]) + '\n')
			f.close()
			i+=1
			
			
if not found:
	print "No image found!"	





