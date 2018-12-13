from pico2d import *
import math
import loading_state as lo



# global TESTINGGAME,MOVE_TIME,BARREL_GUNPORT


TESTINGGAME= False
MOVE_TIME = 0

BARREL_GUNPORT = 106



#-------Tank Body---------
class Body:
    KeyEvent = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]
    image = None
    def __init__(self,px,py,prad,prs,pfs,pbs):
        self.x ,self.y =px,py

        self.canGo = 1
        self.rotSpeed= prs/10 * math.pi/60
        self.fwSpeed = pfs
        self.bkSpeed = pbs
        #print(self.fwSpeed,self.bkSpeed)
        self.rad = prad
        self.key = {}

        self.moved = False
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
            self.moved = True
            mv = None
            if self.key[SDLK_w]:
                mv = self.fwSpeed*MOVE_TIME* self.canGo
            elif self.key[SDLK_s]:
                mv = self.bkSpeed*MOVE_TIME* self.canGo

            self.x += mov * mv * math.cos(self.rad)
            self.y += mov * mv * math.sin(self.rad)
        else:
            self.moved = False
        return self.x, self.y

    def handle_event(self,keys):
        if keys.type == SDL_KEYDOWN or keys.type == SDL_KEYUP:
            if keys.key in Body.KeyEvent:
                self.key[keys.key] = keys.type == SDL_KEYDOWN

#-------Tank Barrel---------
class Barrel:
    image = None
    def __init__(self,px,py,prs,wC):
        self.x,self.y = px,py
        self.gpx,self.gpy = 0 ,0

        self.tx,self.ty = 0,0
        self.attack = False

        self.mx,self.my = 0, 0
        self.rad = 0.0
        self.rotSpeed = prs/10 * math.pi/60

        self.reload = True
        self.reloading = False
        self.weapon = 0
        self.wpCount = wC
        if Barrel.image == None:
            Barrel.image =  lo.loadImages.object_player_image["player_barrel"]
            if TESTINGGAME:
                self.colAim = load_image('po.png')



         #   self.im2 = self.im
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
        if TESTINGGAME:
            self.colAim.draw(self.gpx,self.gpy)
        #self.im2.draw(374,369)


        #self.collision.draw()

    def update(self, px, py):
        self.rad = math.atan2(self.y - self.my, self.x - self.mx)
        #print("player",MOVE_TIME)
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
            if self.wpCount == 0:
                lo.loadSound.playerSound["reload_reload"].set_volume(5)
                lo.loadSound.playerSound["reload_reload"].play(1)
            else:
                self.attack = True

        if keys.type == SDL_MOUSEBUTTONDOWN and keys.button == SDL_BUTTON_RIGHT:
            print("reloading!!")
            self.reloading = True



        if (keys.type,keys.key)  == (SDL_KEYDOWN,SDLK_q):
            self.weapon = ((self.weapon+1)%self.wpCount)
            print(self.weapon,"press q")

        if (keys.type,keys.key)  == (SDL_KEYDOWN,SDLK_e):
            self.weapon = ((self.weapon - 1) % self.wpCount)
            print(self.weapon,"press e")
        #print("weapon",self.weapon)

            #print(self.tx,self.ty,self.rad)



#-------Tank Body+Barrel---------
class Player:
    colBox = None
    def __init__(self,sSelect ,sName, sX, sY, sHp, sRad, sPrs, sPfs, sPbs,w,h,wC,aCool):
        self.select = sSelect
        self.name = sName
        self.play = 'player'
        self.x, self.y = sX, sY
        self.visualR = h / 2

        #--------------------------------
        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2

        self.wp = lo.loadState.weaponCount[self.select]
        print("player init ",self.wp)

        self.hp = sHp
        self.rad = math.pi/(180/sRad)
        self.rotSpeed = sPrs
        self.bodyFwSpeed = sPfs
        self.bodyBkSpeed = sPbs

        self.weaponCount = wC
        self.attackCool = aCool

        self.body = Body(self.x,self.y,self.rad,self.rotSpeed,self.bodyFwSpeed,self.bodyBkSpeed)
        self.barrel = Barrel(self.x,self.y,self.rotSpeed,self.weaponCount)

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
        if self.barrel.attack:
            Player.countWeapon(self)

    def handle_event(self,keys):

        self.body.handle_event(keys)
        self.barrel.handle_event(keys)
    def countWeapon(self):
        self.wp[self.barrel.weapon] -=1
        if self.wp[self.barrel.weapon] <=0:
            self.barrel.reload = False
        if self.barrel.reloading:
            self.barrel.reloading = False
            self.wp[self.barrel.weapon] = lo.loadState.weaponCount[self.select][self.barrel.weapon]
            print("reloading!!!!!!!!!!!!!!!!!!!!!!!!",lo.loadState.weaponCount[self.select][self.barrel.weapon])
            print("in barrel: ",self.wp[self.barrel.weapon])
            print("self.wp",self.wp)
            self.barrel.reload = True



