
#//-----------------/This module's name is 'loading_state'/------------------//
#//-----------------/prev module is 'logo_state'/----------------------------//
#//----------------/This moudle has almost moudles/------------------------//
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
global glLoadingImage
global glStartTime
#seventh define class

#eighth define function

#ninth redefine game_framework's function
def enter():
    global glLoadingImage,glStartTime
    glLoadingImage = load_image('../res/ui/logo_title/loading_image.png')
def exit():
    global glLoadingImage
    del glLoadingImage
    pass

def draw():
    clear_canvas()
    glLoadingImage.draw(400,300)
    update_canvas()
    pass

def update():
        delay(0.03)
def handle_events():
    event = get_events()
    for e in event:
        if e.type == SDL_QUIT:
            gf.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                gf.quit()
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

