

#//-----------------This module's name is 'logo_state'---------------------//
#//-----------------prev module is 'main.py'-------------------------------//
#//---------------------Notice End-----------------------------------------//


#first import pico2d
from pico2d import *
#second import game_framework - keyword 'as' is only use game_framework
import game_framework as gf
#third import next module

#fourth import need module
import time
#fifth initializing module variables(for using to any modul)

#sixth initializing global variables(for only using this module)


def enter():
	

def exit():
	
	

def draw():
	clear_canvas()
	logo.draw(400, 300)
	update_canvas()

def update():
	

def handle_events():
	pass

def pause():
	pass

def resume():
	pass

#start to this module
if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()

