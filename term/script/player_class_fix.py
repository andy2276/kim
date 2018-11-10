
#//-----------------/This module's name is 'player_class_fix'/------------------//
#//-----------------/prev module is 'None'/-------------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//


#first import pico2d
from pico2d import *
#second import game_framework - keyword 'as' is only use game_framework
import game_framework as gf
#third import next module

#fourth import need module
import math
#fifth initializing module variables(for using to any modul)

#sixth initializing global variables(for only using this module)
GSIV = {"startX": 2, "startY": 2, "startAngle": math.pi/2}#trans jason and test


#seventh define class
class Body:
    #keysType = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]
    keysType = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]#97,100,119,115

    def __init__(self):
        self.image = load_image("../res/object/character/player_body_pix2.png")

        #self.x, self.y = get_canvas_width()/ GSIV["startX"] , get_canvas_height()/GSIV["startY"]
        self.x, self.y = 400, 400
        self.rad = GSIV["startAngle"]
        self.rotSpeed = 0.1 * math.pi/60
        self.moveSpeed = 10 * 1/60
        self.backSpeed = 10 * 1/60
        self.key = {}
        for k in Body.keysType:
            #print(k)
            self.key[k] = False  #type init
            #print(self.key[k])
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
        #self.image.draw(self.x,self.y)

    def update(self):
        rot = 1 if self.key[SDLK_a] else 0 # mag is 1. if self.key is True. else if 0
        rot += -1 if self.key[SDLK_d] else 0
        mov = 1 if self.key[SDLK_w] else 0
        mov += -1 if self.key[SDLK_s] else 0
        #print(self.rad)
        if rot != 0:
            if mov < 0 :
                rot = -rot
            self.rad += rot * self.rotSpeed
        
        #print("body",self.rad)
        if mov != 0:
            #if self.key[SDLK_s] and (self.key[SDLK_a] or self.key[SDLK_d]) :
             #   self.x += -mov * self.backSpeed * math.sin(self.rad)
              #  self.y += mov * self.backSpeed * math.cos(self.rad)
            #else:
                self.x += mov * self.moveSpeed * math.cos(self.rad)
                self.y += mov * self.moveSpeed * math.sin(self.rad)

        #print(self.x,self.y)

    def handle_event(self, keys):
        if keys.type == SDL_KEYDOWN or keys.type == SDL_KEYUP :
            if keys.key in Body.keysType:
                self.key[keys.key] = keys.type == SDL_KEYDOWN # if key[keys.key] in Body.keyType == True:

                #print(self.key[keys.key])
                #print(keys.key)
class Barrel:
    global player
    def __init__(self):
        self.image = load_image('../res/object/character/player_barrel_pix2.png')
        self.x,self.y = player.x,player.y
        self.mx,self.my = 0, 0
        self.rot = 0
        self.rotSpeed = 0.1 * math.pi/60

    def update(self):
        #print("barrel",player.rad)
        self.x, self.y = player.x, player.y


    def draw(self):
        self.image.composite_draw(self.rot,"",self.x ,self.y)
        self.rot = math.atan2(self.y - self.my,self.x - self.mx)
        #print("rot",self.rot)


    def handle_event(self,point):
        if point.type == SDL_MOUSEMOTION:
            self.mx,self.my = point. x,600 - point.y





#eighth define function

#ninth redefine game_framework's function
def enter():
    global player,barrel
    player = Body()
    barrel = Barrel()


def exit():
	pass

def draw():
    global player,barrel
    clear_canvas()
    player.draw()
    barrel.draw()
    update_canvas()

def update():
    global player,barrel
    player.update()
    barrel.update()

def handle_events():
    global player,barrel
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        else:
            player.handle_event(key)
            barrel.handle_event(key)



def pause():
	pass

def resume():
	pass



#start to this module
if __name__ == '__main__':
	import sys
	glCurrentModule = sys.modules[__name__]
	open_canvas()
	gf.run(glCurrentModule)
	close_canvas()

