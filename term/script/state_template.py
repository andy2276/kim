
#//-----------------This module's name is 'state_template'-------------------//
#//-----------------prev module is 'None'-------------------------------//
#//---------------------Notice End-----------------------------------------//


#first import pico2d
from pico2d import *
#second import game_framework - keyword 'as' is only use game_framework
import game_framework as gf
#third import next module

#fourth import need module

#fifth initializing module variables(for using to any modul)

#sixth initializing global variables(for only using this module)

#seventh define class

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

