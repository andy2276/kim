
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
GSIV = {"startX": 2, "startY": 2, "startAngle": 0}#trans jason and test


#seventh define class
class Body:
    #keysType = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]
    keysType = [SDLK_a, SDLK_d, SDLK_w, SDLK_s]#97,100,119,115

    def __init__(self):
        self.image = load_image("../res/object/character/player_body_pix.png")

        #self.x, self.y = get_canvas_width()/ GSIV["startX"] , get_canvas_height()/GSIV["startY"]
        self.x, self.y = 400, 400
        self.rad = GSIV["startAngle"]
        self.rotSpeed = 1 * math.pi/60
        self.key = {}
        for k in Body.keysType:
            #print(k)
            self.key[k] = False  #type init
            #print(self.key[k])
    def draw(self):
        self.image.composite_draw(self.rad,"",self.x,self.y)
        #self.image.draw(self.x,self.y)

    def update(self):
        mag = 1 if self.key[SDLK_a] else 0 # mag is 1. if self.key is True. else if 0
        mag += -1 if self.key[SDLK_d] else 0
        #move = 1 if self.key[SDLK_UP] else 0
        #move += -1 if self.key[SDLK_DOWN] else 0

        print(mag)


    def handle_event(self, keys):
        if keys.type == SDL_KEYDOWN or keys.type == SDL_KEYUP :

            if keys.key in Body.keysType:
                self.key[keys.key] = keys.type == SDL_KEYDOWN # if key[keys.key] in Body.keyType == True:

                #print(self.key[keys.key])
                #print(keys.key)







#eighth define function

#ninth redefine game_framework's function
def enter():
    global player
    player = Body()


def exit():
	pass

def draw():
    global player
    clear_canvas()
    player.draw()
    update_canvas()

def update():
    global player
    player.update()

def handle_events():
    global player
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        else:
            player.handle_event(key)

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

