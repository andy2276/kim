import random
import sys
sys.path.insert(0,'..//hw_0928')
from pico2d import *

import game_framework as gf


from boy import Boy
from grass import Grass

boy = None
grass = None



def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass
    del boy
    del grass



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gf.quit()
        elif event.type == SDL_KEYDOWN:
            gf.quit()
        else:
            boy.handle_event(event)

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()

if __name__ == '__main__':
	glCurrentModule = sys.modules[__name__]	
	open_canvas()
	gf.run(glCurrentModule)
	close_canvas()


