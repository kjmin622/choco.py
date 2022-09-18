import os
from constant import *

class Side:
    def __init__(self,objectlist,image,path = None):
        self.objectlist = objectlist
        self.imagepath = os.path.join(DIR_IMAGE,image)
        self.path = path