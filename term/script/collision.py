from pico2d import *

import math

#------------draw collision box?
drawCollider = False


def isSearchRange(player, enemy,want):
    #return true, UnI - enemy.searchR return false only false
    UnI = math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)
    if UnI - enemy.searchR <= 0:
        if want == 1:
            return player.x,player.y,enemy.searchR - UnI
        return True
    else:
        return False
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

class Collision:
    _precision = {"high":0,"middle":1,"low":2}
    def __init__(self,object):
        self.type = object.colType
        self.x,self.y = object.x,object.y
        self.w,self.h = object.w, object.h
        self.target = object
        if self.type == 'box':
            self.rdx,self.rdy = 0
            self.lux,self.luy =0
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
        pass


    def handle_event(self):
        pass
    def boxCollision(self,option):
        if option:
            self.rdx, self.rdy = self.x - self.w / 2 - Collision._precision["high"],\
                                 self.y - self.h / 2 - Collision._precision["high"]
            self.lux, self.luy = self.x + self.w / 2 - Collision._precision["high"],\
                                 self.y + self.h / 2 - Collision._precision["high"]
        else:
            return self.x - self.w / 2 - Collision._precision["high"],\
                   self.y - self.h / 2 - Collision._precision["high"],\
                   self.x + self.w / 2 - Collision._precision["high"],\
                   self.y + self.h / 2 - Collision._precision["high"]

    def isCollision(self,other):
        #아더와 본인의 타겟을 계속 비교한다. 리턴을 빠르게 하면 속도에서 이득을 볼수있을것이다.
        pass




a = cllider(10, 10, "box", 2, 3)
b = collider(20, 30, "circle", 2, 2)

print(a.bb)