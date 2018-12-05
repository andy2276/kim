
#//-----------------/This module's name is 'loading_state'/------------------//
#//-----------------/prev module is 'logo_state'/----------------------------//
#//----------------/This moudle has almost moudles/------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//

#blocks 15X15!!

from pico2d import *
import game_framework as gf
import json
import delta_time
import object_control

C_WIDTH, C_HIEGHT = 1200,800
CW_HALF,CH_HALF = C_WIDTH/2, C_HIEGHT/2

class LoadingState:
    def __init__(self):
        op = open("object.json")
        datas = json.load(op)
        self.player = datas["player"]
        self.enemy = datas["enemy"]

        op.close()


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
            "cannonball":load_image('../res/object/projectile/cannonball.png'),
            "missile":load_image('../res/object/projectile/missile.png')
        }
        self.object_structure_image = {"blocks":load_image("../res/object/structure/structure_block_fix.png")
        }
        self.map_terrain_image = {"base":load_image("../res/object/structure/base_fix.png")

        }
        self.imageCount = 7

loadImages = None
loadState = None
loadCount = 0
loadBlocks = []

loadTerrain = []

def enter():
    global loadImages,loadState,loadCount,loadBlocks,loadTerrain
    open_canvas(C_WIDTH, C_HIEGHT)
    loadImages = LoadingImage()
    loadState = LoadingState()

    initBox = []
    initMap = []
    for y in range(15):
        for x in range(15):
            initBox.append((loadImages.object_structure_image["blocks"]).clip_image(100*x,100*y,100,100))
        loadBlocks.append(initBox)
        initBox = []

    for y in range(3):
        for x in range(3):
            initMap.append(loadImages.map_terrain_image["base"].clip_image(150*y,150*x,150,150))
        loadTerrain.append(initMap)
        initMap = []

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
    global loadImages, loadCount,loadImages,loadState,loadCount,loadBlocks
    loadCount += 5 if loadCount <=47 else 0

   #  #----------------------
   #  if loadImages == None:
   #      loadImages = LoadingImage()
   #
   #      loadCount = curTime - allTime
   #      allTime = curTime
   #  if loadState == None:
   #      loadState = LoadingState()
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   # #---------------------
    delay(1/60)
    handle_events()
    if loadCount >=47:
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

