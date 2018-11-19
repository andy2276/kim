from pico2d import *
import math

MOVE_TIME = 1/60

#-------Tank Body---------
class Body:
    KeyEvent = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]
    image = None
    def __init__(self,px,py,prad,prs,pfs,pbs):
        self.x ,self.y =px,py

        self.rotSpeed= prs/10 * math.pi/60
        self.fwSpeed = pfs*MOVE_TIME*2
        self.bkSpeed = pbs*MOVE_TIME
        #print(self.fwSpeed,self.bkSpeed)
        self.rad = prad
        self.key = {}
        for k in Body.KeyEvent :
            self.key[k] = False
        if Body.image ==None : Body.image = load_image("../res/object/character/player_body_pix2.png")

    def draw(self):
        self.image.composite_draw(self.rad, "" , self.x, self.y)


    def update(self):
        rot = 1 if self.key[SDLK_a] else 0
        rot += -1 if self.key[SDLK_d] else 0
        mov = 1 if self.key[SDLK_w] else 0
        mov += -1 if self.key[SDLK_s] else 0
        if rot != 0:
            if mov < 0:
                rot = -rot
            self.rad += rot*self.rotSpeed
        #rot and mov not over 1 or -1
        if mov !=0:
            mv = None
            if self.key[SDLK_w]:
                mv = self.fwSpeed
            elif self.key[SDLK_s]:
                mv = self.bkSpeed

            self.x += mov * mv * math.cos(self.rad)
            self.y += mov * mv * math.sin(self.rad)


        return self.x, self.y

    def handle_event(self,keys):
        if keys.type == SDL_KEYDOWN or keys.type == SDL_KEYUP:
            if keys.key in Body.KeyEvent:
                self.key[keys.key] = keys.type == SDL_KEYDOWN

#-------Tank Barrel---------
class Barrel:
    image = None
    def __init__(self,px,py,prs):
        self.x,self.y = px,py

        self.tx,self.ty = 0,0

        self.mx,self.my = 0, 0
        self.rad = 0.0
        self.rotSpeed = prs/10 * math.pi/60
        if Barrel.image == None: Barrel.image = load_image('../res/object/character/player_barrel_pix2.png')

    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
        self.rad = math.atan2(self.y - self.my,self.x - self.mx)
        #self.collision.draw()

    def update(self, px, py):

        #print(self.rad)
        self.x , self.y = px, py


    def handle_event(self,keys):
        if keys.type == SDL_MOUSEMOTION:
            #print(keys.x,600- keys.y)
            self.mx, self.my = keys.x, 600 - keys.y
            #print(self.mx, self.my)

#-------Tank Body+Barrel---------
class Player:
    def __init__(self, sName, sX, sY, sHp, sRad, sPrs, sPfs, sPbs,w,h):
        self.id = sName
        self.play = 'player'
        self.x, self.y = sX, sY

        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2

        self.hp = sHp
        self.rad = math.pi/(180/sRad)
        self.rotSpeed = sPrs
        self.bodyFwSpeed = sPfs
        self.bodyBkSpeed = sPbs

        self.body = Body(self.x,self.y,self.rad,self.rotSpeed,self.bodyFwSpeed,self.bodyBkSpeed)
        self.barrel = Barrel(self.x,self.y,self.rotSpeed)

        self.collision = None
        self.colType = 'box'
        self.w, self.h = w, h


        #self.collision = co.collider(self.x,self.y,"box",16,16)  # 함수만들거임

    def draw(self):
        self.body.draw()
        self.barrel.draw()
        #if self.collision != None:
         #   self.collision.draw()
    def update(self):

        self.x, self.y = self.body.update()
        self.barrel.update(self.x, self.y)
        print("player ",self.x)
        if self.collision != None:
            self.collision.update()

    def handle_event(self,keys):
        self.body.handle_event(keys)
        self.barrel.handle_event(keys)

