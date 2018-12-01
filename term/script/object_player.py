from pico2d import *
import math
import loading_state as lo

MOVE_TIME = 0
BARREL_GUNPORT = 106


#-------Tank Body---------
class Body:
    KeyEvent = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]
    image = None
    def __init__(self,px,py,prad,prs,pfs,pbs):
        self.x ,self.y =px,py

        self.rotSpeed= prs/10 * math.pi/60
        self.fwSpeed = pfs*MOVE_TIME
        self.bkSpeed = pbs*MOVE_TIME
        #print(self.fwSpeed,self.bkSpeed)
        self.rad = prad
        self.key = {}
        for k in Body.KeyEvent :
            self.key[k] = False
        if Body.image ==None :
            Body.image = lo.loadImages.object_player_image["player_body"]

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
        self.gpx,self.gpy = 0 ,0

        self.tx,self.ty = 0,0
        self.attack = False

        self.mx,self.my = 0, 0
        self.rad = 0.0
        self.rotSpeed = prs/10 * math.pi/60

        if Barrel.image == None:
            Barrel.image =  lo.loadImages.object_player_image["player_barrel"]
            self.colAim = load_image('../res/object/character/po.png')


         #   self.im2 = self.im
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
        self.colAim.draw(self.gpx,self.gpy)
        #self.im2.draw(374,369)


        #self.collision.draw()

    def update(self, px, py):
        self.rad = math.atan2(self.y - self.my, self.x - self.mx)

        dx = BARREL_GUNPORT*math.cos(self.rad) - math.sin(self.rad)
        dy = BARREL_GUNPORT*math.sin(self.rad) + math.cos(self.rad)

        self.gpx = self.x + dx*-1
        self.gpy = self.y + dy*-1

        self.x , self.y = px, py

        #print(self.tx,self.ty)




    def handle_event(self,keys):
        if keys.type == SDL_MOUSEMOTION:
            self.mx, self.my = keys.x, lo.C_HIEGHT - keys.y
        if keys.type == SDL_MOUSEBUTTONDOWN and keys.button == SDL_BUTTON_LEFT:
            self.tx,self.ty =  keys.x, lo.C_HIEGHT - keys.y
            self.attack = True
            #print(self.tx,self.ty,self.rad)



#-------Tank Body+Barrel---------
class Player:
    colBox = None
    def __init__(self, sName, sX, sY, sHp, sRad, sPrs, sPfs, sPbs,w,h):
        self.name = sName
        self.play = 'player'
        self.x, self.y = sX, sY
        self.visualR = h / 2

        #--------------------------------
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
        self.crush = False
        if Player.colBox == None:
            self.colBox =  lo.loadImages.object_player_colBox_image['player_colBox']

        #self.collision = co.collider(self.x,self.y,"box",16,16)  # 함수만들거임

    def draw(self):
        self.body.draw()
        self.barrel.draw()
        if self.collision != None:
            self.collision.draw()
    def update(self):

        self.x, self.y = self.body.update()
        self.rad = self.body.rad
        self.barrel.update(self.x, self.y)
        #print("player ",self.x)
        if self.collision != None:
            self.collision.update()

    def handle_event(self,keys):
        self.body.handle_event(keys)
        self.barrel.handle_event(keys)

