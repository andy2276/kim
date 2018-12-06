from pico2d import *

import game_framework as gf
import  loading_state as lo
import math

class stageInfo:
    def __init__(self):
        self.selectPlayer = 0



def enter():
    pass

def exit():
	pass

def draw():
    global player,enemy,projectile,structure
    clear_canvas()

    update_canvas()


def update():
   pass

def handle_events():
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()


def pause():
	pass

def resume():
	pass


if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas(1200,800)

    gf.run(glCurrentModule)
    close_canvas()