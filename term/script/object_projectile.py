from pico2d import *
import math
import loading_state as lo

MOVE_TIME = 1/60

class projectile:
    def __init__(self):
        self.name = 'superClass'
        self.x,self.y =0,0
        self.rad = 0.0
        self.play = 'enemy'
        self.fwSpeed = 0.0
        self.visualR = 0
        self.collision = None
        self.coltype = 'circle'
        self.w,self.h = 0,0
        self.crush = False

    def draw(self):
       lo.loadImages.object_projectile_image[self.name].draw(self.x,self.y)
    def update(self):
        dist = MOVE_TIME*self.fwSpeed
        self.x += math.cos(self.rad)*dist
        self.y += math.sin(self.rad)*dist
        print(self.x,self.y,self.rad)
        if self.crush :
            print("boom!!")

    def handle_event(self):
        pass

class missile(projectile):
    def __init__(self,sN = 'noname',sX = 0,sY = 0,sRad = math.pi/180,sPlay = 'no',sFs = 0,
                 sVr= 0,sCt = 'box',sW = 0,sH = 0):
        self.name = sN
        self.x,self.y = sX,sY
        self.rad = sRad
        self.play = sPlay
        self.fwSpeed = sFs
        self.visualR = sVr
        self.collision = None
        self.coltype = sCt
        self.w,self.h = sW,sH
        self.crush = False




