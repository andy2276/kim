
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

import delta_time as tm

logo = None
flowTime = 0.0

def enter():
	global logo
	logo = load_image('../res/ui/logo_title/kpu_credit.png')

def exit():
	global logo
	del logo

def draw():
	clear_canvas()
	logo.draw(get_canvas_width()/2, get_canvas_width()/2)
	update_canvas()

def update():
	global logo,flowTime
	gf.change_state(loading_state) if flowTime >= 60.0

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


