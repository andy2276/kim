from pico2d import *
import math
import loading_state as lo

MOVE_TIME = 1/60

class projectile:
    def __init__(self):
        self.name = 'superClass'
        self.x,self.y =0,0
        self.rad = 0.0
        self.paly = 'enemy'
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
        print(self.x,self.y)
        if self.crush :
            print("boom!!")

    def handle_event(self):
        pass

class missile(projectile):
    def __init__(self,sN,sX,sY,sRad,sPlay,sFs,sVr,sCt,sW,sH):
        self.name = sN
        self.x,self.y = sX,sY
        self.rad = sRad
        self.paly = sPlay
        self.fwSpeed = sFs
        self.visualR = sVr
        self.collision = None
        self.coltype = sCt
        self.w,self.h = sW,sH
        self.crush = False


test = 30
a = missile('missile_bagic',0,0,test*math.pi/180,'player',10,10,'circle',20,20)
for i in range(60):
    a.update()

print(math.degrees(test*math.pi/180))
