
#//-----------------/This module's name is 'logo_state'/-------------------//
#//-----------------/prev module is 'main.py'/-------------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//


#first import pico2d
from pico2d import *
#second import game_framework - keyword 'as' is only use game_framework
import game_framework as gf
#third import next module
import loading_state
#fourth import need module
import time
#fifth initializing module variables(for using to any modul)

#sixth initializing global variables(for only using this module)

global glLogoImage,glStartTime

#seventh define class

#eighth define function

#ninth redefine game_framework's function
def enter():
	global glLogoImage,glStartTime
	glStartTime = time.time()
	glLogoImage = load_image('../res/ui/logo_title/kpu_credit.png')

def exit():
	global glLogoImage
	del glLogoImage

def draw():
	clear_canvas()
	glLogoImage.draw(400, 300)
	update_canvas()

def update():
        global glStartTime
        lcMidTime = time.time() - glStartTime
        if lcMidTime >= 0.5:
                gf.change_state(loading_state)
                return
        delay(0.02)
	

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


