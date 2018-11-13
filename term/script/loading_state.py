
#//-----------------/This module's name is 'loading_state'/------------------//
#//-----------------/prev module is 'logo_state'/----------------------------//
#//----------------/This moudle has almost moudles/------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//


from pico2d import *
import game_framework as gf
import json
import math

global loadimage
global glStartTime

class loadingImage:
    def __init__(self):
        self.loading_state_image = load_image('../res/ui/logo_title/loading_image_pix.png')
        self.object_player_image ={
            "player_body":load_image("../res/object/character/player_body_pix2.png"),
            "player_barrel": load_image('../res/object/character/player_barrel_pix2.png')
        }
        self.object_enemy_image = {
            "bagic_enemy": load_image('../res/object/enemy/bagic_enemy.png')
        }
class loadingState:
    def __init__(self):
        op= open('object.json')
        data = json.load(op)
        
        self.player = data["player"][0]
        self.enemy = data[][]

        
        op.close()


def enter():
    global loadimage = loadingImage()
    global loadstate = loadingState()
   

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

