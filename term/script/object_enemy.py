from pico2d import *

import math
import random


MOVE_TIME = 1/60
MOVE_FREEZE = 1



class enemy:
    _class = ["bagic_enemy"]
    _RANGE = {
        'bagic_enemy':{"search":300,"attack":150,"safe":120}
    }
    _STATE = {'stay','recon','found','move','attack'}
    _COUNT = 1

    def __init__(self,sName,sX,sY,sRad,sRs,sFs,sAi,w,h):
        self.name = sName
        self.play = 'enemy'
        self.x, self.y = sX,sY
        self.visualR = w / 2

        self.tx,self.ty = 0,0

        # this place is Collider
        self.collision = None
        self.colType = 'box'
        self.w,self.h = w,h
        self.crush = False

        self.count = enemy._COUNT
        enemy._COUNT += 1#id & count

        self.rad = sRad
        self.rotForce = sRs*MOVE_TIME * math.pi/60
        self.fwForce = sFs*MOVE_TIME * MOVE_FREEZE
        self.ai = sAi


        self.state = 'stay'
        self.found = False
        self.attack = False

        self.dist = 0

        self.searchR = enemy._RANGE[self.name]["search"]#반지름임
        self.attackR = enemy._RANGE[self.name]["attack"]
        self.safeR = enemy._RANGE[self.name]["safe"]

        if self.name in enemy._class:
            self.image = loadImages.object_enemy_image[self.name]
            self.colBox = loadImages.object_enemy_colBox_image[self.name]
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
        if self.collision != None:
            self.collision.draw()

        #self.collision.draw()
    def update(self):

        if self.state == 'stay':
            enemy.stay(self)
        elif self.state == 'recon':
            enemy.reconnaissance(self)
        elif self.state == 'found':
            enemy.foundyou(self)
        elif self.state == 'attack':
            enemy.attack(self)
        if self.collision != None:
            self.collision.update()

    def handle_event(self):
        pass

    def stay(self):
        self.tx = math.fabs(self.x + random.randint(-50,50))
        self.ty =  math.fabs(self.y + random.randint(-50,50))
        #print("test",self.x,self.y,self.tx,self.ty)
        self.state = 'recon'
    def reconnaissance(self):
        #if 0.1<=math.sqrt((self.tx-self.x)**2+(self.ty - self.y)**2)<=1:
         #   print("ok")
          #  self.state = 'stay'
           # return


        if -2<=self.x - self.tx<=2:#근사치
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
        if self.dist<=self.attackR:
            self.state = 'attack'
            #print("attack", self.dist)
            self.attack = True
            return

    def move(self):
        self.rad = math.atan2(self.ty - self.y, self.tx - self.x)
        self.x += math.cos(self.rad) * self.fwForce
        self.y += math.sin(self.rad) * self.fwForce

    def attack(self):
        if self.attackR >= self.dist:
            #print("coWha!!")
            if self.safeR >= self.dist:
                self.rad = math.atan2(self.ty - self.y, self.tx - self.x)
                self.x -= math.cos(self.rad) * self.fwForce
                self.y -= math.sin(self.rad) * self.fwForce

        return







