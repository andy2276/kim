from pico2d import *

import math
import  random
import loading_state as lo

TESTINGGAME = True

class structure:
    def __init__(self,sN,sL,sB,sX,sY,sW,sH,sP,sColType,sR):
        self.name = sN
        self.x,self.y = sX,sY
        self.w,self.h = sW,sH
        self.rad = 0
        self.play = sP
        self.left = sL
        self.bottom = sB
        self.collision = None
        self.colType = sColType
        self.crush = False
        self.r = sR
        self.visualR = self.r

    def draw(self):
        lo.loadBlocks.clip_draw(self.left,self.bottom,self.w,self.h,self.x,self.y)

    def update(self):
        pass
    def handle_event(self):
        pass

class Box(structure):
    def __init__(self,sN,sL,sB,sX,sY,sW,sH,sP,sColType,sR):
        self.name = sN
        self.x, self.y = sX, sY
        self.w, self.h = sW, sH
        self.rad = 0
        self.play = sP
        self.play = sP
        self.left = sL
        self.bottom = sB
        self.collision = None
        self.colType = sColType
        self.crush = False
        self.r = sR
        self.visualR = self.r
