
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
        self.mvX,self.mvY #X & Y
        self.mvHp,self.mvSpeed#state
        self.mvRotate#rotate
        self.mvImage,self.mvRoImage#image
class clPlayerBarrel:
    def __init__(self):
        self.mvCenterX,self.mvCenterY
        self.mvMouseX,self.mvMouseY
        self.mvBarrelimage
#eighth define function

#ninth redefine game_framework's function
def enter():
	pass

def exit():
	pass

def draw():
	pass

def update():
	pass
def handle_events():
	pass

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

