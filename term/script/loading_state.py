
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
import delta_time
import object_control

C_WIDTH, C_HIEGHT = 1200,800
CW_HALF,CH_HALF = C_WIDTH/2, C_HIEGHT/2

class loadingState:
    def __init__(self):
        op= open('object.json')
        data = json.load(op)

        self.player = data["player"][0]
        #self.enemy = data[][]

        
        op.close()

loadImages = None
loadCount = 0

class LoadingImage:
    def __init__(self):
        self.loading_state_image = {"backGround":load_image('../res/ui/logo_title/loading_image_pix.png'),
         "loadingBar": load_image('../res/ui/logo_title/loading_bar.png')}

        self.object_player_image = {"player_body": load_image("../res/object/character/player_body_pix2.png"),
            "player_barrel": load_image('../res/object/character/player_barrel_pix2.png')
        }
        self.object_player_colBox_image = {
            "player_colBox": load_image("../res/object/character/player_box.png")
        }
        self.object_enemy_image = {
            "bagic_enemy": load_image('../res/object/enemy/bagic_enemy.png')
        }
        self.object_enemy_colBox_image = {
            "bagic_enemy": load_image('../res/object/enemy/bagic_enemy_box.png')
        }
        self.object_projectile_image = {
            "missile_bagic":load_image('../res/object/projectile/missile_bagic.png')
        }
        self.imageCount = 7



def enter():
    global loadImages,loadCount
    open_canvas(C_WIDTH, C_HIEGHT)
    loadImages = LoadingImage()
    loadCount =0

def exit():
    close_canvas()
    pass



def draw():
    global loadImages,loadCount
    clear_canvas()
    loadImages.loading_state_image["backGround"].draw(CH_HALF+200,CH_HALF)
    loadImages.loading_state_image["loadingBar"].clip_draw(0, 35, 450, 35,CH_HALF+200, CH_HALF-300)
    loadImages.loading_state_image["loadingBar"].clip_draw(0, 0, 10 * loadCount, 35, CH_HALF-25 + (10 * loadCount) / 2,
                                                           CH_HALF - 300)

    update_canvas()





def update():
    global loadImages, loadCount
    loadCount += 5 if loadCount <=42 else 0

    handle_events()
    if loadCount <=42:
        gf.push_state(object_control)


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
    open_canvas(C_WIDTH, C_HIEGHT)
    gf.run(glCurrentModule)
    close_canvas()

