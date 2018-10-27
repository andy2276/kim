
#//-----------------/This module's name is 'player_class'/------------------//
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

#fifth initializing module variables(for using to any modul)

#sixth initializing global variables(for only using this module)

#seventh define class

class clPlayerBody:
    def __init__(self):
        self.mvX, self.mvY = 300,200 #X & Y
        self.mvHp, self.mvSpeed = 10,10.0#state
        self.mvRotateR, self.mvRotateL = 0,0#rotate
        self.mvImage = load_image("../res/object/character/player_body_pix.png")
        self.mvRoImage = None#image

    def draw(self):
        self.mvImage.draw(self.mvX,self.mvY)
        
    def update(self):
        pass
    def handle_event(self):
        pass
        


#eighth define function

#ninth redefine game_framework's function
def enter():
    global player,pressing
    pressing = False

    player = clPlayerBody()
	

def exit():
	pass

def draw():
    global player
    clear_canvas()
    player.draw()
    update_canvas()
	

def update():
	pass
def handle_events():
    global player,pressing
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gf.quit()
        if event.type ==SDL_KEYDOWN:
            pressing = True
        if pressing == True:
            if event.type == SDL_KEYUP:
                pressing = False
            if  event.key == SDLK_RIGHT:
                player.mvX += 10
            if event.key == SDLK_LEFT:
                player.mvX -= 10
            
	

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

