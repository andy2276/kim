from pico2d import *

import math

#------------draw collision box?
drawCollider = True



class collider:
    def __init__(self, xo, yo, coltype, widtho, higho):
        self.x, self.y = xo, yo
        self.w, self.h = widtho, higho
        self.type = coltype
        if self.type == "box":
            collider.box(self, self.w, self.h)
        elif self.type == "circle":
            collider.circle(self, self.w) if self.w == self.h else print("nope!!!")
        else:
            self.type = 'controler'
            print("controler")

    def box(self, w, h):
        self.bb = {"LD": [self.x - w / 2, self.y - h / 2], "RU": [self.x + w / 2, self.y + h / 2]}
    def circle(self, r):
        self.bb = {"SP": [self.x, self.y], "HD": [r / 2]}

    def update(self):
        pass
#충돌체는 나중에 하고 지금은 인공지능이나 만들자.
class Collision:
    _precision = {"high":0,"middle":1,"low":2}
    def __init__(self,object):
        self.type = object.colType
        self.x,self.y = object.x,object.y
        self.w,self.h = object.w, object.h
        self.target = object

        self.crush = False
        self.him = None
        if self.type == 'box':
            self.ldx,self.ldy = 0,0
            self.rux,self.ruy =0,0
            self.rad = object.rad
            Collision.boxCollision(self,True)
        elif self.type == 'circle':
            self.r = self.w/2
    def draw(self):
        if drawCollider :
            if self.type == 'box':
                draw_rectangle(*Collision.boxCollision(self,False))
            elif self.type == 'circle':
                pass


    def update(self):
        self.x, self.y = self.target.x, self.target.y
        self.rad = self.target.rad
        if self.type == 'box':
            self.ldx +=math.cos(self.rad)
            self.ldy +=math.sin(self.rad)
            self.rux +=math.cos(self.rad)
            self.ruy +=math.sin(self.rad)


    def handle_event(self):
        pass
    def boxCollision(self,option):
        if option:
            self.ldx, self.ldy = self.x - self.w / 2 - Collision._precision["high"],\
                                 self.y - self.h / 2 - Collision._precision["high"]
            self.rux, self.ruy = self.x + self.w / 2 - Collision._precision["high"],\
                                 self.y + self.h / 2 - Collision._precision["high"]
        else:
            return self.ldx,self.ldy,self.rux,self.ruy

    def isCollision(self,other):
        #아더와 본인의 타겟을 계속 비교한다. 리턴을 빠르게 하면 속도에서 이득을 볼수있을것이다.
        if self.target.colType == 'box':
            if self.rux < other.collision.ldx :
                self.crush = False
                self.him = None
                return False
            if self.ruy < other.collision.ldy :
                self.crush = False
                self.him = None
                return False
            if self.ldx > other.collision.rux :
                self.crush = False
                self.him = None
                return False
            if self.ldy > other.collision.ruy :
                self.crush = False
                self.him = None
                return False

            self.crush  = True
            self.him = other

            return True
        if self.target.colType == 'circle':
            pass

    def whoCollideMe(self):
        if self.crush :
            return self.him
        return






