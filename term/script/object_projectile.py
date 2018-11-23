from pico2d import *
import math

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
        pass
    def update(self):
        pass
    def handle_event(self):
        pass

class missile(projectile):
    def __init__(self,sX,sY,sRad,sPlay,sFs,sVr,sCt):
        self.name = 'missile'
        self.x,self.y = sX,sY
        self.rad = sRad
        self.paly = sPlay
        self.fwSpeed = sFs
        self.visualR = sVr
        self.coltype = sCt

