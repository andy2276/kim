
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


logo = None
loadingBar = None
flowTime = 0.0
test = 0

def enter():
	global logo
	open_canvas()
	logo = load_image('../res/ui/logo_title/kpu_credit.png')



def exit():
	close_canvas()
	global logo
	del logo

def draw():
	global logo
	clear_canvas()
	logo.draw(get_canvas_width()/2, get_canvas_width()/2-100)
	update_canvas()

def update():
	global logo,flowTime

	if flowTime >=3.0:
		gf.change_state(loading_state)
		handle_events()
	else :
		delay(0.1)
		flowTime += 1.0



def handle_events():
	events = get_events()
	for key in events:
		if key.type == SDL_QUIT:
			gf.quit()
		elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			gf.pop_state()

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


