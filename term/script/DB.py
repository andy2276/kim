from pico2d import *

import game_framework as gf

import math

class stageInfo:
    def __init__(self):
        self.selectPlayer = 0


class HUI:
    def __init__(self,sX,sY,sW,sH):
        self.x,self.y =sX,sY
        self.w,self.h = sW,sH



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
    global player,barrel
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


if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas(1200,800)

    gf.run(glCurrentModule)
    close_canvas()