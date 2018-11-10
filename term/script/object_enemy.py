from pico2d import *

import math

MOVE_TIME = 1/60




class enemy:
    enemy_class = ["bagic_enemy"]
    ENEMY_IMAGE = {
        'bagic_enemy': load_image('../res/object/enemy/bagic_enemy.png')
        #아니면 초기화를 시켜줄때 넣는 방법도 있다. 다른곳에서 로딩하고
    }
    def __init__(self,sName,sX,sY,sRad,sRs,sFs,sAi):
        self.name = sName
        self.x, self.y = sX,sY
        self.rad = sRad
        self.rotForce = sRs*MOVE_TIME * math.pi/60
        self.fwForce = sFs*MOVE_TIME
        self.ai = sAi

    def draw(self):
        self.image.composite
    def update(self):
        pass
    def handle_event(self):
        pass