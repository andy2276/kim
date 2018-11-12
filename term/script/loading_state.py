
#//-----------------/This module's name is 'loading_state'/------------------//
#//-----------------/prev module is 'logo_state'/----------------------------//
#//----------------/This moudle has almost moudles/------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//


from pico2d import *
import game_framework as gf
import math

global glLoadingImage
global glStartTime

class loadingImage:
    def __init__(self):
        self.loading_state_image = load_image('../res/ui/logo_title/loading_image_pix.png')
        


def enter():
   pass

def exit():
   pass



def draw():
    clear_canvas()

    update_canvas()
    pass

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

#start to this module
if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]	
    open_canvas()
    gf.run(glCurrentModule)
    close_canvas()

