
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
# class loadingImage:
#     def __init__(self):
#         self.loading_state_image = load_image('../res/ui/logo_title/loading_image_pix.png')
#
#         self.object_player_image = {
#             "player_body": load_image("../res/object/character/player_body_pix2.png"),
#             "player_barrel": load_image('../res/object/character/player_barrel_pix2.png')
#         }
#         self.object_player_colBox_image = {
#             "player_colBox": load_image("../res/object/character/player_box.png")
#         }
#         self.object_enemy_image = {
#             "bagic_enemy": load_image('../res/object/enemy/bagic_enemy.png')
#         }
#         self.object_enemy_colBox_image = {
#             "bagic_enemy": load_image('../res/object/enemy/bagic_enemy_box.png')
#         }


class loadingState:
    def __init__(self):
        op= open('object.json')
        data = json.load(op)

        self.player = data["player"][0]
        #self.enemy = data[][]

        
        op.close()

loadImages = None


class LoadingImage:
    def __init__(self):
        self.loading_state_image = load_image('../res/ui/logo_title/loading_image_pix.png')

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




def enter():
    global loadImages
    loadImages = LoadingImage()
    print("in Loading State!")



def exit():
   pass



def draw():
    global loadImages
    clear_canvas()


    loadImages.loading_state_image.draw(get_canvas_width()/2,get_canvas_height()/2)


    update_canvas()





def update():

    handle_events()


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

