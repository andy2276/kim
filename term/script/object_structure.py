from pico2d import *

import math
import  random
import loading_state as lo

TESTINGGAME = True

class structure:
    def __init__(self,sN,sX,sY,sW,sH,sP,sImgN,sColType,sR):
        self.name = sN
        self.x,self.y = sX,sY
        self.w,self.h = sW,sH
        self.rad = 0
        self.play = sP
        self.imageNumX = sImgN%10
        self.imageNumY = sImgN//10
        self.collision = None
        self.colType = sColType
        self.crush = False
        self.r = sR
        self.visualR = self.r

    def draw(self):
        lo.loadBlocks[self.imageNumY][self.imageNumX].draw(self.x,self.y)

    def update(self):
        pass
    def handle_event(self):
        pass

class Box(structure):
    def __init__(self,sN,sX,sY,sW,sH,sP,sImgN,sColType,sR):
        self.name = sN
        self.x, self.y = sX, sY
        self.w, self.h = sW, sH
        self.rad = 0
        self.play = sP
        if sImgN == 0:
            self.imageNumX = 0
            self.imageNumY = 0
        else:
            self.imageNumX = sImgN % 15
            self.imageNumY = sImgN // 15


        self.collision = None
        self.colType = sColType
        self.crush = False
        self.r = sR
        self.visualR = self.r
