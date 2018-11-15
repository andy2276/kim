from pico2d import *

import math
import random
import loading_state

MOVE_TIME = 1/60

class enemy:
    _class = ["bagic_enemy"]
    _RANGE = {
        'bagic_enemy':{"search":150,"attack":30}
    }
    _STATE = {'stay','recon','found','move','attack'}
    _COUNT = 1
    def __init__(self,sName,sX,sY,sRad,sRs,sFs,sAi,w,h):
        self.name = sName
        self.play = 'enemy'
        self.x, self.y = sX,sY

        self.tx,self.ty = 0,0

        self.collision = None
        self.colType = 'box'
        self.w,self.h = w,h

        self.count = enemy._COUNT
        enemy._COUNT += 1#id & count

        self.rad = sRad
        self.rotForce = sRs*MOVE_TIME * math.pi/60
        self.fwForce = sFs*MOVE_TIME
        self.ai = sAi


        self.state = 'stay'
        self.found = False
        self.dist = 0

        self.searchR = enemy._RANGE[self.name]["search"]
        self.attackR = enemy._RANGE[self.name]["attack"]

        if self.name in enemy._class:
            self.image = loading_state.loadingImage().object_enemy_image[self.name]
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
    def update(self):
        if self.state == 'stay':
            enemy.stay(self)
        elif self.state == 'recon':
            enemy.reconnaissance(self)
        elif self.state == 'found':
            enemy.foundyou(self)


    def handle_event(self):
        pass

    def stay(self):
        self.tx = math.fabs(self.x + random.randint(-50,50))
        self.ty =  math.fabs(self.y + random.randint(-50,50))
        print("test",self.x,self.y,self.tx,self.ty)
        self.state = 'recon'
    def reconnaissance(self):
        #if 0.1<=math.sqrt((self.tx-self.x)**2+(self.ty - self.y)**2)<=1:
         #   print("ok")
          #  self.state = 'stay'
           # return


        if -1<=self.x - self.tx<=1:#근사치
            self.state = 'stay'
            return
        if self.found :
            print('found you!')
            self.state = 'found'
            return


        enemy.move(self)

    def foundyou(self):
        enemy.move(self)
        if self.found == False:
            self.state = 'stay'
            return



    def move(self):
        self.rad = math.atan2(self.ty - self.y, self.tx - self.x)
        self.x += math.cos(self.rad) * self.fwForce
        self.y += math.sin(self.rad) * self.fwForce








