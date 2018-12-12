
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
        stru = open("stageInStructure.json")
        self.structData = json.load(stru)
        stru.close()

        stage = open("stageInfo.json")
        self.stageData = json.load(stage)
        stage.close()

        op = open("object.json")
        datas = json.load(op)
        self.player = datas["player"]
        self.enemy = datas["enemy"]
        self.projectile = datas["projectile"]
        self.weaponCount = datas["weaponKindCount"]
        self.attackKind = datas["attackKind"]
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
            "fireball":load_image('../res/object/projectile/missile.png'),
            "energy":load_image("../res/object/projectile/energy.png")
        }
        #self.object_projectile_image["cannonball"].
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
            "goUI":load_image("../res/ui/main/goUI.png"),
            "stageClear":load_image("../res/ui/main/stageClear.png")
        }

        self.imageCount = 7
class LoadingSound():
    def __init__(self):
        self.playerSound = {
            "fire_cannon":[load_music("player_fire_cannon.mp3"),load_music("player_fire_cannon2.mp3")],
            "fire_fireball": [load_music("player_fire_fireball.mp3"),load_music("player_fire_fireball2.mp3"),load_music("player_fire_fireball3.mp3")],
            "fire_energy": load_music("player_fire_energy.mp3"),
            "move": [load_music("player_move1.mp3"),load_music("player_move2.mp3")],
            "reload_need": load_music("player_need_reload.mp3"),
            "reload_reload": load_music("player_reload.mp3"),
        }

        self.enemySound = {
            "enemy_fire":load_music("enemy_fire.mp3"),
        }
        self.bgSound = {
            "boom":[load_music("boom1.mp3"),load_music("boom2.mp3"),load_music("boom3.mp3")],
            "main_menu":load_music("main_menu.mp3"),
            "ingame":load_music("ingame_bg.mp3")
        }
        self.uiSound ={
            "menu_intro": load_music("menu_intro.mp3"),
            "menu_hovr": load_music("menu_click.mp3"),
            "menu_click": load_music("click.mp3")
        }


loadImages = None
loadSound = None
loadState = None
loadCount = 0
loadBlocks = []
loadTerrain = []
loadProjectile = []
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
    global loadImages,loadState,loadCount,loadBlocks,loadTerrain,loadSound
    open_canvas(C_WIDTH, C_HIEGHT)
    loadState = LoadingState()
    loadSound = LoadingSound()
    loadImages = LoadingImage()


    loadBlocks = loadImages.object_structure_image["blocks"]

    stageMaps = []
    for s in range(3):
        for y in range(3):
            for x in range(3):
                stageMaps.append(loadImages.map_terrain_image["base"].clip_image(150*y,150*x,150,150))
        loadTerrain.append(stageMaps)
    loadCount =0

    loadSound.uiSound["menu_intro"].set_volume(128)
    loadSound.uiSound["menu_intro"].repeat_play()

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
    global loadImages, loadCount,loadImages,loadState,loadCount,loadBlocks,TESTINGGAME,MOVE_TIME

    loadCount += 1 if loadCount <=46 else 0
    print(loadCount)
    handle_events()
    if loadCount >=46:
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

