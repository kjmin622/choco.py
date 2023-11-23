import os
from PIL import Image
import numpy as np

DIR_PATH = os.path.dirname(__file__)
DIR_SAVE = os.path.join(os.path.dirname(os.path.abspath(DIR_PATH)),"data")

def equal(a,b):
    return a[0]==b[0] and a[1]==b[1] and a[2]==b[2]

img = Image.open("farthingmap.png")
imgarr = np.array(img, dtype = "uint8")

file = open(os.path.join(DIR_SAVE,"mapdata.py"),"w")
file.write(str(len(imgarr))+","+str(len(imgarr[0]))+"\n")

file.write("MAPLIST = {")
for i in range(len(imgarr)) :
    if(i%100==0):
        print(len(imgarr[0]),i)

    for j in range(len(imgarr[i])):
        color = imgarr[i][j]
        if(equal(color,[0,0,0])):
            file.write(f"'{j},{i}':1,")
        if(equal(color,[255,0,0])):
            file.write(f"'{j},{i}':-1,")
        if(equal(color,[0,0,255])):
            file.write(f"'{j},{i}':-2,")
file.write("}")
        

file.close()