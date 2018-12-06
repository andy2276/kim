from pico2d import *
import math
import loading_state as lo


# global MOVE_TIME,TESTINGGAME
global MOVE_TIME

MOVE_TIME = 1/60

TESTINGGAME = False

class projectile:
    def __init__(self):
        self.name = 'superClass'
        self.x,self.y =0,0
        self.rad = 0.0
        self.play = 'enemy'
        self.fwSpeed = 0.0
        self.visualR = 0
        self.collision = None
        self.colBox = None
        self.coltype = 'circle'
        self.w,self.h = 0,0
        self.crush = False

        self.image = None

    def draw(self):
        if self.play == "player":
            self.image.composite_draw(self.rad,"",self.x,self.y)
        else:
            self.image.composite_draw(self.rad + math.pi, "", self.x, self.y)
        #print(self.x,self.y)


    def update(self):
        dist = MOVE_TIME*self.fwSpeed
        if self.play == "player":
            self.x += math.cos(self.rad)*dist*-1
            self.y += math.sin(self.rad)*dist*-1
        else:
            self.x += math.cos(self.rad) * dist
            self.y += math.sin(self.rad) * dist
        #print(self.x,self.y,self.rad)


    def handle_event(self):
        pass

class missile(projectile):

    def __init__(self,sN = 'noname',sX = 0,sY = 0,sRad = math.pi/180,sPlay = 'no',sFs = 0,sVr= 0,sCt = 'circle',sW = 0,sH = 0):
        global TESTINGGAME
        self.name = sN
        self.x,self.y = sX,sY
        self.rad = sRad
        self.play = sPlay
        self.fwSpeed = sFs
        self.visualR = sVr

        self.collision = None
        self.colType = sCt
        if TESTINGGAME:
            self.colBox = lo.loadImages.object_enemy_colBox_image['bagic_enemy']
        self.w,self.h = sW,sH
        self.r = self.w/2
        self.crush = False
        self.image = lo.loadImages.object_projectile_image['missile']

class cannonball(projectile):
    def __init__(self,sN = 'noname',sX = 0,sY = 0,sRad = math.pi/180,sPlay = 'no',sFs = 0,sVr= 0,sCt = 'circle',sW = 0,sH = 0):
        self.name = sN
        self.x,self.y = sX,sY
        self.rad = sRad
        self.play = sPlay
        self.fwSpeed = sFs
        self.visualR = sVr

        self.collision = None
        self.colType = sCt
        if TESTINGGAME:
            self.colBox = lo.loadImages.object_enemy_colBox_image['bagic_enemy']
        self.w,self.h = sW,sH
        self.r = self.w/2
        self.crush = False
        self.image = lo.loadImages.object_projectile_image['cannonball']





