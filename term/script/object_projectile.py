from pico2d import *
import math

MOVE_TIME = 1/60

class projectile:
    def __init__(self):
        self.name = 'superClass'
        self.x,self.y =0,0
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
    def __init__(self,sX,sY):
        self.name = 'missile'
        self.x
