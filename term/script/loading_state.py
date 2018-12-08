
#//-----------------/This module's name is 'loading_state'/------------------//
#//-----------------/prev module is 'logo_state'/----------------------------//
#//----------------/This moudle has almost moudles/------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//

#blocks 15X15!!


print("welcom to loading_state!!")
from pico2d import *
import game_framework as gf
import json

import delta_time

# global TESTINGGAME,TIMEDELAY,C_WIDTH,C_HIEGHT,CW_HALF,CH_HALF,loadImages,loadState,loadCount,loadBlocks

global MOVE_TIME



TESTINGGAME = False
TIMEDELAY = 0

C_WIDTH, C_HIEGHT = 1200,800
CW_HALF,CH_HALF = C_WIDTH/2, C_HIEGHT/2

class LoadingState:
    def __init__(self):
        global TESTINGGAME,TIMEDELAY

        test = open("testOption.json")
        data = json.load(test)
        if 1 == data["test"]:
           TESTINGGAME = True
        TIMEDELAY = data["delayTime"]
        test.close()

        map = open("stageInMap.json")
        self.mapData = json.load(map)
        map.close()

        stage = open("stageInfo.json")
        self.stageData = json.load(stage)
        stage.close()

        op = open("object.json")
        datas = json.load(op)
        self.player = datas["player"]
        self.enemy = datas["enemy"]
        op.close()



class LoadingImage:
    def __init__(self):
        global TESTINGGAME
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
        if TESTINGGAME:
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
        self.main_menu_image = {"background":load_image("../res/ui/main/background_fix.png"),
            "battleUI":load_image("../res/ui/main/battleUI.png"),
            "selectUI":load_image("../res/ui/main/selectUI.png"),
            "mainFont":load_image("../res/ui/main/mainFont_fix.png"),
            "bagic_player":load_image("../res/ui/main/select2.png"),
            "super_player":load_image("../res/ui/main/select1.png"),
            "goUI":load_image("../res/ui/main/goUI.png")
        }

        self.imageCount = 7

loadImages = None
loadState = None
loadCount = 0
loadBlocks = []

loadTerrain = []
class UI:
    def __init__(self,sN, sX, sY, sW, sH, sImgN):

        self.name = sN
        self.x, self.y = sX, sY
        self.w, self.h = sW, sH

        self.imageNum = sImgN

        self.handOn = False
        self.clickOn = False
        self.clickOff = False
        self.eventOn = False
        self.eventTime = 0


        self.left,self.bottom = self.x- self.w/2,self.y - self.h/2
        self.right,self.top = self.x + self.w/2,self.y+self.h/2
        self.widthRange = self.right - self.left
        self.highRange = self.top - self.bottom


    def draw(self):
        global loadImages
        loadImages.main_menu_image[self.name].draw(self.x,self.y)

    def update(self):
        if self.clickOff and self.handOn:
            self.eventOn = True
        else:
            self.eventOn = False
        pass





    def handle_event(self,keys):
        if keys.x != None:
            self.eventOn = False
            if self.left <= keys.x and keys.x <=self.right and self.bottom <= C_HIEGHT-keys.y  and C_HIEGHT-keys.y <= self.top:
                self.handOn = True
            elif False == (self.left <= keys.x and keys.x <=self.right and self.bottom <= C_HIEGHT-keys.y  and C_HIEGHT-keys.y <= self.top):
                self.handOn = False

            if (keys.type,keys.button) == (SDL_MOUSEBUTTONUP,SDL_BUTTON_LEFT):
                self.clickOff = True
            else:
                self.clickOff = False
            if (keys.type,keys.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                self.clickOn = True
            else:
                self.clickOn = False

        # print(self.handOn,self.clickOn,self.eventOn)
        # if self.handOn:
        #     print("hangOn!!")
        # if self.clickOn:
        #     print("clickOn!!")
        # if self. eventOn:
        #     print("eventOn!!")


class selectUI(UI):
    def __init__(self,sN, sX, sY, sW, sH, sImgN,sOption = True):
        self.name = sN
        self.x, self.y = sX, sY
        self.w, self.h = sW, sH

        self.imageNum = sImgN

        self.handOn = False
        self.clickOn = False
        self.clickOff = True
        self.eventOn = False
        self.eventTime = 0

        self.selfOption = sOption
        if self.selfOption == False:
            self.optionVar = 0


        self.k = 0

        self.left, self.bottom = self.x - self.w / 2, self.y - self.h / 2
        self.right, self.top = self.x + self.w / 2, self.y + self.h / 2
        self.widthRange = self.right - self.left
        self.highRange = self.top - self.bottom

    def draw(self):
        global loadImages
        if self.selfOption:
            if self.handOn:
                self.k = 1
                if self.eventOn:
                    self.k = 2
            else:self.k = 0


        loadImages.main_menu_image[self.name].clip_draw(self.k*self.w,self.imageNum*self.h,self.w,self.h, self.x, self.y)

def enter():
    global loadImages,loadState,loadCount,loadBlocks,loadTerrain
    open_canvas(C_WIDTH, C_HIEGHT)
    loadState = LoadingState()
    loadImages = LoadingImage()


    initBox = []

    for y in range(15):
        for x in range(15):
            initBox.append((loadImages.object_structure_image["blocks"]).clip_image(100*x,100*y,100,100))
        loadBlocks.append(initBox)
        initBox = []

    for y in range(3):
        for x in range(3):
            loadTerrain.append(loadImages.map_terrain_image["base"].clip_image(150*y,150*x,150,150))

    loadCount =0

def exit():
    close_canvas()
    global  loadImages,loadState,loadCount,loadBlocks,loadTerrain
    print("loading close!")
    loadImages = None
    loadState = None
    loadCount = 0
    loadBlocks = []
    loadTerrain = []
    del loadImages,loadState,loadCount,loadBlocks,loadTerrain
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
    global loadImages, loadCount,loadImages,loadState,loadCount,loadBlocks,TESTINGGAME
    loadCount += 5 if loadCount <=47 else 0

    delay(1/60)
    handle_events()
    if loadCount >=47:
        import menu
        gf.push_state(menu)


def handle_events():
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
def pause():
    print("loading on!!")
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

