from pico2d import *

import math
import random
import object_player as Player
import loading_state

MOVE_TIME = 1/60

player = Player.Player





class enemy:
    enemy_class = ["bagic_enemy"]
    ENEMY_RANGE = {
        'bagic_enemy':{"search":50,"attack":30}
    }
    ENEMY_STATE = {'stay','recon','found','move','attack'}
    def __init__(self,sName,sX,sY,sRad,sRs,sFs,sAi):
        self.name = sName
        self.x, self.y = sX,
        self.play = 'enemy'
        self.tx,self.ty = 0,0
        self.rad = sRad
        self.rotForce = sRs*MOVE_TIME * math.pi/60
        self.fwForce = sFs*MOVE_TIME
        self.ai = sAi




        self.state = 'stay'
        self.searchR = enemy.ENEMY_RANGE[self.name]["search"]
        self.attackR = enemy.ENEMY_RANGE[self.name]["attack"]
        if self.name in enemy.enemy_class:
            self.image = loading_state.loadingImage().object_enemy_image[self.name]
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
    def update(self):
        if self.state == 'stay':
            enemy.stay(self)
        elif self.state == 'recon':
            enemy.move(self)

    def handle_event(self):
        pass

    def stay(self):
        self.tx = math.fabs(self.x + random.randint(-50,50))
        self.ty =  math.fabs(self.y + random.randint(-50,50))
        print("test",self.x,self.y,self.tx,self.ty)
        self.state = 'recon'
    def move(self):
        #if 0.1<=math.sqrt((self.tx-self.x)**2+(self.ty - self.y)**2)<=1:
         #   print("ok")
          #  self.state = 'stay'
           # return
        if -1<=self.x - self.tx<=1:#근사치
            print("ok")
            self.state = 'stay'
            return
        self.rad = math.atan2(self.ty-self.y,self.tx-self.x)
        #print(math.degrees(self.rad))
        self.x += math.cos(self.rad)*self.fwForce
        self.y += math.sin(self.rad)*self.fwForce






