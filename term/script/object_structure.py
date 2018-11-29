from pico2d import *

import math
import  random
import loading_state as lo

class structure:
    def __init__(self,sX,sY,sW,sH,sImgN,sColType,sR):
        self.x,self.y = sX,sY
        self.w,self.h = sW,sH
        self.imageNum = sImgN
        self.collision = None
        self.colType = sColType
        self.crush = False
        self.r = sR